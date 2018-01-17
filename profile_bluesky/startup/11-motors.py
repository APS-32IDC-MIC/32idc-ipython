print(__file__)

"""motors, stages, positioners, ..."""


gamma = EpicsMotor('32idc01:m31', name='gamma')
append_wa_motor_list(gamma)
