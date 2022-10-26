# Writing a new scene

Below are a few example scenes we'll be looking at:

```py
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

```

All scenes are functions, but not all functions are scenes. We know that a function is a scene if it has `_scene` at the end of its name and it takes `ctx` as an argument. Thus, when writing a new scene, be sure to declare the function the same way.

`ctx` is a dictionaray which stores the game data. Initially it isn't much (it only stores the scenes played in `played_scenes`). However, scenes are allowed to modify and add to the `ctx` however way they like (**BUT DON'T CHANGE `played_scenes`**). When `ctx` is added to, such as in in `name_scene` with the line `ctx["name"] = name`, future scenes are allowed to use the data.

The docstring (the multiline comment under the function header) is also required. While it's not code, it notifies other programmers two things:

1) Who wrote the scene (real name and Discord name is preferred)
2) How `ctx` is changed

The former is so that we know who to ask if we want something changed. The latter allows the programmer to know what data they can utilize without having to closely read the code.

After following the above steps, you can write the scene as you like! Whether it be tic tac toe, trivia, or a multiple choice text adventure game, you can do it as long as the transition from the previous scene makes sense. At the end of the scene, if nothing is returned, then the game ends. If another scene is returned (`return yes_kettle_scene`), then it'll automatically be called by the game loop. **Please do not call scenes yourself!**

# Guidelines and Rules

## Rules

- Include a docstring (the multi-line comment right under the function header)
- The docstring should have:
	- Either your real name or Discord name (or both)
	- If you update `ctx`, include a brief description of the update
- Only update `main.py`. If you wish to update `basics.py`, talk to the Officers first!
- After creating your scene(s), create the scenes in development
	- Do not put your name on the development scenes
	- Write `in_dev()` for their body
- Prior to uploading, your Python program should work without crashes!
- **Do not call other scenes. Make sure you *return* the scene!**

## Guidelines

- Create small scenes
- Create development scenes so others can contribute
- Try not to take days or weeks writing scenes
- Upload your code often!

# How to Upload Your Code

We encourage you to contribute by writing the scenes which are in development, which are functions that don't have a name beneath their function name, or their body simply says `in_dev()`.

## Method 1 (Easiest)

Download the code by clicking the green `Code` button at the top of the site and clicking `Download ZIP`. Modify the code and when you're done, let the officers know in the Discord channel and send them the files.


## Method 2 (Preferred)
For this method, a **GitHub account is required, and we expect you to know how to use Git**. Thus, we won't go into too many details, but the basic steps are:

- Create a fork
- Commit your changes
- Create a Pull Request on our repo
- Merge our branch with your fork's branch

And the officers handle the rest from there.
