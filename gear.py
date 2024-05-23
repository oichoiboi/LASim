from dataclasses import dataclass, field, classVar
from typing import List
from stats import Stats
from enums import GearTier, GearType
from abc import ABC, abstractmethod
import json
from typing import Optional

#double check how Echidna honing affects Akkan gear
MAX_HONING_LEVEL: {
    GearTier.Relic: 20,
    GearTier.Brel: 25,
    GearTier.Akkan: 25
}

#grab real values later
TRANSC_LVL_BONUS: {1:580,
2: 680,
3: 700}

with open('mainstat_table.json', 'r') as json_file:
    gear_stats = json.load(json_file)


#with an assumption that GearMgr will handle all error logic, ie setting elixir or transc without proper item level
@dataclass
class Gear(ABC):
    piece: GearType
    tier: GearTier = GearTier.Akkan
    honeLvl: int = 0
    elixirA: str = ""
    elixirB: str = ""
    transcLvl: int = 0
    transcGrade: int = 0
    advHoneLvl = 0

    def honeStat(self, advHoneSys):
        tier_data = gear_stats.get(piece.tier.value, [])
        item = next(
            (
                item
                for item in tier_data
                if item["Level"] == piece.honeLvl and piece.value in item
            ),
            None,
        )
        stat = 0 if item is None else item[piece.value]

        #if advHoneSys is true...do the same for Echidna honing
        return stat

    @property 
    @abstractmethod
    def mainStat(self):
        pass

    @property
    @abstractmethod
    def wpnPower(self):
        pass

    @property
    @abstractmethod
    def flatAP(self):
        pass

    @property
    @abstractmethod
    def mult(self):
        pass

    def set_elixir(self, elixirA, elixirB):
        self.elixirA = elixirA
        self.elixirB = elixirB
    
    def get_transcLvl_bonus(self):
        stat = TRANSC_LVL_BONUS.get(self.transcLvl)
        return stat

    @abstractmethod
    def get_transcGrade_bonus(self):
        pass
    
    

    
        


    

    



class GearMgr:
    def __init__(self):
        self.gear = []
        for gear in GearType:
            self.gear.append(Gear(gear, GearTier.Akkan, 0, 0, 0))
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
        else:
            return self.baseItemLvl

    def get_gearStat(self):
        pass
        #return flatAP, stat, wpnpower
            


test = GearMgr()
for gear in test.gear:
    print(gear.piece)