from lookupvalues import *
import json
from setup import *


class Stats:
    def __init__(self, **kwargs):
        for arg in STAT_KEYS_ADD:
            setattr(self, arg, kwargs.get(arg, 0))
        for arg in STAT_KEYS_MULT:
            setattr(self, arg, kwargs.get(arg, 1))

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
        self.name = kwargs.get("name", None)
        self.req_lvl = kwargs.get("req_lvl", None)

    def lvl_check(self, lvl):
        if lvl >= self.req_lvl:
            return True


class BaseSkill(Stats):
    def __init__(
        self,
        name=None,
        level=0,
        charge=False,
        holdcast=False,
        hitmaster=False,
        backatk=False,
        headatk=False,
        basecasttime=0,
        casttime=0,
        basecooldown=0,
        cooldown=0,
        skillcoeff=0,
        baseframes=0,
        tripods=None,
        **kwargs
    ):
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
    def __init__(
        self, type=None, trans_lvl=0, trans_grade=0, honing=0, tier=None, data=None, **kwargs
    ):
        super().__init__(**kwargs)
        self.type = type
        self.trans_lvl = trans_lvl
        self.trans_grade = trans_grade
        self.honing = honing
        self.tier = tier
        self.data = data

    def get_gear_value(self):
        tier_data = self.data.get(self.tier, [])
        item = next(
            (item for item in tier_data if item["Level"] == self.honing and self.type in item), None)
        stat = 0 if item is None else item[self.type]
        if self.type == "Weapon":
            self.WpnPower = stat
        else:
            self.MainStat = stat

