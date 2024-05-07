import pandas as pd
import json

CRIT_CONSTANT = 0
MSASPEED_CONSTANT = 0
CDRSTAT_CONSTANT = 0

STAT_KEYS_ADD = [
    "AP",
    "Add",
    "Atkspeed",
    "AwkCDR",
    "CDR_Flat",
    "CDR1",
    "CDR2",
    "CDmg",
    "ChargeAS",
    "Crit",
    "DefRed",
    "HBCDdmg",
    "HCAS",
    "MCDmg",
    "MainStat",
    "Movespeed",
    "SkillCDR",
    "WpnPower",
]
STAT_KEYS_MULT = [
    "AwkMult",
    "Back",
    "Charge",
    "HC",
    "HM",
    "Head",
    "HeadBack",
    "Mult",
    "SkillMult",
]

with open("mainstat_table.json", "r") as json_file:
    gear_stats = json.load(json_file)



