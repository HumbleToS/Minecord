from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from discord import User


class Player:
    __slots__ = ('user', 'current_health', 'max_health', 'inventory', 'level', 'experience', 'experience_to_next_level',
                 'selected', 'armor', 'tools', 'quests', 'guild', 'strength', 'defense', 'intelligence', 'fortune')

    def __init__(self, **kwargs):
        self.user: User = kwargs.get('user')
        self.current_health = kwargs.get('health', 100)
        self.max_health = kwargs.get('max_health', 100)
        self.inventory = kwargs.get('inventory', {})
        self.level = kwargs.get('level', 1)
        self.experience = kwargs.get('experience', 0)
        self.experience_to_next_level = kwargs.get('experience_to_next_level', 100)
        self.selected = kwargs.get('selected', None)
        self.armor = kwargs.get('armor', None)
        self.tools = kwargs.get('tools', {})
        self.quests = kwargs.get('quests', {})
        self.guild = kwargs.get('guild', None)
        self.strength = kwargs.get('strength', 100)
        self.defense = kwargs.get('defense', 100)
        self.intelligence = kwargs.get('intelligence', 100)
        self.fortune = kwargs.get('mining_fortune', 0)
