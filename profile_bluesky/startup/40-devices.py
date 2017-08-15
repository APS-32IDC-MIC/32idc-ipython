print(__file__)


# Set up default complex devices

from ophyd import FormattedComponent as FC, Component as Cpt


class SynApps_swait_Variable(Device):
    # inside-out naming!
    inputtrigger = FC(EpicsSignal, '{self.prefix}.IN{self.letter}P', lazy=True)
    inputname    = FC(EpicsSignal, '{self.prefix}.IN{self.letter}N', lazy=True)
    inputvalue   = FC(EpicsSignal, '{self.prefix}.{self.letter}', lazy=True)

    def __init__(self, prefix, letter=None, **kwargs):
        self.letter = letter.upper()
        super().__init__(prefix, **kwargs)


# synApps userCalc (swait record)
class SynApps_UserCalc_Device(Device):
    value = Cpt(EpicsSignalRO, ".VAL")
    process = Cpt(EpicsSignal, ".PROC")
    description = Cpt(EpicsSignal, ".DESC")
    calc = Cpt(EpicsSignal, ".CALC")
    a = FC(SynApps_swait_Variable, "{self.prefix}", lazy=True, letter="a")
    b = FC(SynApps_swait_Variable, "{self.prefix}", lazy=True, letter="b")
    c = FC(SynApps_swait_Variable, "{self.prefix}", lazy=True, letter="c")
    d = FC(SynApps_swait_Variable, "{self.prefix}", lazy=True, letter="d")
    e = FC(SynApps_swait_Variable, "{self.prefix}", lazy=True, letter="e")
    f = FC(SynApps_swait_Variable, "{self.prefix}", lazy=True, letter="f")
    g = FC(SynApps_swait_Variable, "{self.prefix}", lazy=True, letter="g")
    h = FC(SynApps_swait_Variable, "{self.prefix}", lazy=True, letter="h")
    i = FC(SynApps_swait_Variable, "{self.prefix}", lazy=True, letter="i")
    j = FC(SynApps_swait_Variable, "{self.prefix}", lazy=True, letter="j")
    k = FC(SynApps_swait_Variable, "{self.prefix}", lazy=True, letter="k")
    l = FC(SynApps_swait_Variable, "{self.prefix}", lazy=True, letter="l")


# define userCalc1, userCalc2, userCalc3, ... userCalc10
for _ in range(1,10+1):
    nm = "userCalc" + str(_)
    globals()[nm] = SynApps_UserCalc_Device("32idcSIM:"+nm,  name=nm)

if False:       # for example:
    userCalc1.a.inputname.put("32idcSIM:userCalc1")
    userCalc1.b.value.put("100")
    userCalc1.calc.put("(A%B)+1")
    userCalc1.process.put(1)
