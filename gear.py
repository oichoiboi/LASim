from dataclasses import dataclass, field
from typing import List, Dict
from enums import GearTier, GearType
import json

#double check how Echidna honing affects Akkan gear
TIER_DATA = {
    GearTier.Relic: {
        'Base': 1250,
        'Per': 15,
        'Max': 20
    },
    GearTier.Brel: {
        'Base': 1390,
        'Per': 5,
        'Max': 25
    },
    GearTier.Akkan: {
        'Base': 1525,
        'Per': 5,
        'Max': 25
    },
    GearTier.T4Relic: {
        'Base': 1590,
        'Per': 5,
        'Max': 20
    },
    GearTier.T4Ancient: {
        'Base': 1590,
        'Per': 5,
        'Max': 25
    }
}

armour_pieces = [GearType.Helmet, GearType.Shoulder, GearType.Chest, GearType.Pants, GearType.Gloves]

with open('mainstat_table.json', 'r') as json_file:
    gear_stats = json.load(json_file)

# with an assumption that GearMgr will handle all error logic, ie setting elixir or transc without proper item level
@dataclass
class Gear:
    piece: GearType
    tier: GearTier = GearTier.Akkan
    honeLvl: int = 0
    advHoneLvl: int = 0

    @staticmethod
    def get_stat(tier: str, level: int, piece: str):
        tier_data = gear_stats.get(tier, [])  # return the nested dict in the selected tier, otherwise return empty list
        item = next(
            (
                item
                for item in tier_data
                if item["Level"] == level and piece in item
            ),
            None,
        )
        return 0 if item is None else item[piece]

    @property
    def mainStat(self):
        if self.piece is not GearType.Weapon:
            return self.get_stat(self.tier.value, self.honeLvl, self.piece.value)
        else:
            return 0

    @property
    def weaponPower(self):
        if self.piece is GearType.Weapon:
            return self.get_stat(self.tier.value, self.honeLvl, self.piece.value)
        else:
            return 0

    @property
    def advhoneStat(self):
        return self.get_stat("Echidna", self.advHoneLvl, self.piece.value)

    @property
    def itemLvl(self):
        tier = TIER_DATA[self.tier]
        base, per = tier['Base'], tier['Per']  # user shouldn't be able to select honeLvl higher than max in GUI
        return base + self.honeLvl * per


class GearMgr:
    def __init__(self):
        self.gear = {piece: Gear(piece, GearTier.Akkan, 0, 0) for piece in GearType}

    @property
    def baseitemLvl(self):
        return sum(piece.itemLvl for piece in self.gear.values())

    @property
    def advHoneLvl(self):
        return sum(piece.advHoneLvl for piece in self.gear.values())

    @property
    def itemLvl(self):
        if self.baseitemLvl >= 1620:
            return (self.baseitemLvl + self.advHoneLvl) / 6
        return self.baseitemLvl / 6

    @property
    def mainstat(self):
        return sum(piece.mainStat for piece in self.gear.values())

    @property
    def wpnPower(self):
        return sum(piece.weaponPower for piece in self.gear.values())

    def set_honeLvl(self, piece: GearType, level: int):
        self.gear[piece].honeLvl = min(TIER_DATA[self.gear[piece].tier]['Max'], level)

    def set_tier(self, piece: GearType, tier: GearTier):
        self.gear[piece].tier = tier
        self.set_honeLvl(piece, self.gear[piece].honeLvl)

    def set_advitemLvl(self, piece: GearType, level: int):
        if self.itemLvl > 1630:
            self.gear[piece].advHoneLvl = min(level, 20)
        elif self.itemLvl > 1620:
            self.gear[piece].advHoneLvl = min(level, 10)



test = GearMgr()
for gear in test.gear:
    print(gear.piece)





