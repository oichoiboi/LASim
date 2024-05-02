import sqlite3
import csv
import pandas as pd

CRIT_CONSTANT = 0
MSASPEED_CONSTANT = 0
CDRSTAT_CONSTANT = 0

STATLUT = pd.read_excel('C:\LASim\mainstat_table.xlsx')
json_data = STATLUT.to_json()
print(json_data)

HELMET = 'Helmet'
SHOULDERS = 'Shoulders'
CHEST = 'Chest'
PANTS = 'Pants'
GLOVES = 'Gloves'
WEAPON = 'Weapon'




    
        