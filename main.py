"""
The main python file. Write all your scenes here!
"""

from basics import in_dev, play

# The ctx stores the game data.
def name_scene(ctx):
    """
Amr Ojjeh (amrojjeh)
ctx[name] stores the name of the player
    """
    name = input("Enter your name: ")
    ctx["name"] = name
    yes_no = input("Would you like to be a kettle? ").lower()
    if yes_no == 'y':
        return yes_kettle_scene
    return no_kettle_scene

def yes_kettle_scene(ctx):
    """
Please contribute to this scene!
    """
    in_dev()

def no_kettle_scene(ctx):
    """
Please contribute to this scene!
    """
    in_dev()

play(name_scene)
