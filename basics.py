"""
Don't update this code without telling the officers!
The minimalist framework to manage the different scenes
"""

def in_dev():
    """
In development! Please contribute to scenes that are in development.
    """
    print("===NEXT SCENE IS IN DEVELOPMENT===")

def ended():
    """
The function is called once the game runs out of scenes
    """
    print("===THE GAME HAS ENDED===")

def play(curr_scene):
    """
Starts the game!
    """
    ctx = {"played_scenes": []}
    while curr_scene:
        ctx["played_scenes"].append(curr_scene.__name__)
        curr_scene = curr_scene(ctx)

    ended()
    print("You played: " + str(ctx["played_scenes"]))
