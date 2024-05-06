from dataclasses import dataclass

class Stats:
    def __init__(self):
        self.STAT_KEYS = ['AP', 'Add', 'Atkspeed', 'AwkCDR', 'AwkMult', 'Back', 'CDR1', 'CDR2', 'CDmg', 
             'Charge', 'ChargeAS', 'Crit', 'DefRed', 'HBCDdmg', 'HC', 'HCAS', 'HM', 'Head', 
             'HeaBack', 'MCDmg', 'Main Stat', 'Movespeed', 'SkillCDR', 'SkillMult', 'WpnPower']
        for arg in self.STAT_KEYS:
            setattr(setattr, arg, 0)

    def reset_stat(self):
        for attr in self.__dict__:
            setattr(self, attr, 0)

    def copy_stats(self, other):
        for attr in self.__dict__:
            setattr(self, attr, getattr(other, attr))



class Job():
    def __init__(self):
        self.stats = Stats()
        self.skills = []
        self.maxGauge = 0
        self.lvlcoefficient = {key: 0 for key in range(13)}

@dataclass
class Tripod():
    stats: Stats
    name: str = None
    lvl: int = 0

    def lvl_check(lvl):
        if lvl >=lvl:
            return True

@dataclass
class BaseSkill():
    stats: Stats
    charge: bool = False
    holdcast: bool = False
    hitmaster: bool = False
    backatk: bool = False
    headatk: bool = False
    basecooldown: int = 0
    cooldown: int = 0
    basecasttime: int = 0
    casttime: int = 0

        

@dataclass
class Gear():
    stats: Stats
    type: str = None
    trans_lvl: int = 0
    trans_grade: int = 0
    honing: int = 0
    tier: str = None
    
    def get_gear_value(data, tier, level, piece):
        tier_data = data.get(tier, [])
        item = next((item for item in tier_data if item['Level'] == level and piece in item), None)
        return item[piece] if item else 0
    
 





    


       


