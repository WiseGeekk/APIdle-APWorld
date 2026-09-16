from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import APIdleWorld
     
LOCATION_NAME_TO_ID = {
    "Test Location 1": 1,
    "Test Location 2": 2,
}


class APIdleLocation(Location):
    game = "APIdle"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: APIdleWorld) -> None:
    create_regular_locations(world)
    #create_events(world)


def create_regular_locations(world: APIdleWorld) -> None:
    test1 = world.get_region("Test1")
    test2 = world.get_region("Test2")

    test1_locations = get_location_names_with_ids(
        ["Test Location 1"]
    )
    test1.add_locations(test1_locations, APIdleLocation)

    test2_locations = get_location_names_with_ids(
        ["Test Location 2"]
    )
    test2.add_locations(test2_locations, APIdleLocation)

    # Locations may be in different regions depending on the player's options.
    # In our case, the hammer option puts the Top Middle Chest into its own room called Top Middle Room.
    # top_middle_room_locations = get_location_names_with_ids(["Top Middle Chest"])
    # if world.options.hammer:
    #     top_middle_room = world.get_region("Top Middle Room")
    #     top_middle_room.add_locations(top_middle_room_locations, APQuestLocation)
    # else:
    #     overworld.add_locations(top_middle_room_locations, APQuestLocation)

    # Locations may exist only if the player enables certain options.
    # In our case, the extra_starting_chest option adds the Bottom Left Extra Chest location.
    # if world.options.extra_starting_chest:
        # Once again, it is important to stress that even though the Bottom Left Extra Chest location doesn't always
        # exist, it must still always be present in the world's location_name_to_id.
        # Whether the location actually exists in the seed is purely determined by whether we create and add it here.
        # bottom_left_extra_chest = get_location_names_with_ids(["Bottom Left Extra Chest"])
        # overworld.add_locations(bottom_left_extra_chest, APQuestLocation)


# def create_events(world: APIdleWorld) -> None:
#     # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
#     # In our case, the player must press a button in the top left room to open the final boss door.
#     # AP has something for this purpose: "Event locations" and "Event items".
#     # An event location is no different than a regular location, except it has the address "None".
#     # It is treated during generation like any other location, but then it is discarded.
#     # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
#     # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
#     top_left_room = world.get_region("Top Left Room")
#     final_boss_room = world.get_region("Final Boss Room")

#     # One way to create an event is simply to use one of the normal methods of creating a location.
#     button_in_top_left_room = APQuestLocation(world.player, "Top Left Room Button", None, top_left_room)
#     top_left_room.locations.append(button_in_top_left_room)

#     # We then need to put an event item onto the location.
#     # An event item is an item whose code is "None" (same as the event location's address),
#     # and whose classification is "progression". Item creation will be discussed more in items.py.
#     # Note: Usually, items are created in world.create_items(), which for us happens in items.py.
#     # However, when the location of an item is known ahead of time (as is the case with an event location/item pair),
#     # it is common practice to create the item when creating the location.
#     # Since locations also have to be finalized after world.create_regions(), which runs before world.create_items(),
#     # we'll create both the event location and the event item in our locations.py code.
#     button_item = items.APIdleItem("Top Left Room Button Pressed", ItemClassification.progression, None, world.player)
#     button_in_top_left_room.place_locked_item(button_item)

#     # A way simpler way to do create an event location/item pair is by using the region.create_event helper.
#     # Luckily, we have another event we want to create: The Victory event.
#     # We will use this event to track whether the player can win the game.
#     # The Victory event is a completely optional abstraction - This will be discussed more in set_rules().
#     final_boss_room.add_event(
#         "Final Boss Defeated", "Victory", location_type=APQuestLocation, item_type=items.APIdleItem
#     )

#     # If you create all your regions and locations line-by-line like this,
#     # the length of your create_regions might get out of hand.
#     # Many worlds use more data-driven approaches using dataclasses or NamedTuples.
#     # However, it is worth understanding how the actual creation of regions and locations works,
#     # That way, we're not just mindlessly copy-pasting! :)