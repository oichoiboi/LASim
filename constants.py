import sqlite3
import csv
import pandas as pd

CRIT_CONSTANT = 0
MSASPEED_CONSTANT = 0
CDRSTAT_CONSTANT = 0


RELIC_WEAPON = {
    1: 15442,
    2: 16069,
    3: 16556,
    4: 17057,
    5: 17574,
    6: 18107,
    7: 18655,
    8: 19220,
    9: 19803,
    10: 20403,
    11: 22239,
    12: 24241,
    13: 26422,
    14: 28800,
    15: 32109,
    16: 34300,
    17: 36641,
    18: 39142,
    19: 41814,
    20: 46678
}

BREL_WEAPON = {
    1: 20001,
    2: 20403,
    3: 21207,
    4: 22461,
    5: 23790,
    6: 25196,
    7: 26686,
    8: 28264,
    9: 31033,
    10: 32430,
    11: 33889,
    12: 35414,
    13: 37008,
    14: 38673,
    15: 40413,
    16: 42232,
    17: 44132,
    18: 46118,
    19: 48194,
    20: 50362,
    21: 52051,
    22: 53796,
    23: 55599,
    24: 57463,
    25: 59390
}

AKKAN_WEAPON = {
    1: 38673,
    2: 39534,
    3: 40413,
    4: 41313,
    5: 42232,
    6: 43172,
    7: 44132,
    8: 45114,
    9: 46118,
    10: 47145,
    11: 48194,
    12: 49266,
    13: 50362,
    14: 52051,
    15: 53796,
    16: 55599,
    17: 57463,
    18: 59390,
    19: 61381,
    20: 63439,
    21: 65566,
    22: 67764,
    23: 70036,
    24: 72384,
    25: 74811
}


class StatLookup():
    def __init__(self):
        self.df = pd.read_excel('C:\LASim\mainstat_table.xlsx')
        self.df.set_index(['Tier', 'Level'], inplace=True)
        self.stat = 0

    def stat_lookup(self, tier: str, level: int, piece: str):
        stat = self.df.loc[(tier, level), piece]
        print(f"The value of {piece} for Tier {tier} and Level {level} is: {stat}")
        return stat
    
ex = StatLookup()
print(ex.df)
stat = ex.stat_lookup('Akkan',25,'Helmet')
print(stat)

    
        