from stats import Stats
from enums import Activation, Direction
from dataclasses import dataclass, field
from typing import Dict, List, Union

    
@dataclass
class Tripod(Stats):
    name: str = ""
    min_skill_lvl: int = 1
    level: int = field(default=0, init=False)
    max_level: int = field(default=5)
    stat_dict: Dict[str, Union[List[float], float]] = field(default_factory=dict)
        
    def update_stats(self):
        for key, value in self.stat_dict.items():
            if isinstance(value, list):
                setattr(self, key, value[self.level - 1])
            else:
                setattr(self, key, value)
        
    def change_level(self, level):
        self.level = min(5, level)
        self.update_stats()
    
    def min_skill_lvl(self, level):
        return False if level < self.min_skill_lvl else True
        

@dataclass
class Skill():
    name: str = ""
    skillCoeff: int = 0
    level: int = field(default=0, init=False)
    direction: Direction = Direction.NONPOSITIONAL
    cooldown: float = 0
    frames: float = 0
    tripods: List[Tripod] = field(default_factory=list)
    def __post_init__(self):
        self.tripods = [Tripod(**tripod) for tripod in self.tripods]

'''
@dataclass
class Gear():
    def __init__(
        self, type=None, trans_lvl=0, trans_grade=0, honing=0, tier=None, data=None, **kwargs
    ):
        self.type = type
        self.trans_lvl = trans_lvl
        self.trans_grade = trans_grade
        self.honing = honing
        self.tier = tier
        self.data = data
        self.WpnPower = 

    def get_gear_value(self):
        tier_data = self.data.get(self.tier, [])
        item = next(
            (item for item in tier_data if item["Level"] == self.honing and self.type in item), None)
        stat = 0 if item is None else item[self.type]
        if self.type == "Weapon":
            self.WpnPower = stat
        else:
            self.MainStat = stat
'''