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
Ricardo Bernabe (BallinMonkey12)
    """
    print("=== Something Behind You ===")

    print("You wake up and go to the restroom")
    print('Look in the mirror? Yes / No')

    answer_yes = ['Yes', 'Y', 'yes', 'y']
    answer_no = ['No', 'N', 'no', 'n']

    ans1= input(">>")

    if ans1 in answer_yes:
        print("You feel Something grab you")

        print("Do you break free?")

        ans2= input(">>")

        if ans2 in answer_yes:
            print('You run back to bed and pretend it was a dream')

        elif ans2 in answer_no:
            print("Something chokes you to death")
            print("=== You died ===")
        else:
            print('=== You died ===')

def no_kettle_scene(ctx):
    """
Please contribute to this scene!
    """
    in_dev()

play(name_scene)
