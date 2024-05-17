import enum

class Position(enum.Enum):
    NONPOSITIONAL = 1
    FRONTATTACK = 2
    BACKATTACK = 3
    FRONTBACK = 4
    
    @classmethod
    def from_json(cls, value):
        if isinstance(value, int):
            return cls(value)
        elif isinstance(value, str):
            return cls[value]
    
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
    HELMET = "Helmet"
    SHOULDER = "Shoulder"
    CHEST = "Chest"
    PANTS = "Pants"
    WEAPON = "Weapon"
    
class GearTier(str, enum.Enum):
    RELIC = "Relic"
    BREL = "Brelshaza"
    AKKAN = "Akkan"

tier = GearTier.AKKAN
print(tier.value)