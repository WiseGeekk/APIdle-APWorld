from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import APIdleWorld


def create_and_connect_regions(world: APIdleWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: APIdleWorld) -> None:
    test1 = Region("Test1", world.player, world.multiworld)
    test2 = Region("Test2", world.player, world.multiworld)

    regions = [test1, test2]

    # # Some regions may only exist if the player enables certain options.
    # # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # if world.options.hammer:
    #     top_middle_room = Region("Top Middle Room", world.player, world.multiworld)
    #     regions.append(top_middle_room)

    world.multiworld.regions += regions


def connect_regions(world: APIdleWorld) -> None:
    test1 = world.get_region("Test1")
    test2 = world.get_region("Test2")

    # An even easier way is to use the region.connect helper.
    test1.connect(test2, "Test1 to Test2")

    # # Some Entrances may only exist if the player enables certain options.
    # # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # # In this case, we previously created an extra "Top Middle Room" region that we now need to connect to Overworld.
    # if world.options.hammer:
    #     top_middle_room = world.get_region("Top Middle Room")
    #     overworld.connect(top_middle_room, "Overworld to Top Middle Room")