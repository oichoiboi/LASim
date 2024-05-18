from dataclasses import dataclass, field
from typing import List
from stats import Stats
from enums import GearTier, GearType
from abc import ABC, abstractmethod

class Gear:
    def __init__(self, type, transcLvl, transcGrade, honeLvl, tier):
        self.type = type
        self.tier = tier
        self.transcLvl = transcLvl
        self.transcGrade = transcGrade
        self.honeLvl = honeLvl
    
    def set_transcLvl(self, level: int):
        if self.tier != GearType.Akkan:
            pass
        else:
            self.transcLvl = level
        
    def set_honeLvl(self, level: int):
        if self.tier == GearTier.RELIC and level <=20:
            self.honeLvl = level
        elif (self.tier == GearTier.BREL or self.tier == GearTier.AKKAN) and level <= 25:
            self.honeLvl = level



    def set_tier(self, tier: GearTier):
        if tier in GearTier:
            self.tier = tier.value
        else:
            raise TypeError
        self.get_gearStat()
        
    def set_transcGrade(self, grade: int):
        self.transcGrade = grade


class GearMgr:
    def __init__(self):
        self._helmet = Gear(GearType.HELMET, 0, 0, 0, GearTier.AKKAN)

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
