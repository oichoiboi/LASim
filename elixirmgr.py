from stats import Stats
from typing import Dict, Union, Tuple
from dataclasses import dataclass, field
from elixir import (ElixirType, COMMON_ELX, HELMET_ELX, SHOULDER_ELX,
                    CHEST_ELX, PANTS_ELX, GLOVES_ELX, SET_ELX, ELX_OPTIONS)
import enum


@dataclass
class ElixirPiece:
    piece: ElixirType
    elx1: Union[Tuple, None]
    elx2: Union[Tuple, None]
    elx1_lvl: int
    elx2_lvl: int

    @staticmethod
    def find_elx(elx_name: str):
        return next((elx for elx in ELX_OPTIONS if elx[0] == elx_name), None)  # find the elixir with the matching name

    def change_elx1_effect(self, elx_name: str):
        elx = self.find_elx(elx_name)
        if elx is None:
            print("Elixir could not be found")
        elif elx[1] == self.elx1[1] or elx[1] == ElixirType.Common:
            self.elx1 = elx

    def change_elx2_effect(self, elx_name: str):
        elx = self.find_elx(elx_name)
        if elx is None:
            print("Elixir could not be found")
        elif elx[1] == self.elx2[1] or elx[1] == ElixirType.Common:
            self.elx1 = elx

    def change_elx1_lvl(self, lvl: int):
        self.elx1_lvl = min(lvl, 5)

    def change_elx2_lvl(self, lvl: int):
        self.elx2_lvl = min(lvl, 5)

    def get_elx_value(self, mod):
        return self.elx1[2].get(mod, 0)[self.elx1_lvl], self.elx2[2].get(mod, 0)[self.elx2_lvl]


@dataclass
class ElixirMgr:
    elixirs: Dict[ElixirType, ElixirPiece] = field(default_factory=Dict)
    set_elixir: Tuple = field(default=None)

    def __post_init__(self):
        if not self.elixirs:
            self.elixirs = {piece: ElixirPiece(piece, None, None, 0, 0) for piece in ElixirType}

    def change_elx_effect(self, piece, elx_name, slot: int):
        if slot == 1:
            self.elixirs[piece].change_elx1_effect(elx_name)
        elif slot == 2:
            self.elixirs[piece].change_elx2_effect(elx_name)
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
            values.append(self.set_elixir[2].get(mod, 0)[set_level])
        return values
