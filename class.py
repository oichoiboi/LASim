from lookupvalues import *


class Stats:
    STAT_KEYS = ['AP', 'Add', 'Atkspeed', 'AwkCDR', 'AwkMult', 'Back', 'CDR1', 'CDR2', 'CDmg', 
             'Charge', 'ChargeAS', 'Crit', 'DefRed', 'HBCDdmg', 'HC', 'HCAS', 'HM', 'Head', 
             'HeadBack', 'MCDmg', 'Main Stat', 'Movespeed', 'SkillCDR', 'SkillMult', 'WpnPower']
    
    def __init__(self):
        for arg in STAT_KEYS:
            setattr(self, arg, 0)

    def reset_stats(self):
        for attr in self.__dict__:
            setattr(self, attr, 0)

class Job():
    def __init__(self, name):
        self.name = name
        self.stats = Stats()
        self.skills = []
   
class Skill():
    def __init__(self):
        self.stats = Stats()
        self.cooldown = 0
        self.casttime = 0


class Gear():
    def __init__(self, type=None, trans_level=0, trans_grade=0, honing=0, tier=None):
        self.stats = Stats()
        self.type = type
        self.trans_level = trans_level
        self.trans_grade = trans_grade
        self.honing = honing
        self.tier = tier


class Simulator(Stats):
    def __init__(self) -> None:
        pass

       


