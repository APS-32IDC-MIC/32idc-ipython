print(__file__)

from ophyd import (PVPositioner, EpicsMotor, EpicsSignal, EpicsSignalRO,
                   PVPositionerPC, Device)
from ophyd import Component as Cpt

# from 32idcSIM sim detector IOC

# define m1, m2, m3, ... m16
for _ in range(1,16+1):
    nm = "m" + str(_)
    globals()[nm] = EpicsMotor("32idcSIM:"+nm,  name=nm)


#gamma = EpicsMotor('32idc01:m31', name='gamma')
