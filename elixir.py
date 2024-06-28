from stats import Stats

"""
Define an Elixir class, and then instantiate every relevant elixir in the game
"""
OPTIONS = {"Common": [
    'ATTACK_POWER', 'WEAPON_POWER', 'MAIN_STAT', 'STAGGER',
    'MASTER_OF_EVASION', 'ESCAPE_EXPERT', 'EXPLOSIVES_EXPERT',
    'POTION_POISONING', 'MP', 'BLESSING_OF_LIFE', 'RESOURCE_BLESSING',
    'VAGABOND'],
    "Shoulder": ['AWK_SKILL_DMG', 'BOSS_DMG', 'SHIELD_ENHANCE', 'HEALING_ENHANCE'],
    "Chest": ['INCOMING_DMG_RED', 'MAG_DEF', 'PHY_DEF', 'MAX_HP'],
    "Pants": ['ADD_DMG', 'CRIT_DMG', 'SPECIALTY_GAIN', 'ALLY_ENHANCE']
}

COMMON = {
    'ATTACK_POWER': {1: 122, 2: 253, 3: 383, 4: 575, 5: 767},
    'WEAPON_POWER': {1: 236, 2: 488, 3: 740, 4: 1110, 5: 1480},
    'MAIN_STAT': {1: 720, 2: 1782, 3: 2700, 4: 4050, 5: 5400},
    'STAGGER': {1: 0.0038, 2: 0.0079, 3: 0.012, 4: 0.018, 5: 0.024},
    'MASTER_OF_EVASION': {1: 0.0038, 2: 0.0079, 3: 0.012, 4: 0.018, 5: 0.024},
    'ESCAPE_EXPERT': {1: 0.0038, 2: 0.0079, 3: 0.012, 4: 0.018, 5: 0.024},
    'EXPLOSIVES_EXPERT': {1: 0.016, 2: 0.033, 3: 0.05, 4: 0.075, 5: 0.1},
    'POTION_POISONING': {1: 0.0113, 2: 0.0234, 3: 0.0355, 4: 0.0532, 5: 0.071},
    'MP': {1: 15, 2: 32, 3: 49, 4: 73, 5: 98},
    'BLESSING_OF_LIFE': {1: 6, 2: 12, 3: 19, 4: 29, 5: 39},
    'RESOURCE_BLESSING': {1: 0.0046, 2: 0.0095, 3: 0.0145, 4: 0.0217, 5: 0.029},
    'VAGABOND': {1: 0.008, 2: 0.0165, 3: 0.025, 4: 0.0375, 5: 0.05}
}

SHOULDER = {
        'AWK_SKILL_DMG': {1: 0.012, 2: 0.0247, 3: 0.0375, 4: 0.0562, 5: 0.075},
        'BOSS_DMG': {1: 0.0038, 2: 0.0079, 3: 0.012, 4: 0.018, 5: 0.024},
        'SHIELD_ENHANCE': {1: 0.0067, 2: 0.0138, 3: 0.021, 4: 0.0315, 5: 0.042},
        'HEALING_ENHANCE': {1: 0.0067, 2: 0.0138, 3: 0.021, 4: 0.0315, 5: 0.042}
}

CHEST = {
        'INCOMING_DMG_RED': {1: -0.016, 2: 0.033, 3: 0.05, 4: 0.075, 5: 0.1},
        'MAG_DEF': {1: 960, 2: 1980, 3: 3000, 4: 4500, 5: 6000},
        'PHY_DEF': {1: 960, 2: 1980, 3: 3000, 4: 4500, 5: 6000},
        'MAX_HP': {1: 2720, 2: 5610, 3: 8500, 4: 12750, 5: 17000}
}

PANTS = {
        'ADD_DMG': {1: 0.0049, 2: 0.0102, 3: 0.0155, 4: 0.0232, 5: 0.031},
        'CRIT_DMG': {1: 0.0112, 2: 0.0231, 3: 0.035, 4: 0.0525, 5: 0.07},
        'SPECIALTY_GAIN': {1: 0.0064, 2: 0.0132, 3: 0.02, 4: 0.03, 5: 0.04},
        'ALLY_ENHANCE': {1: 0.0096, 2: 0.0198, 3: 0.03, 4: 0.045, 5: 0.06}
}

HELMET_COMMON = {1: 0.0049, 2: 0.0102, 3: 0.0155, 4: 0.0232, 5: 0.031}
HELMET_SETS = {'DMG': {1: 0.0049, 2: 0.0102, 3: 0.0155, 4: 0.0232, 5: 0.031},
          'BLADED_SHIELD': {1: 0.04, 2: 0.08},
          'CRITICAL': ''






