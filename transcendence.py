from dataclasses import dataclass, field
from typing import List, Dict
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
class GearTransc:
    name: GearType
    level: int = field(default=0)
    grade: int = field(default=0)

@dataclass
class TranscendenceMgr:
    gear: List[GearTransc] = field(init=False)

    def __post_init__(self):
        self.gear = [GearTransc(piece, 0, 0) for piece in GearType]

    def levelMainStat(self):
        return sum(LVL_ARMOUR_BONUS[piece.level] for piece in self.gear if piece.name is not GearType.Weapon)

    def levelWpnPwr(self):
        return sum(LVL_WPN_BONUS[piece.level] for piece in self.gear if piece.name is GearType.Weapon)

    @property
    def totalGrade(self):
        return sum(piece.grade for piece in self.gear)

    def mainStat(self):
        stat = 0
        for piece in self.gear:
            match piece.name:
                case GearType.Helmet:
                    stat += (55 * self.totalGrade if piece.grade >= 10 else 0)
                case GearType.Gloves:
                    if piece.grade >= 5:
                        stat += 4200
                    if piece.grade >= 15:
                        stat += 4200
                    if piece.grade >= 20:
                        stat += 4200
        return stat

    def wpnPower(self):
        stat = 0
        for piece in self.gear:
            match piece.name:
                case GearType.Helmet:
                    stat += (14 * self.totalGrade if piece.grade >= 15 else 0)
                case GearType.Shoulder:
                    if piece.grade >= 5:
                        stat += 1200
                    if piece.grade >= 15:
                        stat += 1200
                    if piece.grade >= 20:
                        stat += 1200
                case GearType.Chest:
                    if piece.grade >= 20:
                        stat += 3200
                    if piece.grade >= 15:
                        stat += 2000
                    if piece.grade >= 5:
                        stat += 2000
        return stat

    def flatAP(self):
        stat = 0
        for piece in self.gear:
            match piece.name:
                case GearType.Helmet:
                    stat += (6 * self.totalGrade if piece.grade >= 20 else 0)
                case GearType.Weapon:
                    if piece.grade >= 5:
                        stat += 800
                    if piece.grade >= 10:
                        stat += 800
                    if piece.grade >= 15:
                        stat += 800
                    if piece.grade >= 20:
                        stat += 1125
        return stat

    @property
    def intimidation(self):
        if self.gear[4].grade >= 20:
            return True
        else:
            return False

    @property
    def successor(self):
        if self.gear[4].grade >= 15:
            return 2
        elif self.gear[4].grade >= 10:
            return 1

