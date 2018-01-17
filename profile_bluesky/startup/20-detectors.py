print(__file__)

"""various detectors and other signals"""

aps_current = EpicsSignal("S:SRcurrentAI", name="aps_current")
userCalcs_32idc01 = userCalcsDevice("32idc01:", name="userCalcs_32idc01")
