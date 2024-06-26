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
    def get_stat(tier, level, piece):
        tier_data = gear_stats.get(tier, []) # return the nested dictionary in the selected tier, otherwise return empty list
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
    def honeStat(self):
        return self.get_stat(self.tier.value, self.honeLvl, self.piece.value)
    @property
    def advhoneStat(self):
        return self.get_stat("Echidna", self.advHoneLvl, self.piece.value)

    @property
    def itemLvl(self):
        tier = TIER_DATA[self.tier]
        base, per = tier['Base'], tier['Per'] # user shouldn't be able to select honeLvl higher than max in GUI
        return base + self.honeLvl * per


class GearMgr:
    def __init__(self):
        self.gear = {}
        for piece in GearType:
            self.gear[piece] = (Gear(piece, GearTier.Akkan, 0, 0))

    @property
    def baseitemLvl(self):
        return sum(piece.itemLvl for piece in self.gear.values())/6

    @property
    def advHoneLvl(self):
        return sum(piece.advHoneLvl for piece in self.gear.values())

    @property
    def itemLvl(self):
        if self.baseitemLvl >= 1620:
            return self.baseitemLvl + self.advHoneLvl
        return self.baseitemLvl

    def get_gearStat(self):
        pass
        # return flatAP, stat, wpnpower

    @property
    def mainstat(self):
        pass

    @property
    def wpnPower(self):
        pass

    def set_honeLvl(self, piece: GearType, level: int):
        if TIER_DATA[self.gear[piece].tier]['Max'] <= level:
            self.gear[piece].honeLvl = level

    def set_tier(self, piece: GearType, tier: GearTier):
        self.gear[piece].tier = tier
        if TIER_DATA[self.gear[piece].tier]['Max'] <= self.gear[piece].honeLvl:
            self.gear[piece].honeLvl = TIER_DATA[self.gear[piece].tier]['Max']

    def set_advitemLvl(self, piece: GearType, level: int):
        if TIER_DATA[self.gear[piece].tier]['Max'] <= level:
            self.gear[piece].advHoneLvl = level






test = GearMgr()
for gear in test.gear:
    print(gear.piece)





