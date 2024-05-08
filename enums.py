import enum

class Direction(enum.Enum):
    NONPOSITIONAL = 1
    FRONTATTACK = 2
    BACKATTACK = 3
    FRONTBACK = 4
    
class Activation(enum.Enum):
    NORMAL = 1
    HOLDCAST = 2
    CHARGE = 3