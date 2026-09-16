from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

#from .options import option_groups, option_presets


class APIdleWebWorld(WebWorld):
    game = "APIdle"

    theme = "stone"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up APIdle for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["WiseGeekk"],
    )

    # We add these tutorials to our WebWorld by overriding the "tutorials" field.
    tutorials = [setup_en]

    # If we have option groups and/or option presets, we need to specify these here as well.
    #option_groups = option_groups
    #options_presets = option_presets