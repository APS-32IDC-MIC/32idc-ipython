print(__file__)

"""Set up default complex devices"""

from ophyd import Component, Device, DeviceStatus
from ophyd import EpicsMotor, EpicsScaler
from ophyd import EpicsSignal, EpicsSignalRO, EpicsSignalWithRBV
from ophyd import PVPositioner, PVPositionerPC
from APS_BlueSky_tools.devices import userCalcsDevice

class MotorDialValues(Device):
    value = Component(EpicsSignalRO, ".DRBV")
    setpoint = Component(EpicsSignal, ".DVAL")

class MyEpicsMotorWithDial(EpicsMotor):
    dial = Component(MotorDialValues, "")
