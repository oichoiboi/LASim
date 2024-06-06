from dataclasses import dataclass, field
from typing import List
from enum import Enum

class BuffType(Enum):
    Constant = 1 # not sure if I want to add this
    Temp = 2
    Cycle = 3

@dataclass
class Buff:
    name: str = "None"
    modifiers: List[str] | str = "None"
    buffType: BuffType = BuffType.Constant
    values: List[float] | float = 0
    cycles: List[float] | float = 0
    cooldown: float = 0
    lastUse: float = 0
    average: float = 0
    max: float = 0

    def __post_init__(self):
        if self.buffType is BuffType.Temp:
    def available(self, current_time):
        """
        Should work regardless if it's a permanent buff or not
        """
        if self.buffType is BuffType.Constant or self.buffType is BuffType.Cycle:
            return True
        elif self.buffType is BuffType.Temp and current_time > (self.lastUse + self.cooldown):
            return True
        return False

    def modifier(self, current_time):
        pass

    def get_cyclic_value(self, current_time):
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
