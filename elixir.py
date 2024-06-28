from stats import Stats
from typing import Dict, Union, List
from enums import GearType
from dataclasses import dataclass
"""
Define an Elixir class, and then instantiate every relevant elixir in the game
"""

@dataclass
class Elixir:
    name: str
    piece: Union[GearType, None]
    mods: Dict[Stats, Dict[int, float]]

    def get_value(self, mod, lvl):
        return self.mods.get(mod, 0).get(lvl, 0)

ELIXIR_OPTIONS = {"Common": [
    'ATTACK_POWER', 'WEAPON_POWER', 'MAIN_STAT', 'STAGGER',
    'MASTER_OF_EVASION', 'ESCAPE_EXPERT', 'EXPLOSIVES_EXPERT',
    'POTION_POISONING', 'MP', 'BLESSING_OF_LIFE', 'RESOURCE_BLESSING',
    'VAGABOND'],
    "Shoulder": ['AWK_SKILL_DMG', 'BOSS_DMG', 'SHIELD_ENHANCE', 'HEALING_ENHANCE'],
    "Chest": ['INCOMING_DMG_RED', 'MAG_DEF', 'PHY_DEF', 'MAX_HP'],
    "Pants": ['ADD_DMG', 'CRIT_DMG', 'SPECIALTY_GAIN', 'ALLY_ENHANCE']
}

flatAP_ELX = Elixir('ATTACK_POWER', GearType.Common, {Stats.FlatAP: {1: 122, 2: 253, 3: 383, 4: 575, 5: 767}})
wpnPwr_ELX = Elixir('WEAPON_POWER', GearType.Common, {Stats.WpnPower: {1: 236, 2: 488, 3: 740, 4: 1110, 5: 1480}})
mainStat_ELX = Elixir('MAIN_STAT', GearType.Common, {Stats.MainStat: {1: 720, 2: 1782, 3: 2700, 4: 4050, 5: 5400}})
awkDmg_ELX = Elixir('AWK_SKILL_DMG', GearType.Shoulder, {Stats.AwkDmg: {1: 0.012, 2: 0.0247, 3: 0.0375, 4: 0.0562, 5: 0.075}})
bossDmg_ELX = Elixir('BOSS_DMG', GearType.Shoulder, {Stats.MultDmg: {1: 0.012, 2: 0.0247, 3: 0.0375, 4: 0.0562, 5: 0.075}})
addDmg_ELX = Elixir('ADD_DMG', GearType.Pants, {Stats.AddDmg: {1: 0.0049, 2: 0.0102, 3: 0.0155, 4: 0.0232, 5: 0.031}})
critDmg_ELX = Elixir('CRIT_DMG', GearType.Pants, {Stats.CritDmg: {1: 0.0112, 2: 0.0231, 3: 0.035, 4: 0.0525, 5: 0.07}})
idenGain_ELX = Elixir('SPECIALTY_GAIN', GearType.Pants, {Stats.IdentityGain: {1: 0.0064, 2: 0.0132, 3: 0.02, 4: 0.03, 5: 0.04}})
apBuff_ELX = Elixir('ALLY_ENHANCE', GearType.Pants, {Stats.APBuff: {1: 0.0096, 2: 0.0198, 3: 0.03, 4: 0.045, 5: 0.06}})
helmet_DPS_ELX = Elixir('HELMET_COMMON', GearType.Helmet, {Stats.MultDmg: {1: 0.0049, 2: 0.0102, 3: 0.0155, 4: 0.0232, 5: 0.031}})
gloves_DPS_ELX = Elixir('HELMET_COMMON', GearType.Gloves, {Stats.AtkPower: {1: 0.0023, 2: 0.0047, 3: 0.0072, 4: 0.0108, 5: 0.0144}})
helmet_SUP_ELX = Elixir('HELMET_COMMON', GearType.Helmet, {Stats.HealShield: {1: 0.0023, 2: 0.0047, 3: 0.0072, 4: 0.00108, 5: 0.0144}})
gloves_SUP_ELX = Elixir('HELMET_COMMON', GearType.Gloves, {Stats.APBuff: {1: 0.0064, 2: 0.0132, 3: 0.02, 4: 0.03, 5: 0.04}})
CRITICAL = Elixir('CRITICAL', None, {Stats.MultCDmg: {1: 0.06, 2: 0.12}})
MASTER = Elixir('MASTER', None, {Stats.CritRate: {1: 0.07, 2: 0.07}, Stats.AddDmg: {1: 0, 2: 0.085}})




"""
Common
'STAGGER': {1: 0.0038, 2: 0.0079, 3: 0.012, 4: 0.018, 5: 0.024}
'MASTER_OF_EVASION': {1: 0.0038, 2: 0.0079, 3: 0.012, 4: 0.018, 5: 0.024}
'MP': {1: 15, 2: 32, 3: 49, 4: 73, 5: 98},
'RESOURCE_BLESSING': {1: 0.0046, 2: 0.0095, 3: 0.0145, 4: 0.0217, 5: 0.029}

CHEST_ELX = {
        'INCOMING_DMG_RED': {1: -0.016, 2: 0.033, 3: 0.05, 4: 0.075, 5: 0.1},
        'MAG_DEF': {1: 960, 2: 1980, 3: 3000, 4: 4500, 5: 6000},
        'PHY_DEF': {1: 960, 2: 1980, 3: 3000, 4: 4500, 5: 6000},
        'MAX_HP': {1: 2720, 2: 5610, 3: 8500, 4: 12750, 5: 17000}
}
"""


HELMET_COMMON = {1: 0.0049, 2: 0.0102, 3: 0.0155, 4: 0.0232, 5: 0.031}
HELMET_SETS = {'DMG': {1: 0.0049, 2: 0.0102, 3: 0.0155, 4: 0.0232, 5: 0.031},
          'BLADED_SHIELD': {1: 0.04, 2: 0.08},
          'CRITICAL': ''






