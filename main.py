"""
The main python file. Write all your scenes here!
"""

from basics import in_dev, play

#lists for use in functions when needed
answer_yes = ['Yes', 'Y', 'yes', 'y']
answer_no = ['No', 'N', 'no', 'n']

# The ctx stores the game data.
def name_scene(ctx):
    """
Amr Ojjeh (amrojjeh)
ctx[name] stores the name of the player
    """
    name = input("Enter your name: ")
    ctx["name"] = name
    yes_no = input("Would you like to be a kettle? ").lower()
    if yes_no in answer_yes:
        return yes_kettle_scene
    return no_kettle_scene



def yes_kettle_scene(ctx):
    """
Ricardo Bernabe (BallinMonkey12)
    """
    print("=== Something Behind You ===")

    print("You wake up and go to the restroom")
    print('Look in the mirror? Yes / No')

   # answer_yes = ['Yes', 'Y', 'yes', 'y']
   # answer_no = ['No', 'N', 'no', 'n']

    ans1= input(">>")

    if ans1 in answer_yes:
        print("You feel Something grab you")

        print("Do you break free?")

        ans2= input(">>")

        if ans2 in answer_yes:
            print('You run back to bed and pretend it was a dream...')
            return back_to_bed

        elif ans2 in answer_no:
            print("Something chokes you to death")
            print("=== You died ===")

            goback = input("Go back one scene? ")
            if goback in answer_yes:
                return yes_kettle_scene
    else:
        return no_look_mirror

def back_to_bed(ctx):
    """Julio amaya"""

    print("You realize it wasn't a dream and are in great danger. What do you do?")
    print("""1) Call the police
2) Get out of bed and fight it
3) Stay in the bed until you rust out and die
4) Pray to god""")
    anss = int(input(">>> "))
    match anss:
        case 1:
            print("Oops! You have no fingers so there's no way you can call the police!")
            return back_to_bed
        case 2:
            print("You tried your best to fight this dark evil but you were crushed.")
            print("=== You died ===")

            goback = input("Go back one scene? ")
            if goback in answer_yes:
                return back_to_bed
        case 3:
            print("You have successfully rusted out.")
            print("=== You died ===")
            
            goback = input("Go back one scene? ")
            if goback in answer_yes:
                return back_to_bed
        case 4:
            print("""Kettle Jesus showed up from the heavens through your roof, you can barely see him! he is too bright!
He saved you. He destroyed the dark evil that was hunting you.""")
            return jesus_saved_you

def jesus_saved_you(ctx):
    in_dev()


def no_look_mirror(ctx):
    in_dev()



def no_kettle_scene(ctx):
    """
Please contribute to this scene!
ctx["max_hunger"] is the days the chicken can last without food (src: google)
ctx["hunger"] is the days the chicken lasted without food
ctx["age"] is the age of the chicken days
    """
    ctx["max_hunger"] = 5
    ctx["hunger"] = 0
    ctx["age"] = 0
    print("Since you're not a kettle, you're a chicken.")
    yes_no = input("Do you eat grain? ")
    if "y" in yes_no:
        return eats_grain_scene
    return not_normal_chicken_scene


def eats_grain_scene(ctx):
    """
Written during the club
    """

    """julio amaya"""

    print("""You're just a boring chicken.
After a few weeks you'll served in KFC.""")

    goback = input("Go back one scene? ")
    if goback in answer_yes:
        return no_kettle_scene


def not_normal_chicken_scene(ctx):
    """
Written during the club
    """
    print("Now you must eat milk, but how are you going to turn the milk to solid state?. What do you do?")
    print("""1) Wait until night
2) Call the butcher
3) Wait for the milk to expire
4) Use dark magic""")
    num = int(input("Enter a number: "))
    match num:
        case 1:
            return wait_until_night_scene
        case 2:
            return butcher_scene
        case 3:
            if "wait_milk_expire" in ctx["played_scenes"]:
                return chicken_dead
            return wait_milk_expire                
        case 4:
            return dark_magic_scene

def butcher_scene(ctx):
    """julio amaya"""

    print("The butcher was hungry and ate you.")
    print('=== You died ===')

    goback = input("Go back one scene? ")
    if goback in answer_yes:
        return not_normal_chicken_scene


def dark_magic_scene(ctx):
    """julio amaya"""
    
    print("""You spawned a jug of milk by flapping a wing, then shot a bean of energy from you beak 
that turned the milk into trunks that you can eat!
You have found that you have dark magic powers!! what is your next step?""")
    print("""1) Turn yourself into a human
2) Fly away to the moon
3) Spawn a portal and Go to the harry potter world for chickens
4) Spawnn more milk""")
    ansss = int(input(">>> "))

    match ansss:
        case 1:
            print("""Your magic isn't fully developed, you turned into a hybrid of chicken and human.
The butcher thought you were an alien and butchered you.""")
            print("=== You died ===")


def wait_until_night_scene(ctx):
    in_dev()

def wait_milk_expire(ctx):
    """
Written during the club
    """
    ctx["age"] += 2
    ctx["hunger"] += ctx["age"]
    print(f"You've waited for {ctx['age']} days and you're hungry. It's possible you may expire before the milk. What do you do?")
    return not_normal_chicken_scene

def chicken_dead(ctx):
    print("The chicken was fried by the sun and it was served in KFC next to cheese.")

play(name_scene)
