import pandas as pd
import json

CRIT_CONSTANT = 0
MSASPEED_CONSTANT = 0
CDRSTAT_CONSTANT = 0

STATLUT = pd.read_excel('C:\LASim\mainstat_table.xlsx')

STAT_KEYS = ['AP', 'Add', 'Atkspeed', 'AwkCDR', 'AwkMult', 'Back', 'CDR1', 'CDR2', 'CDmg', 
             'Charge', 'ChargeAS', 'Crit', 'DefRed', 'HBCDdmg', 'HC', 'HCAS', 'HM', 'Head', 
             'HeadBack', 'MCDmg', 'Main Stat', 'Movespeed', 'SkillCDR', 'SkillMult', 'WpnPower']

with open('mainstat_table.json', 'r') as json_file:
    gear_stats = json.load(json_file)

def get_gear_value(data, tier, level, piece):
    tier_data = data.get(tier, [])
    item = next((item for item in tier_data if item['Level'] == level and piece in item), None)
    return item[piece] if item else 0






    
        