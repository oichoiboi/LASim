from lookupvalues import *
import json
from setup import *

class Gunslinger(Job):
    pass


class GS_Skills(BaseSkill):
    def __init__(self, execution=False, **kwargs):
        super().__init__(**kwargs)
        self.execution = execution


with open('gunslinger.json', 'r') as json_file:
    gs_skills = json.load(json_file)


skills = {GS_Skills(**skill) for skill in gs_skills}
for skill in skills:
    for tripod in skill.tripods:
        print(tripod.name)
        print(tripod.Mult)
        
