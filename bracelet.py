from stats import Stats
from typing import Dict, Union, List, Tuple
from dataclasses import dataclass, field
import enum
from enums import Rarity
from functools import reduce

"""
Bracelet module
"""
H_W = 1
F_C = 1

BRACELET_OPTIONS = {
    'WEDGE': {Stats.AddDmg: {Rarity.COMMON: 0.0163, Rarity.RARE: 0.019, Rarity.EPIC: 0.0244, Rarity.LEGENDARY: 0.0271}},
    'HAMMER':
        {Stats.CritDmg: {Rarity.COMMON: 0.06*H_W, Rarity.RARE: 0.08*H_W, Rarity.EPIC: 0.1*H_W, Rarity.LEGENDARY: 0.12*H_W}},
    'FERVOR': {Stats.MultDmg: {Rarity.COMMON: 0.025*F_C, Rarity.RARE: 0.03*F_C, Rarity.EPIC: 0.035*F_C, Rarity.LEGENDARY: 0.04*F_C}},
    'COOL_HEADED': {
        Stats.MultDmg: {Rarity.COMMON: 0.025*F_C, Rarity.RARE: 0.03*F_C, Rarity.EPIC: 0.035*F_C, Rarity.LEGENDARY: 0.04*F_C}},
    'DAGGER': {Stats.DefRed: {Rarity.COMMON: 0.015, Rarity.RARE: 0.018, Rarity.EPIC: 0.021, Rarity.LEGENDARY: 0.025}},
    'EXPOSE_WEAKNESS': {
        Stats.CritRate: {Rarity.COMMON: 0.015, Rarity.RARE: 0.018, Rarity.EPIC: 0.021, Rarity.LEGENDARY: 0.025}},
    'WEAPON_POWER': {
        Stats.WpnPower: {Rarity.COMMON: 1300, Rarity.RARE: 1600, Rarity.EPIC: 1900, Rarity.LEGENDARY: 2200}},
    'SUPERIORITY': {
        Stats.MultDmg: {Rarity.COMMON: 0.015, Rarity.RARE: 0.02, Rarity.EPIC: 0.025, Rarity.LEGENDARY: 0.03}},
    'ASSAIL': {Stats.CritDmg: {Rarity.COMMON: 0.04, Rarity.RARE: 0.06, Rarity.EPIC: 0.8, Rarity.LEGENDARY: 0.1}},
    'PRECISE': {Stats.CritRate: {Rarity.COMMON: 0.02, Rarity.RARE: 0.03, Rarity.EPIC: 0.04, Rarity.LEGENDARY: 0.05}},
    'AMBUSH': {Stats.BackAtkDmg: {Rarity.COMMON: 0.025, Rarity.RARE: 0.03, Rarity.EPIC: 0.035, Rarity.LEGENDARY: 0.04}},
    'BATTLE': {
        Stats.FrontAtkDmg: {Rarity.COMMON: 0.025, Rarity.RARE: 0.03, Rarity.EPIC: 0.035, Rarity.LEGENDARY: 0.04}},
    'SAWTOOTH': {Stats.CritDmg: {Rarity.COMMON: 0.02, Rarity.RARE: 0.03, Rarity.EPIC: 0.05, Rarity.LEGENDARY: 0.07}},
    'ENLIGHTENMENT': {
        Stats.IdentityGain: {Rarity.COMMON: 0.03, Rarity.RARE: 0.04, Rarity.EPIC: 0.05, Rarity.LEGENDARY: 0.06}}}

class Bracelet:
    def __init__(self, crit=0, swift=0, spec=0, mainStat=0, effects=None):
        if effects is None:
            self.effects = dict()
        self.crit = crit
        self.swift = swift
        self.spec = spec
        self.mainStat = mainStat

    def change_crit(self, stat):
        self.crit = max(0, min(120, stat))

    def change_spec(self, stat):
        self.spec = max(0, min(120, stat))

    def change_swift(self, stat):
        self.swift = max(0, min(120, stat))

    def change_mainStat(self, stat):
        self.mainStat = max(0, min(5000, stat))

    def change_effect(self, old: str, new: str):
        keys = BRACELET_OPTIONS.keys()
        if new in BRACELET_OPTIONS.keys():
            self.effects[new] = self.effects.pop(old, 0)
        H_W = 2*8/14 if 'HAMMER' in keys and 'WEDGE' in keys else 1.00
        F_C = 1.01 if 'FERVOR' in keys and 'COOL_HEAD' in keys else 1.00

    def change_level(self, effect: str, level: int):
        self.effects[effect] = level

    def get_mod(self, mod, mode):
        results = [BRACELET_OPTIONS.get(effect, 0).get(mod, 0).get(level) for effect, level in self.effects]
        if mode == 0:
            return sum(results)
        elif mode == 0:
            return reduce(lambda x, y: x * (y + 1), results, 1)












