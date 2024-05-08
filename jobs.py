import json
from stats import *
from skills import Tripod, Skill

class Job(Stats):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.skills = []
        self.maxGauge = 0
        self.lvlcoefficient = {key: 0 for key in range(13)}
        
class Gunslinger(Job):
    pass


with open('test.json', 'r') as json_file:
    gs_skills = json.load(json_file)


skills = [Skill(**skill) for skill in gs_skills]
for skill in skills:
    for tripod in skill.tripods:
        print(tripod.stat_dict)
        tripod.change_level(5)
        print(tripod.Atkspeed)
        