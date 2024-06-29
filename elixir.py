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


@dataclass
class Elixir:
    name: str
    mods: Dict[Stats, Dict[int, float]]

    def get_value(self, mod, lvl):
        return self.mods.get(mod, 0).get(lvl, 0)


# COMMON
ATTACK_POWER = Elixir('ATTACK_POWER', {Stats.FlatAP: {1: 122, 2: 253, 3: 383, 4: 575, 5: 767}})
WEAPON_POWER = Elixir('WEAPON_POWER', {Stats.WpnPower: {1: 236, 2: 488, 3: 740, 4: 1110, 5: 1480}})
MAIN_STAT = Elixir('MAIN_STAT', {Stats.MainStat: {1: 720, 2: 1782, 3: 2700, 4: 4050, 5: 5400}})
COMMON_ELX = {ATTACK_POWER, WEAPON_POWER, MAIN_STAT}

# SHOULDER
AWK_SKILL_DMG = Elixir('AWK_SKILL_DMG', {Stats.AwkDmg: {1: 0.012, 2: 0.0247, 3: 0.0375, 4: 0.0562, 5: 0.075}})
BOSS_DMG = Elixir('BOSS_DMG', {Stats.MultDmg: {1: 0.012, 2: 0.0247, 3: 0.0375, 4: 0.0562, 5: 0.075}})
SHOULDER_ELX = {AWK_SKILL_DMG, BOSS_DMG}

# CHEST
CHEST_ELX = list()

# PANTS
ADD_DMG = Elixir('ADD_DMG', {Stats.AddDmg: {1: 0.0049, 2: 0.0102, 3: 0.0155, 4: 0.0232, 5: 0.031}})
CRIT_DMG = Elixir('CRIT_DMG', {Stats.CritDmg: {1: 0.0112, 2: 0.0231, 3: 0.035, 4: 0.0525, 5: 0.07}})
SPECIALTY_GAIN = Elixir('SPECIALTY_GAIN', {Stats.IdentityGain: {1: 0.0064, 2: 0.0132, 3: 0.02, 4: 0.03, 5: 0.04}})
ALLY_ENHANCE = Elixir('ALLY_ENHANCE', {Stats.APBuff: {1: 0.0096, 2: 0.0198, 3: 0.03, 4: 0.045, 5: 0.06}})
PANTS_ELX = {ADD_DMG, CRIT_DMG, SPECIALTY_GAIN, ALLY_ENHANCE}

# HELMET
HELMET_DPS_COMMON = Elixir('HELMET_DPS_COMMON', {Stats.MultDmg: {1: 0.0049, 2: 0.0102, 3: 0.0155, 4: 0.0232, 5: 0.031}})
HELMET_SUP_COMMON = Elixir('HELMET_SUP_COMMON',
                           {Stats.HealShield: {1: 0.0023, 2: 0.0047, 3: 0.0072, 4: 0.00108, 5: 0.0144}})
HELMET_ELX = {HELMET_DPS_COMMON, HELMET_SUP_COMMON}

# GLOVES
GLOVES_DPS_COMMON = Elixir('GLOVES_DPS_COMMON',
                           {Stats.AtkPower: {1: 0.0023, 2: 0.0047, 3: 0.0072, 4: 0.0108, 5: 0.0144}})
GLOVES_SUP_COMMON = Elixir('GLOVES_SUP_COMMON', {Stats.APBuff: {1: 0.0064, 2: 0.0132, 3: 0.02, 4: 0.03, 5: 0.04}})
GLOVES_ELX = {GLOVES_DPS_COMMON, GLOVES_SUP_COMMON}

# SET EFFECTS
CRITICAL = Elixir('CRITICAL', {Stats.MultCDmg: {1: 0.06, 2: 0.12}})
MASTER = Elixir('MASTER', {Stats.CritRate: {1: 0.07, 2: 0.07}, Stats.AddDmg: {1: 0, 2: 0.085}})
BLADED_SHIELD = Elixir('BLADED_SHIELD', {Stats.MultDmg: {1: 0.04, 2: 0.12}})
VANGUARD = Elixir('VANGUARD', {Stats.SkillDmg: {1: 0.03, 2: 0.03}, Stats.AtkPower: {1: 0.03, 2: 0.03},
                               Stats.MultDmg: {1: 0, 2: 0.05}})
FAITH = Elixir('FAITH', {Stats.APBuff: {1: 0.08, 2: 0.14}, Stats.IdentityGain: {1: 0, 2: 0.05}})
LUMINARY = Elixir('LUMINARY', {Stats.APBuff: {1: 0.08, 2: 0.14}, Stats.SkillCDR: {1: 0, 2: 0.05}})
ADVANCE = Elixir('ADVANCE',
                 {Stats.WpnPower: {1: 2230, 2: 2230}, Stats.MoveSpeed: {1: 0, 2: 0.08}, Stats.APBuff: {1: 0, 2: 0.06}})

SET_ELX = {CRITICAL, MASTER, BLADED_SHIELD, VANGUARD, FAITH, LUMINARY, ADVANCE}

elx_options = {ElixirType.Common: COMMON_ELX,
               ElixirType.Helmet: HELMET_ELX,
               ElixirType.Shoulder: SHOULDER_ELX,
               ElixirType.Chest: CHEST_ELX,
               ElixirType.Pants: PANTS_ELX,
               ElixirType.Gloves: GLOVES_ELX
               }


@dataclass
class ElixirPiece:
    piece: ElixirType
    elx1: Union[Elixir, None]
    elx2: Union[Elixir, None]
    elx1_lvl: int
    elx2_lvl: int

    def change_elx1_effect(self, elx1: Elixir):
        if elx1 is None:
            pass
        elif elx1 in elx_options.get(self.piece) or elx1 in elx_options.get(ElixirType.Common):
            self.elx1 = elx1

    def change_elx2_effect(self, elx2: Elixir):
        if elx2 is None:
            pass
        elif elx2 in elx_options.get(self.piece) or elx2 in elx_options.get(ElixirType.Common):
            self.elx1 = elx2

    def change_elx1_lvl(self, lvl: int):
        self.elx1_lvl = min(lvl, 5)

    def change_elx2_lvl(self, lvl: int):
        self.elx2_lvl = min(lvl, 5)

    def get_elx_value(self, mod):
        return self.elx1.get_value(mod, self.elx1_lvl), self.elx2.get_value(mod, self.elx2_lvl)


@dataclass
class ElixirMgr:
    elixirs: Dict[ElixirType, ElixirPiece] = field(default_factory=Dict)
    set_elixir: Elixir = field(default=None)

    def __post_init__(self):
        if not self.elixirs:
            self.elixirs = {piece: ElixirPiece(piece, None, None, 0, 0) for piece in ElixirType}

    def change_elx_effect(self, piece, elx: Elixir, slot: int):
        if slot == 1:
            self.elixirs[piece].change_elx1_effect(elx)
        elif slot == 2:
            self.elixirs[piece].change_elx2_effect(elx)
        else:
            pass

    def change_elx_lvl(self, piece, lvl: int, slot: int):
        if slot == 1:
            self.elixirs[piece].change_elx1_lvl(lvl)
        elif slot == 2:
            self.elixirs[piece].change_elx2_lvl(lvl)
        else:
            pass

    def change_set_elixir(self, elx):
        if elx in SET_ELX:
            self.set_elixir = elx

    @property
    def elixir_points(self):
        return sum(piece.elx1_lvl + piece.elx2_lvl for piece in self.elixirs.values())

    @property
    def elixir_set_effect_level(self):
        if self.elixir_points >= 40:
            return 2
        elif self.elixir_points >= 35:
            return 1
        else:
            return 0

    def get_total_mod(self, mod):
        set_level = self.elixir_set_effect_level
        values = [
            value
            for piece in self.elixirs.values()
            for value in piece.get_elx_value(mod)
            if value != 0
        ]
        if set_level > 0:
            values.append(self.set_elixir.get_value(mod, set_level))
        return values
