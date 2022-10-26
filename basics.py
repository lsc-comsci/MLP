"""
Don't update this code without telling the officers!
The minimalist framework to manage the different scenes
"""

import functools

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

def scene(func):
    """
Decorator for scene functions.
Stores the function in played_scenes when ran
Also assigns the "scene" attr to the function
    """
    @functools.wraps(func)
    def wrapper_scene(ctx):
        if "played_scenes" in ctx:
            ctx["played_scenes"].append(func.__name__)
        else:
            ctx["played_scenes"] = [func.__name__]
        return func(ctx)
    wrapper_scene.scene = True
    return wrapper_scene

def play(curr_scene):
    """
Starts the game!
    """
    ctx = {}
    while hasattr(curr_scene, "scene"):
        curr_scene = curr_scene(ctx)

    ended()
    print("You played: " + str(ctx["played_scenes"]))
