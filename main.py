"""
The main python file. Write all your scenes here!
"""

from basics import in_dev, scene, play

# The @scene tells the code that this is a new scene
# The ctx stores the game data.
@scene
def name_scene(ctx):
    """
This function stores the name inside ctx so that it can be used by later.
    """
    name = input("Enter your name: ")
    ctx["name"] = name
    yes_no = input("Would you like to be a kettle? ").lower()
    if yes_no == 'y':
        return yes_kettle_scene
    return no_kettle_scene

@scene
def yes_kettle_scene(ctx):
    """
Please contribute to this scene!
    """
    in_dev()

@scene
def no_kettle_scene(ctx):
    """
Please contribute to this scene!
    """
    in_dev()

play(name_scene)
