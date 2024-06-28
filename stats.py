"""
Enumerate stats in Lost Ark and maybe add methods for collecting them easily
"""

from enum import Enum, auto


class Stats(Enum):
    # AP stats
    AtkPower = auto()
    WpnPower = auto()
    MainStat = auto()
    FlatAP = auto()
    # Damage related stats
    AddDmg = auto()
    MultDmg = auto()
    SkillDmg = auto()
    AwkDmg = auto()
    # positional specific multipliers
    BackAtkDmg = auto()
    FrontAtkDmg = auto()
    HeadBackDmg = auto()
    NonPosDmg = auto()
    # Crit stats
    CritRate = auto()
    CritDmg = auto()
    MultCDmg = auto()
    FrontAtkCDmg = auto()
    BackAtkCDmg = auto()
    # Casting speed related
    AtkSpeed = auto()
    ChargeSpeed = auto()
    CastSpeed = auto()
    MoveSpeed = auto()
    DefRed = auto()
    # CDR stats
    CDR1 = auto()
    CDR2 = auto()
    SkillCDR = auto()
    AwkCDR = auto()
    # Conditionals
    ChargeDmg = auto()
    CastDmg = auto()
    # Other
    Stagger = auto()
    IdentityGain = auto()
    APBuff = auto()
    HealShield = auto()









