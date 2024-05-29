from dataclasses import dataclass, field
from typing import List
from stats import Stats
from enums import GearTier, GearType
from abc import ABC, abstractmethod
import json
from typing import Optional

#double check how Echidna honing affects Akkan gear
MAX_HONING_LEVEL = {
    GearTier.Relic: 20,
    GearTier.Brel: 25,
    GearTier.Akkan: 25
}

TRANSC_LVL_WPN_BONUS = {1: 300,
                   2: 340,
                   3: 380,
                   4: 420,
                   5: 460,
                   6: 500,
                   7: 540}

TRANSC_LVL_ARMOUR_BONUS = {1: 600,
                   2: 680,
                   3: 760,
                   4: 840,
                   5: 920,
                   6: 1000,
                   7: 1080}



with open('mainstat_table.json', 'r') as json_file:
    gear_stats = json.load(json_file)


#with an assumption that GearMgr will handle all error logic, ie setting elixir or transc without proper item level
@dataclass
class Gear(ABC):
    piece: GearType
    tier: GearTier = GearTier.Akkan
    honeLvl: int = 0
    transcLvl: int = 0
    transcGrade: int = 0
    advHoneLvl = 0

    @property
    def honeStat(self):
        tier_data = gear_stats.get(self.tier.value, [])
        item = next(
            (
                item
                for item in tier_data
                if item["Level"] == self.honeLvl and self.piece.value in item
            ),
            None,
        )
        return 0 if item is None else item[self.piece.value]
    
    def transcLvlBonus(self, transcSys: bool):
        if transcSys:
            if self.piece is GearType.Weapon:
                return TRANSC_LVL_WPN_BONUS.get(self.transcLvl, 0)
            else:
                return TRANSC_LVL_ARMOUR_BONUS.get(self.transcLvl, 0)
        return 0

    def advHoneStat(self, advSys: bool):
        if advSys:
            tier_data = gear_stats.get("Echidna", [])
            item = next(
                (
                    item
                    for item in tier_data
                    if item["Level"] == self.advHoneLvl and self.piece.value in item
                ),
                None,
            )
            return 0 if item is None else item[self.piece.value]
        return 0
        
    @abstractmethod
    def mainStat(self, transcSys: bool, totalGrade: int, advSys: bool):
        pass

    @abstractmethod
    def wpnPower(self, transcSys: bool, totalGrade: int, advSys: bool):
        pass
    
    @abstractmethod
    def flatAP(self, transcSys: bool, totalGrade: int, advSys: bool):
        pass

    @abstractmethod
    def mult(self, transcSys, advSys):
        pass


@dataclass
class Armour(Gear):

    def mainStat(self, transcSys: bool, totalGrade: int, advSys: bool):
        stat = self.honeStat + self.transcLvlBonus(transcSys) + self.advHoneStat(advSys)
        if transcSys:
            match self.piece:
                case GearType.Helmet:
                    stat += (55 * totalGrade if self.transcGrade >= 10 else 0)
                case GearType.Gloves:
                    if self.transcGrade >= 5:
                        stat += 4200
                    if self.transcGrade >= 15:
                        stat += 4200
                    if self.transcGrade >= 20:
                        stat += 4200
        return stat
            
    def wpnPower(self, transcSys: bool, totalGrade: int, advSys: bool):
        stat = 0
        if transcSys:
            match self.piece:
                case GearType.Helmet:
                    stat += (14 * totalGrade if self.transcGrade >= 15 else 0)
                case GearType.Shoulder:
                    if self.transcGrade >= 5:
                        stat += 1200
                    if self.transcGrade >= 15:
                        stat += 1200
                    if self.transcGrade >= 20:
                        stat += 1200
                case GearType.Chest:
                    if self.transcGrade >= 20:
                        stat += 7200
                    elif self.transcGrade >= 15:
                        stat += 4320
                    elif self.transcGrade >= 5:
                        stat += 1600
        return stat
            
    def flatAP(self, transcSys: bool, totalGrade: int, advSys: bool):
        stat = 0
        if transcSys:
            match self.piece:
                case GearType.Helmet:
                    stat += (14 * totalGrade if self.transcGrade >= 15 else 0)
                case GearType.Shoulder:
                    if self.transcGrade >= 5:
                        stat += 1200
                    if self.transcGrade >= 15:
                        stat += 1200
                    if self.transcGrade >= 20:
                        stat += 1200
                case GearType.Chest:
                    if self.transcGrade >= 20:
                        stat += 7200
                    elif self.transcGrade >= 15:
                        stat += 4320
                    elif self.transcGrade >= 5:
                        stat += 1600
        return stat

    def mult(self, transcSys: bool, advSys: bool):
        pass

    
        


    

    



class GearMgr:
    '''
    Only call methods to aggregate stats if progression systems are true
    Simply need to call individual gear stat methods depending on progression systems
    Transc and Elixir bonuses can return an array/dict/tuple that gets added to the normal stats
    
    Create setter functions with logic around progression systems
    Change self.gear to dict
    '''
    def __init__(self):
        self.gear = []
        '''
        for gear in GearType:
            self.gear.append(Gear(gear, GearTier.Akkan, 0, 0, 0))
            '''
        self.elixirSys = False
        self.transcSys = False
        self.advHoneSys = False
        
    @property
    def elixirPts(self):
        pass
    
    @property
    def totalGrade(self):
        return sum(gear.transcGrade) for gear in self.gear
    
    @property
    def baseItemLvl(self):
        return sum(gear.itemLvl) for gear in self.gear
    
    @property
    def advHoneLvl(self):
        return sum(gear.advHoneLvl) for gear in self.gear
    
    @property
    def totalItemLvl(self):
        if self.baseItemLvl >= 1620:
            return self.baseItemLvl + self.advHoneLvl
        return self.baseItemLvl

    def get_gearStat(self):
        pass
        #return flatAP, stat, wpnpower
            


test = GearMgr()
for gear in test.gear:
    print(gear.piece)