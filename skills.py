from stats import Stats
from enums import Activation, Position, Rune, GearType, Rarity
from dataclasses import dataclass, field
from typing import Dict, List, Union


# RUNE CONSTANTS

GALEWIND = {Rarity.COMMON: 0.8, Rarity.RARE: 0.10, Rarity.EPIC: 0.12, Rarity.LEGENDARY: 0.14}
OVERWHELM = {Rarity.COMMON: 7, Rarity.RARE: 9, Rarity.EPIC: 12, Rarity.LEGENDARY: 15}
    
#GEM CONSTANTS

@dataclass
class Tripod(Stats):
    name: str = ""
    min_skill_lvl: int = 1
    level: int = field(default=0, init=False)
    max_level: int = field(default=5)
    position: Position = None
    activation: Activation = None
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
class Skill:
    '''
    Represents a skill. Has original skill information and tripod information.
    
    '''
    name: str = ""
    skillCoeff: int = 0
    level: int = field(default=0, init=False)
    position: Position = Position.NONPOSITIONAL
    activation: Activation = Activation.NORMAL
    basecooldown: float = 0
    baseframes: float = 0
    tripods: List[Tripod] = field(default_factory=list)
    #img: Image()
    #
    
    def __post_init__(self):
        self.tripods = [Tripod(**tripod) for tripod in self.tripods]
        self.position = Position(self.position)
        self.activation = Activation(self.activation)
    
    @property
    def skill_output(self, atkpower, modifier, crit, cdmg, mcdmg, ):
        '''
        param: modifiers (AP, overall multiplier, crit, cdmg, attack speed, etc)
        return: tuple with skill average damage, skill cooldown, skill cast time, gauge generated
        '''
        pass

    def select_tripod(self, name):
        '''
        param: name of the tripod to be selected
        '''
    
    
