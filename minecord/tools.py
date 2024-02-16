import random
from typing import TYPE_CHECKING, List, Dict

if TYPE_CHECKING:
    from enums import Emojis, Rarity, Spread


class Item:
    __slots__ = ('name', 'description', 'emoji', 'rarity', 'sell_value', 'data')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', "Unknown Item")
        self.description = kwargs.get('description',
                                      "Nothing to see here. Move along.")
        self.emoji = kwargs.get('emoji', None)
        self.sell_value = kwargs.get('sell_value', 1)
        self.data: dict = kwargs.get('data', {})


class DropItem(Item):
    __slots__ = ('probability', 'always', 'min_amount', 'max_amount', 'spread')

    def __init__(self, probability: int, always: bool, min_amount: int, max_amount: int, spread: Spread,
                 **kwargs):
        super().__init__(**kwargs)
        self.probability = probability
        self.always = always
        self.min_amount = min_amount
        self.max_amount = max_amount
        self.spread = spread

    def collect(self, player):

        # every 100 fortune guarantees an extra item
        # each 1 fortune gives a 1% chance to get an extra item
        # e.g. 429 fortune gives 4 extra items and a 29% chance for a 5th extra item

        remainder = 1 if random.randint(0, 99) >= player.fortune % 100 else 0
        bonus = player.fortune // 100 + remainder

        return random.randint(self.min_amount, self.max_amount) + bonus


class LootTable:
    def __init__(self, items: List[DropItem]):
        self.items = items

    def roll(self, player):

        loot: Dict[Item, int] = {}

        for item in self.items:
            if item.always:
                loot[item] = item.collect(player)
            else:
                if random.randint(1, 4096) <= item.probability:
                    loot[item] = item.collect(player)

        return loot

    @classmethod
    def default(cls):
        return ...


class Tool:
    __slots__ = ('name', 'description', 'emoji', 'rarity', 'loot_table', 'data')

    def __init__(self,
                 **kwargs):
        self.name = kwargs.get('name', "Unknown Tool")
        self.description = kwargs.get('description',
                                      "Newton's third law states that every action force has an equal and opposite "
                                      "reaction force.")
        self.emoji: Emojis = kwargs.get('emoji', Emojis.unknown)
        self.rarity: Rarity = kwargs.get('rarity', Rarity.common)
        self.loot_table = kwargs.get('loot_table', None)
        self.data: dict = kwargs.get('data', {})
