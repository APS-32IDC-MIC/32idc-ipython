print(__file__)

# Bluesky callbacks (scan data handling)


class FrameNotifier(bluesky.callbacks.core.CallbackBase):
    """
    """

    def __init__(self, *args, path=None, hdf=None, **kws):
        self.hdf = hdf
        self.path = path or os.getcwd()
        if os.path.exists(self.path):
            if not self.path.endswith(os.sep):
                # must end with '/'
                self.path += os.sep
        else:
            msg = 'path: ' + self.path + ' does not exist'
            raise ValueError(msg)

    def start(self, doc):
        if self.hdf is not None:
            #print(str(self.hdf))
            short_uid = doc["uid"].split("-")[0]
            self.hdf.enable_callbacks.put('Enable')
            self.hdf.array_callbacks.put('Enable')
            self.hdf.file_path.put(self.path)
            self.hdf.file_name.put('ts_' + short_uid)
            self.hdf.file_template.put('%s%s_%5.5d.h5')
            # # coordinate with BlueSky sequence numbers, which start at 1
            self.hdf.file_number.put(1)
            self.hdf.file_write_mode.put('Single')
            self.hdf.auto_increment.put('Yes')
            self.hdf.auto_save.put('Yes')

    def event(self, doc):
        if self.hdf is not None:
            frame_name = self.hdf.full_file_name.get()
            #print(frame_name)
            #print(sorted(doc['data'].keys()))
            if False:
                # this is where we send info to the Verifier or Analysis pipeline
                # required this setup:
                #  simdet.hdf1.read_attrs = ['full_file_name']
                #-------------
                # emit: motor position, time, data file name, ?frame number?
                # look into sending by zeromq or by EPICS PVs or by json
                # perhaps a handshake from verifier that image has been received?
                #-------------
                print(doc['data'][self.hdf.name + '_full_file_name'])


class EPICSNotifierCallback(bluesky.callbacks.core.CallbackBase):
    """
    demo of a callback handler: update a couple EPICS string PVs
    """

    def __init__(self, notices, *args, **kws):
        self.notices = notices
        self.num_projections = None
        self.plan_name = None
        self.short_uid = None
        self.scan_id = None
        self.scan_label = None
        self.notices.post("", "")

    def start(self, doc):
        self.plan_name = doc["plan_name"]
        self.short_uid = doc["uid"].split("-")[0]
        self.scan_id = doc["scan_id"]
        self.num_projections = doc["num_projections"]
        self.scan_label = "%s %d (%s)" % (self.plan_name, self.scan_id, self.short_uid)
        msg = "start: " + self.scan_label
        self.plan_name + ': ' + self.short_uid
        self.notices.post(msg, "")

    def event(self, doc):
        msg = "event %d of %d" % (doc["seq_num"], self.num_projections)
        progress = 100.0 * doc["seq_num"] / self.num_projections
        msg += " (%.1f%%)" % progress
        self.notices.post(None, msg)

    def stop(self, doc):
        msg = "End: " + self.scan_label
        self.notices.post(msg, "")


class PreTomoScanChecks(bluesky.callbacks.core.CallbackBase):
    """
    callback handler: update a couple EPICS string PVs

    ATTRIBUTES

    :param readable source_intensity: signal that describes source intensity now

    ATTRIBUTES

    :param float source_intensity_threshold:
        minimum acceptable source intensity
        (default: 1.0 in units of `source_intensity`)
    :param int report_interval:
        when waiting for beam, make UI reports on this interval
        (default: 60, units: seconds)
    :param int recheck_interval:
        when waiting for beam, re-check on this interval
        (default: 1, units: seconds)
    """

    def __init__(self, motor, source_intensity=None):
        self.motor = motor
        self.source_intensity = source_intensity
        self.source_intensity_threshold = 1.0   # arbitrary default
        self.report_interval = 60
        self.recheck_interval = 1

    def start(self, doc):
        self.check_beam()

        self.check_motor_moving(self.motor)

        args = doc["plan_args"]
        for key in "start stop".split():
            self.check_motor_limits(self.motor, args[key])

    def check_beam(self):
        if self.source_intensity is not None:
            t_ref = time.time.now()
            t_update = t_ref + 1    # first report comes early
            while self.source_intensity < self.source_intensity_threshold:
                t = time.time.now()
                if t >= t_update:
                    t_update += t + self.report_interval
                    h = int((t - t_ref + 0.5) / 3600)
                    m = int(((t - t_ref + 0.5) % 3600) / 60)
                    s = int((t - t_ref + 0.5) % 60)
                    msg = 'waiting for beam:'
                    if h > 0:
                        msg += ' %dh' % h
                    if h > 0:
                        msg += ' %dm' % m
                    msg += ' %ds' % s
                    #logger.info(msg)
                    print(msg)


    def check_motor_moving(self, motor):
        # TODO: this assume a PyEpics motor object, generalize this check
        assert(isinstance(motor, ophyd.epics_motor.EpicsMotor))
        if not motor.motor_done_move:
            msg = "motor " + motor.name + " is moving, scan canceled"
            raise ValueError(msg)

    def check_motor_limits(self, motor, target):
        # ? backlash distance ?
        assert(isinstance(motor, ophyd.pv_positioner.PVPositioner))
        try:
            motor.check_value(target)
        except ValueError:
            msg = str(target)
            msg += " is outside of limits ("
            msg += str(motor.limits[0])
            msg += ", "
            msg += str(motor.limits[1])
            msg += ") for motor " + motor.name
            msg += ", scan canceled"
            raise ValueError(msg)
