from stats import Stats
from typing import Dict, Union
from dataclasses import dataclass, field
import enum


"""
Define an Elixir class, and then instantiate every relevant elixir in the game

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


class ElixirType(enum.Enum):
    Helmet = "Helmet"
    Shoulder = "Shoulder"
    Chest = "Chest"
    Pants = "Pants"
    Gloves = "Gloves"
    Common = "Common"
    Set = "Set"


# COMMON
ATTACK_POWER = ('ATTACK_POWER', ElixirType.Common, {Stats.FlatAP: {1: 122, 2: 253, 3: 383, 4: 575, 5: 767}})
WEAPON_POWER = ('WEAPON_POWER', ElixirType.Common, {Stats.WpnPower: {1: 236, 2: 488, 3: 740, 4: 1110, 5: 1480}})
MAIN_STAT = ('MAIN_STAT', ElixirType.Common, {Stats.MainStat: {1: 720, 2: 1782, 3: 2700, 4: 4050, 5: 5400}})
COMMON_ELX = {ATTACK_POWER, WEAPON_POWER, MAIN_STAT}

# SHOULDER
AWK_SKILL_DMG = ('AWK_SKILL_DMG', ElixirType.Shoulder, {Stats.AwkDmg: {1: 0.012, 2: 0.0247, 3: 0.0375, 4: 0.0562, 5: 0.075}})
BOSS_DMG = ('BOSS_DMG', ElixirType.Shoulder, {Stats.MultDmg: {1: 0.012, 2: 0.0247, 3: 0.0375, 4: 0.0562, 5: 0.075}})
SHOULDER_ELX = {AWK_SKILL_DMG, BOSS_DMG}

# CHEST
CHEST_ELX = set()

# PANTS
ADD_DMG = ('ADD_DMG', ElixirType.Pants, {Stats.AddDmg: {1: 0.0049, 2: 0.0102, 3: 0.0155, 4: 0.0232, 5: 0.031}})
CRIT_DMG = ('CRIT_DMG', ElixirType.Pants, {Stats.CritDmg: {1: 0.0112, 2: 0.0231, 3: 0.035, 4: 0.0525, 5: 0.07}})
SPECIALTY_GAIN = ('SPECIALTY_GAIN', ElixirType.Pants, {Stats.IdentityGain: {1: 0.0064, 2: 0.0132, 3: 0.02, 4: 0.03, 5: 0.04}})
ALLY_ENHANCE = ('ALLY_ENHANCE', ElixirType.Pants, {Stats.APBuff: {1: 0.0096, 2: 0.0198, 3: 0.03, 4: 0.045, 5: 0.06}})
PANTS_ELX = {ADD_DMG, CRIT_DMG, SPECIALTY_GAIN, ALLY_ENHANCE}

# HELMET
HELMET_DPS_COMMON = ('HELMET_DPS_COMMON', ElixirType.Helmet, {Stats.MultDmg: {1: 0.0049, 2: 0.0102, 3: 0.0155, 4: 0.0232, 5: 0.031}})
HELMET_SUP_COMMON = ('HELMET_SUP_COMMON', ElixirType.Helmet, {Stats.HealShield: {1: 0.0023, 2: 0.0047, 3: 0.0072, 4: 0.00108, 5: 0.0144}})
HELMET_ELX = {HELMET_DPS_COMMON, HELMET_SUP_COMMON}

# GLOVES
GLOVES_DPS_COMMON = ('GLOVES_DPS_COMMON', ElixirType.Helmet, {Stats.AtkPower: {1: 0.0023, 2: 0.0047, 3: 0.0072, 4: 0.0108, 5: 0.0144}})
GLOVES_SUP_COMMON = ('GLOVES_SUP_COMMON', ElixirType.Helmet, {Stats.APBuff: {1: 0.0064, 2: 0.0132, 3: 0.02, 4: 0.03, 5: 0.04}})
GLOVES_ELX = {GLOVES_DPS_COMMON, GLOVES_SUP_COMMON}

# SET EFFECTS
CRITICAL = ('CRITICAL', ElixirType.Set, {Stats.MultCDmg: {1: 0.06, 2: 0.12}})
MASTER = ('MASTER', ElixirType.Set, {Stats.CritRate: {1: 0.07, 2: 0.07}, Stats.AddDmg: {1: 0, 2: 0.085}})
BLADED_SHIELD = ('BLADED_SHIELD', ElixirType.Set, {Stats.MultDmg: {1: 0.04, 2: 0.12}})
VANGUARD = ('VANGUARD', ElixirType.Set, {Stats.SkillDmg: {1: 0.03, 2: 0.03}, Stats.AtkPower: {1: 0.03, 2: 0.03},
                                         Stats.MultDmg: {1: 0, 2: 0.05}})
FAITH = ('FAITH', ElixirType.Set, {Stats.APBuff: {1: 0.08, 2: 0.14}, Stats.IdentityGain: {1: 0, 2: 0.05}})
LUMINARY = ('LUMINARY', ElixirType.Set, {Stats.APBuff: {1: 0.08, 2: 0.14}, Stats.SkillCDR: {1: 0, 2: 0.05}})
ADVANCE = ('ADVANCE', ElixirType.Set, {Stats.WpnPower: {1: 2230, 2: 2230}, Stats.MoveSpeed: {1: 0, 2: 0.08},
                                       Stats.APBuff: {1: 0, 2: 0.06}})
SET_ELX = {CRITICAL, MASTER, BLADED_SHIELD, VANGUARD, FAITH, LUMINARY, ADVANCE}
ELX_OPTIONS = set()
ELX_OPTIONS.union(HELMET_ELX, SHOULDER_ELX, CHEST_ELX, PANTS_ELX, GLOVES_ELX, SET_ELX)
