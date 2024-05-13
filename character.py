import json
from stats import *
from skills import Tripod, Skill
from enum import *

class Character(Stats):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.skills = []
        self.maxGauge = 0
        self.lvlcoefficient = {key: 0 for key in range(13)}
        
class Gunslinger(Character):
    pass


with open('test.json', 'r') as json_file:
    gs_skills = json.load(json_file)


skills = [Skill(**skill) for skill in gs_skills]
for skill in skills:
    print(skill.name, skill.position, skill.activation)
        
