from dataclasses import dataclass, field
from typing import List
from enum import Enum


class BuffType(Enum):
    Constant = 1  # not sure if I want to add this
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
        pass  # may need this later, maybe not

    def available(self, current_time):
        """
        Should work regardless if it's a permanent buff or not
        """
        match self.buffType:
            case BuffType.Constant:
                return True
            case BuffType.Cycle:
                """
                For now I haven't found a buff that cycles and has a cooldown
                """
                return True
            case BuffType.Temp:
                if current_time > (self.lastUse + self.cooldown):
                    return True
        return False

    def modifier(self, current_time):
        pass

    def get_cyclic_value(self, current_time):
        total_cycle_time = sum(duration for _, duration in self.cycles)
        match_cycle = current_time % total_cycle_time

        for value, duration in self.cycles:
            if match_cycle < duration:
                return value
            match_cycle -= duration

        # If time exceeds the total cycle time, return the first value
        return self.cycles[0][0]


self.cycles = [("x", 2), ("y", 2), ("z", 2), ("w", 4)]
time = 20  # seconds
value = get_cyclic_value(time, self.cycles)
print(f"The value at time {time}s is: {value}")
