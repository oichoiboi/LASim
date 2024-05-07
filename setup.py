from dataclasses import dataclass
import json


class Stats:
    def __init__(self, **kwargs):
        self.STAT_KEYS = [
            "AP",
            "Add",
            "Atkspeed",
            "AwkCDR",
            "AwkMult",
            "Back",
            "CDR_Flat",
            "CDR1",
            "CDR2",
            "CDmg",
            "Charge",
            "ChargeAS",
            "Crit",
            "DefRed",
            "HBCDdmg",
            "HC",
            "HCAS",
            "HM",
            "Head",
            "HeadBack",
            "MCDmg",
            "Main Stat",
            "Movespeed",
            "Mult",
            "SkillCDR",
            "SkillMult",
            "WpnPower",
        ]
        for arg in self.STAT_KEYS:
            setattr(self, arg, kwargs.get(arg, 0))

    def reset_stat(self):
        for attr in self.__dict__:
            setattr(self, attr, 0)

    def copy_stats(self, other):
        for attr in self.__dict__:
            setattr(self, attr, getattr(other, attr))


class Job(Stats):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.skills = []
        self.maxGauge = 0
        self.lvlcoefficient = {key: 0 for key in range(13)}

class Tripod(Stats):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.lvl = kwargs.get('lvl', None)

    def lvl_check(self, lvl):
        if lvl >= self.lvl:
            return True



class BaseSkill(Stats):
    def __init__(self, name=None, level=0, charge=False, holdcast=False,
                 hitmaster=False, backatk=False, headatk=False, basecasttime=0,
                 casttime=0, basecooldown=0, cooldown=0, skillcoeff=0,
                 baseframes=0, tripods=None, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.level = level
        self.charge = charge
        self.holdcast = holdcast
        self.hitmaster = hitmaster
        self.backatk = backatk
        self.headatk = headatk
        self.basecasttime = basecasttime
        self.casttime = casttime
        self.basecooldown = basecooldown
        self.cooldown = cooldown
        self.skillcoeff = skillcoeff
        self.baseframes = baseframes
        self.tripods = [Tripod(**tripod) for tripod in tripods] if tripods else []



class Gear(Stats):
    def __init__(self, type=None, trans_lvl=0, trans_grade=0, honing=0, tier=None, **kwargs):
        super().__init__(**kwargs)
        self.type = type
        self.trans_lvl = trans_lvl
        self.trans_grade = trans_grade
        self.honing = honing
        self.tier = tier

    def get_gear_value(data, tier, level, piece):
        tier_data = data.get(tier, [])
        item = next(
            (item for item in tier_data if item["Level"] == level and piece in item),
            None,
        )
        return item[piece] if item else 0

with open('gunslinger.json', 'r') as json_file:
    gs_skills = json.load(json_file)

print(gs_skills)
skills = {BaseSkill(**skill) for skill in gs_skills}
for skill in skills:
    print(skill.name)
    for tripod in skill.tripods:
        print(tripod.name)



