from dataclasses import dataclass, field
from typing import List
from stats import Stats
from enums import GearTier, GearType

@dataclass
class Gear:
    type: GearType = None
    trans_lvl: int = 0
    trans_grade: int = 0
    honing_lvl: int = 0
    tier: GearTier = GearTier.AKKAN
    
    def get_gear_value(self, data):
        tier_data = data.get(self.tier, [])
        item = next(
            (item for item in tier_data if item["Level"] == self.honing and self.type in item), None)
        stat = 0 if item is None else item[self.type]
        return stat
    
    def set_t_lvl(self, level: int):
        self.trans_lvl = level
    
    def set_t_grade(self, grade: int):
        self.trans_grade = grade
        
    def set_honing_level(self, level: int):
        self.honing_lvl = level
        
    def set_tier(self, tier: GearTier):
        if tier in GearTier:
            self.tier = tier
        else:
            raise TypeError
    

    
@dataclass
class GearManager(Stats):
    gear: List[Gear] = None
    
    def get_honing_stats(self):
        pass
    
    def get_trans_stats(self):
        pass
    
    def trans_level_stats(self, gear):
        pass
    
    def trans_grade_stats(self, gear):
        pass
    
    def weapon_quality(self):
        pass