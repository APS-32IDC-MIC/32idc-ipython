print(__file__)

from ophyd import (EpicsScaler, EpicsSignal, EpicsSignalRO,
                   Device, DeviceStatus, EpicsSignalWithRBV)
from ophyd import Device
from ophyd import Component as Cpt
from ophyd import PointGreyDetector
from ophyd import SingleTrigger
from ophyd import AreaDetector
from ophyd import HDF5Plugin
import bluesky

import time


aps_current = EpicsSignal("S:SRcurrentAI", name="aps_current")


## Beam Monitor Counts
#bs_bm2 = EpicsSignalRO('BL14B:Det:BM2', name='bs_bm2')


if False:
    # from 32idcSIM sim detector IOC
    noisy = EpicsSignalRO('32idcSIM:userCalc1', name='noisy')
    scaler = EpicsScaler('32idcSIM:scaler1', name='scaler')

    # Point Grey detector in 32-ID-C
    AreaDetector_PV_prefix = "32idcPG3:"
    #pg3 = PointGreyDetector(AreaDetector_PV_prefix)


    class myHDF5Plugin(Device):
        """custom handling of the HDF5 file writing plugin"""
        # NOTE: ophyd.areadetector.HDF5Plugin does not work with AD2.4, use Device for now
 
        array_callbacks        = Cpt(EpicsSignalWithRBV, 'ArrayCallbacks')
        enable_callbacks       = Cpt(EpicsSignalWithRBV, 'EnableCallbacks')
        auto_increment         = Cpt(EpicsSignalWithRBV, 'AutoIncrement')
        auto_save              = Cpt(EpicsSignalWithRBV, 'AutoSave')
        file_path              = Cpt(EpicsSignalWithRBV, 'FilePath', string=True)
        file_name              = Cpt(EpicsSignalWithRBV, 'FileName', string=True)
        file_number            = Cpt(EpicsSignalWithRBV, 'FileNumber')
        file_template          = Cpt(EpicsSignalWithRBV, 'FileTemplate', string=True)
        file_write_mode        = Cpt(EpicsSignalWithRBV, 'FileWriteMode')
        full_file_name         = Cpt(EpicsSignalRO, 'FullFileName_RBV', string=True)
        store_attributes       = Cpt(EpicsSignalWithRBV, 'StoreAttr', string=True)
        store_performance_data = Cpt(EpicsSignalWithRBV, 'StorePerform', string=True)
        write_file             = Cpt(EpicsSignalWithRBV, 'WriteFile')
        xml_layout_file        = Cpt(EpicsSignalWithRBV, 'XMLFileName', string=True)


    class Pg3Detector(SingleTrigger, AreaDetector):
        hdf1 = Cpt(myHDF5Plugin, 'HDF1:')
 
    pg3 = Pg3Detector(AreaDetector_PV_prefix)


    def mona_notifier(*args, **kws):
        """receive noticie a new image frame file is available, by name"""
        print("tell the world this file is ready: ", args[0])


    WAIT_FILE_NAME_READY_POLL_TIME_s = 0.001

    class FrameNameCallback(bluesky.callbacks.core.CallbackBase):
        """
        callback handler: tell MONA we have a new image frame file
        """
 
        def __init__(self, *args, hdf=None, **kws):
            self.plan_name = None
            self.short_uid = None
            self.scan_id = None
            self.hdf = hdf
 
        def start(self, doc):
            self.plan_name = doc["plan_name"]
            self.short_uid = doc["uid"].split("-")[0]
            self.scan_id = doc["scan_id"]
 
        def event(self, doc):
          if self.hdf is not None:
            # TODO: gross hack - should not need polling loop here
            # TODO: How to use subscribe() on the file name PV
            while (self.hdf.write_file.get() != 0):
                sleep(WAIT_FILE_NAME_READY_POLL_TIME_s)
            frame_name = self.hdf.full_file_name.get()
            mona_notifier(frame_name)

        #def stop(self, doc):
        #  print("stopped: ", doc["uid"].split("-")[0])
