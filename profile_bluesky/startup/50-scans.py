print(__file__)

# Bluesky plans (scans)


def interlace_tomo_scan(
    detectors, 
    motor, 
    start, 
    stop, 
    inner_num, 
    outer_num, 
    *, 
    per_step=None, 
    md={}, 
    snake=False, 
    bisection=False):
    """
    interlace tomography scan plan (based on `plans.scan()`)
    
    :see: https://github.com/dgursoy/mona/blob/master/trunk/32id/tomo_step_scan.py
    :seealso: http://nsls-ii.github.io/bluesky/bluesky.plans.scan.html#bluesky.plans.scan
    :seealso: https://github.com/NSLS-II/bluesky/blob/master/bluesky/plans.py#L2032

    Parameters
    ----------
    
    :param [readable] detectors: list of 'readable' objects
    :param obj motor: instance of `setable` (motor, temp controller, etc.)
    :param float start: first position of `motor`
    :param float stop: last position of `motor`
    :param int inner_num: number of projections in the inner loop
    :param int outer_num: number of projections in the outer loop
    :param obj per_step: (optional) a `callable`

        * custom override of standard inner loop handling (at each point of the scan)
        * Expected signature: ``f(detectors, motor, step)``
    
    :param dict md: (optional) metadata dictionary
    :param bool snake: (optional) move inner loop back and forth or always in given direction (default: False)
    :param bool bisection: (optional) adjust outer loop to step by bisecting its range (default: False)

    See Also
    --------
    :func:`bluesky.plans.scan`
    """
    # work out the sequence of projections in advance, normal 1-D scan handling after that
    inner = np.linspace(start, stop, inner_num)
    outer = np.linspace(0, inner[1]-inner[0], 1+outer_num)
    if bisection:
        outer = np.array(bisection_shuffle(outer))
    projections = inner
    for i, offset in enumerate(outer[1:]):
        if snake and i%2 == 0:
            # http://stackoverflow.com/questions/6771428/most-efficient-way-to-reverse-a-numpy-array#6771620
            projections = np.append(projections, offset + inner[::-1])
        else:
            projections = np.append(projections, offset + inner)
    # only keep the unique points within the range: start ...stop
    unique = []
    for position in ma.compressed(ma.masked_outside(projections, start, stop)):
        if position not in unique:
            unique.append(position)
    # projections = ma.compressed(ma.masked_outside(projections, start, stop))
    projections = unique
    
    num = len(projections)

    _md = {'detectors': [det.name for det in detectors],
          'motors': [motor.name],
          'num_projections': num,
          'plan_args': {'detectors': list(map(repr, detectors)), 'num': num,
                        'motor': repr(motor),
                        'start': start, 'stop': stop,
                        'per_step': repr(per_step)},
          'plan_name': inspect.currentframe().f_code.co_name,
          'plan_pattern': 'linspace',
          'plan_pattern_module': 'numpy',
          'plan_pattern_args': dict(start=start, 
                                    stop=stop, 
                                    inner_num=inner_num, 
                                    outer_num=outer_num, 
                                    snake=snake),
         }
    _md.update(md)

    per_step = per_step or bluesky.plans.one_1d_step

    @bluesky.plans.stage_decorator(list(detectors) + [motor])
    @bluesky.plans.run_decorator(md=_md)
    def inner_scan():
        for projection in projections:
            yield from per_step(detectors, motor, projection)

    return (yield from inner_scan())
