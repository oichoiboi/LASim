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
    baseCD: float = 0  # holds base cooldown of a buff
    cycleTime: float = field(default=0, init=False)
    lastUse: float = field(default=0, init=False)
    average: float = field(default=0, init=False)
    max: float = field(default=0, init=False)

    def __post_init__(self):
        if self.buffType is BuffType.Cycle:
            if self.cycles is List:
                self.cycleTime = sum(self.cycles)
            else:
                self.cycleTime = 0

    def available(self, current_time):
        """
        Should work regardless if it's a permanent buff or not
        """
        match self.buffType:
            case BuffType.Constant:
                return True
            case BuffType.Cycle:
                """
                For now I haven't found a buff that cycles and has a baseCD
                """
                return True
            case BuffType.Temp:
                if current_time > (self.lastUse + self.baseCD):
                    return True
        return False

    def modifier(self, current_time):
        pass

    def get_cyclic_value(self, current_time):
        match_cycle = current_time % self.cycleTime
        for value, duration in self.cycles:
            if match_cycle < duration:
                return value
            match_cycle -= duration

        # If time exceeds the total cycle time, return the first value
        return self.cycles[0][0]


def get_cyclic_value(cycles, values, current_time):
    match_cycle = current_time % sum(cycles)
    for duration in range(len(cycles)):
        if match_cycle < cycles[duration]:
            return values[duration]
        match_cycle -= duration
    return values[0]


def main():
    value = get_cyclic_value([10, 20, 30], [1, 2, 3, 4], 2)
    print(value)


if __name__ == '__main__':
    main()
