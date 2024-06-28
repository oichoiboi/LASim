from dataclasses import dataclass, field
from typing import List, Dict, Union
from stats import Stats
from enums import GearTier, GearType
from abc import ABC, abstractmethod
import json
from typing import Optional

LVL_WPN_BONUS = {1: 300,
                 2: 340,
                 3: 380,
                 4: 420,
                 5: 460,
                 6: 500,
                 7: 540}

LVL_ARMOUR_BONUS = {1: 600,
                    2: 680,
                    3: 760,
                    4: 840,
                    5: 920,
                    6: 1000,
                    7: 1080}


@dataclass
class TranscendenceMgr:
    levels: Dict[GearType, int] = field(init=False)
    grade: Dict[GearType, int] = field(init=False)

    def __post_init__(self):
        self.levels = {piece: 0 for piece in GearType}
        self.grade = {piece: 0 for piece in GearType}

    def set_level(self, piece, lvl):
        self.levels[piece] = min(7, lvl)

    def set_grade(self, piece, grade):
        self.levels[piece] = min(self.levels[piece]*3, grade)

    def levelMainStat(self):
        return sum(LVL_ARMOUR_BONUS[level] for piece, level in self.levels.values() if piece is not GearType.Weapon)

    def levelWpnPwr(self):
        return sum(LVL_WPN_BONUS[level] for piece, level in self.levels.values() if piece is GearType.Weapon)

    @property
    def totalGrade(self):
        return sum(self.grade.values())

    def stats_flat(self, piece: GearType, grades: List[int], values: List[float]):
        if len(grades) != len(values):
            return 0
        return sum(values[i] for i in range(len(grades)) if self.grade[piece] >= grades[i])

    def stats_scale(self, piece: GearType, grades: Union[int, List[int]], value: float):
        if isinstance(grades, int):
            return value * self.totalGrade if self.grade[piece] >= grades else 0
        elif isinstance(grades, list):
            return sum(value * self.totalGrade for i in range(len(grades)) if self.grade[piece] >= grades[i])

    @property
    def mainStat(self):
        helmet = self.stats_scale(GearType.Helmet, 10, 55)
        gloves = self.stats_flat(GearType.Gloves, [5, 15, 20], [4200, 4200, 4200])
        levels = self.levelMainStat()
        return helmet + gloves + levels

    @property
    def wpnPower(self):
        helmet = self.stats_scale(GearType.Helmet, 15, 14)
        shoulder = self.stats_flat(GearType.Shoulder, [5, 15, 20], [1200, 1200, 1200])
        chest = self.stats_flat(GearType.Chest, [5, 15, 20], [2000, 2000, 3200])
        levels = self.levelWpnPwr()
        return helmet + shoulder + chest + levels

    @property
    def flatAP(self):
        helmet = self.stats_scale(GearType.Helmet, 20, 6)
        weapon = self.stats_flat(GearType.Weapon, [5, 10, 15, 20], [800, 800, 800, 1125])
        return helmet + weapon

    @property
    def buff_AP(self):
        helmet = self.stats_scale(GearType.Helmet, [5, 10, 15, 20], 0.0001)
        shoulder = self.stats_scale(GearType.Shoulder, [5, 15, 20], 0.01)
        gloves = self.stats_scale(GearType.Gloves, [5, 15, 20], 0.01)
        pants = self.stats_flat(GearType.Pants, [10, 15, 20], [0.015, 0.015, 0.03])
        return helmet + shoulder + gloves + pants

    @property
    def intimidation(self):
        # 1.5% damage to enemies
        if self.grade[GearType.Pants] >= 20:
            return True
        return False

    @property
    def successor(self):
        if self.grade[GearType.Pants] >= 15:
            return 1.4e7
        elif self.grade[GearType.Pants] >= 10:
            return 7e7
        return 0

    @property
    def brand_power(self):
        return self.stats_flat(GearType.Weapon, [5, 10, 15, 20], [0.02, 0.02, 0.02, 0.04])


