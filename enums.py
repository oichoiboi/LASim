import enum


class Position(enum.Enum):
    NONPOSITIONAL = 1
    FRONTATTACK = 2
    BACKATTACK = 3
    FRONTBACK = 4

    
class Activation(enum.Enum):
    NORMAL = 1
    HOLDCAST = 2
    CHARGE = 3
    CHAIN = 4
    COMBO = 5
    
    
class Rarity(enum.Enum):
    COMMON = 1
    RARE = 2
    EPIC = 3
    LEGENDARY = 4


class Rune(enum.Enum):
    GALEWIND = 1
    OVERWHELM = 2
    WEALTH = 3
    FOCUS = 4
    QUICK = 5
    BLEED = 6


class GemType(enum.Enum):
    DAMAGE = 1
    COOLDOWN = 2


class GearType(enum.Enum):
    Helmet = "Helmet"
    Shoulder = "Shoulder"
    Chest = "Chest"
    Pants = "Pants"
    Gloves = "Gloves"
    Weapon = "Weapon"


class GearTier(enum.Enum):
    Relic = "Relic"
    Brel = "Brelshaza"
    Akkan = "Akkan"
    T4Relic = "T4Relic"
    T4Ancient = "T4Ancient"

