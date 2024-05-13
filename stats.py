from dataclasses import dataclass, field
from typing import List

DEFAULT_0 = [
    "AP",
    "Add",
    "Atkspeed",
    "AwkCDR",
    "CDR_Flat",
    "CDR1",
    "CDR2",
    "CDmg",
    "ChargeAS",
    "Crit",
    "DefRed",
    "HBCDdmg",
    "HCAS",
    "MCDmg",
    "MainStat",
    "Movespeed",
    "SkillCDR",
    "WpnPower",
]
DEFAULT_1 = [
    "AwkMult",
    "Back",
    "Charge",
    "Exec",
    "HC",
    "HM",
    "Head",
    "HeadBack",
    "Mult",
    "SkillMult",
]


@dataclass
class Stats:
    AP: float = field(default=0, init=False)
    Add: float = field(default=0, init=False) 
    Atkspeed: float = field(default=0, init=False) 
    AwkCDR: float = field(default=0, init=False) 
    CDR_Flat: float = field(default=0, init=False) 
    CDR1: float = field(default=0, init=False) 
    CDR2: float = field(default=0, init=False) 
    CDmg: float = field(default=0, init=False) 
    ChargeAS: float = field(default=0, init=False) 
    Crit: float = field(default=0, init=False) 
    DefRed: float = field(default=0, init=False) 
    HBCDdmg: float = field(default=0, init=False) 
    HCAS: float = field(default=0, init=False) 
    MCDmg: float = field(default=0, init=False) 
    MainStat: float = field(default=0, init=False) 
    Movespeed: float = field(default=0, init=False) 
    SkillCDR: float = field(default=0, init=False) 
    WpnPower: float = field(default=0, init=False) 
    AwkMult: float = field(default=0, init=False) 
    Back: float = field(default=0, init=False) 
    Charge: float = field(default=0, init=False) 
    Exec: float = field(default=0, init=False) 
    HC: float = field(default=0, init=False) 
    HM: float = field(default=0, init=False) 
    Head: float = field(default=0, init=False) 
    HeadBack: float = field(default=0, init=False) 
    Mult: float = field(default=0, init=False) 
    SkillMult: float = field(default=0, init=False) 

    def reset(self):
        for attr in self.__dict__:
            setattr(self, attr, 0)
