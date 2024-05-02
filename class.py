from lookupvalues import *


class BaseClass:
    def __init__(self, name):
        self.name = name
        self.mainstat = 0
        self.weaponpower = 0
        self.set = ''
        self.gear = []
        self.skills = []
        

class Skill:
    def __init__(self):
        self.stacks = 0
        self.cooldown = 0
        self.casttime = 0
        

class Gear:
    def __init__(self, type=HELMET, trans_level=0, trans_grade=0, honing=0, tier='Relic', df=STATLUT):
        self.type = type
        self.trans_level = trans_level
        self.trans_grade = trans_grade
        self.honing = honing
        self.tier = tier
        self.df = df
        self.df.set_index(['Tier', 'Level'], inplace=True)
        self.stat = self.df.loc[(self.tier, self.honing), self.type]

