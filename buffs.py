from dataclasses import dataclass, field
class Buff():
    def __init__(self, name, modifiers, values, cooldown):
        self.name = name
        self.modifiers = modifiers #buffs can modify various values, or are constant.
        self.values = values #some buffs have values that ramp up, or are constant.
        self.cooldown = cooldown #If a buff is perm, cooldown = 0. Otherwise, it has internal cooldown = x.
        self.lastUse = 0
        self.step = 0
        self.average = 0
        self.max = 0
        
        
    def available(self, time):
        '''
        Should work regardless if it's a permanent buff or not
        '''
        if time > (self.lastUse + self.cooldown):
            return True
        return False
    
    def modifier(self, time):
        
        
    
    