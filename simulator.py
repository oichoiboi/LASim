
import json
from stats import *

with open('data/mainstat_table.json', 'r') as json_file:
    gear_stats = json.load(json_file)
pieces = ["Helmet", "Shoulders", "Chest", "Pants", "Gloves", "Weapon"]

class Simulator:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gear = []
        for gear in pieces:
            self.gear.append(Gear(gear, 0, 0, 25, "Akkan", gear_stats))

test = Simulator()
for gear in test.gear:
    gear.get_gear_value()
    print("Type:", gear.type)
    print("MainStat:", gear.MainStat)
    print("WpnPower:", gear.WpnPower, "\n")