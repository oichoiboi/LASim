from dataclasses import dataclass, field
from typing import List
from stats import Stats
from enums import GearTier, GearType
from abc import ABC, abstractmethod

#double check how Echidna honing affects Akkan gear
MAX_HONING_LEVEL: {
    GearType.RELIC: 20,
    GearType.BREL: 25,
    GearType.AKKAN: 25
}

class Gear:
    def __init__(self, type, transcLvl, transcGrade, honeLvl, tier):
        self.type = type
        self.tier = tier
        self.set_transcLvl(transcLvl)
        self.transcLvl = transcLvl
        self.transcGrade = transcGrade
        self.honeLvl = honeLvl
    
    def set_transcLvl(self, level: int):
        if self.tier == GearType.AKKAN:
            self.transcLvl = level
        else:
            self.transcLvl = 0
        
    def set_honeLvl(self, level: int):
        if level <= MAX_HONING_LEVEL.get(self.tier):
            self.honeLvl = level
        else:
            self.honeLvl = 0

    def set_tier(self, tier: GearTier):
        self.tier = tier

    def set_transcGrade(self, grade: int):
        if self.tier == GearTier.AKKAN:
            self.transcGrade = grade
        else:
            self.transcGrade = 0


class GearMgr:
    def __init__(self):
        self._helmet = Gear(GearType.HELMET, 0, 0, 0, GearTier.AKKAN)
        self._shoulders = Gear(GearType.SHOULDER, 0, 0, 0, GearTier.AKKAN)
        self._chest = Gear(GearType.CHEST, 0, 0, 0, GearTier.AKKAN)
        self._pants = Gear(GearType.PANTS, 0, 0, 0, GearTier.AKKAN)
        self._gloves = Gear(GearType.GLOVES, 0, 0, 0, GearTier.AKKAN)
        self._weapon = Gear(GearType.WEAPON, 0, 0, 0, GearTier.AKKAN)

    def get_gearStat(self, data):
        tier_data = data.get(self.tier.value, [])
        item = next(
            (
                item
                for item in tier_data
                if item["Level"] == self.honeLvl and self.type.value in item
            ),
            None,
        )
        self.honeStat = 0 if item is None else item[self.type]
