import enum


class Emojis(enum.Enum):
    unknown = " "


class Rarity(enum.Enum):
    common = 0
    uncommon = 1
    rare = 2
    epic = 3
    legendary = 4
    mythic = 5
    divine = 6
    special = 7
    very_special = 8


class Spread(enum.Enum):
    normal = 0
    uniform = 1
