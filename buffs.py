from dataclasses import dataclass, field
from typing import List
from enum import Enum

class BuffType(Enum):
    Cycle

class Buff:
    def __init__(self, name, modifiers, values, cooldown):
        self.name = name
        self.modifiers = modifiers  # buffs can modify various values, or are constant.
        self.values = values  # some buffs have values that ramp up, or are constant.
        self.cycles = list()
        self.cooldown = cooldown  # If a buff is perm, cooldown = 0. Otherwise, it has internal cooldown = x.
        self.lastUse = 0
        self.step = 0
        self.average = 0
        self.max = 0

    def available(self, time):
        """
        Should work regardless if it's a permanent buff or not
        """
        if time > (self.lastUse + self.cooldown):
            return True
        return False

    def modifier(self, time):
        pass

    def get_cyclic_value(self, time):
        total_cycle_time = sum(duration for _, duration in self.cycles)
        current_time = time % total_cycle_time

        for value, duration in self.cycles:
            if current_time < duration:
                return value
            current_time -= duration

        # If time exceeds the total cycle time, return the first value
        return self.cycles[0][0]


self.cycles = [("x", 2), ("y", 2), ("z", 2), ("w", 4)]
time = 20  # seconds
value = get_cyclic_value(time, self.cycles)
print(f"The value at time {time}s is: {value}")
