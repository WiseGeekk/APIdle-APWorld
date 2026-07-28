from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import APIdleWorld


ITEM_NAME_TO_ID = {
    "SampleItem": 1,
    "SampleFiller": 2
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "SampleItem": ItemClassification.progression,
    "SampleFiller": ItemClassification.filler,
}


class APIdleItem(Item):
    game = "APIdle"


def get_random_filler_item_name(world: APIdleWorld) -> str:
    return "SampleFiller"


def create_item_with_correct_classification(world: APIdleWorld, name: str) -> APIdleItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    # It is perfectly normal and valid for an item's classification to differ based on the player's options.
    # In our case, Health Upgrades are only relevant to logic (and thus labeled as "progression") in hard mode.
    # if name == "Health Upgrade" and world.options.hard_mode:
    #     classification = ItemClassification.progression

    return APIdleItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: APIdleWorld) -> None:

    itempool: list[Item] = [
        world.create_item("SampleItem"),
        world.create_item("SampleFiller"),
    ]

    # Some items may only exist if the player enables certain options.
    # In our case, If the hammer option is enabled, the sixth item is the Hammer.
    # Otherwise, we add a filler Confetti Cannon.
    # if world.options.hammer:
        # Once again, it is important to stress that even though the Hammer doesn't always exist,
        # it must be present in the worlds item_name_to_id.
        # Whether it is actually in the itempool is determined purely by whether we create and add the item here.
        # itempool.append(world.create_item("Hammer"))

    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool

    # Sometimes, you might want the player to start with certain items already in their inventory.
    # These items are called "precollected items".
    # They will be sent as soon as they connect for the first time (depending on your client's item handling flag).
    # Players can add precollected items themselves via the generic "start_inventory" option.
    # If you want to add your own precollected items, you can do so via world.push_precollected().
    # if world.options.start_with_one_confetti_cannon:
        # We're adding a filler item, but you can also add progression items to the player's precollected inventory.
        # starting_confetti_cannon = world.create_item("Confetti Cannon")
        # world.push_precollected(starting_confetti_cannon)