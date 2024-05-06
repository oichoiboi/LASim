from setup import *

class Simulator():
    def __init__(self) -> None:
        self.stats = Stats()
        self.helmet = Gear('Helmet')
        self.shoulders = Gear('Shoulders')
        self.chest = Gear('Chest')
        self.pants = Gear('Pants')
        self.gloves = Gear('Gloves')
        self.weapon = Gear('Weapon')
        self.job = Job()