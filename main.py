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
    """ justin kondratenko """
    import time

    for i in range(3):
        time.sleep(1)
        print(".", end="", flush=True)
    time.sleep(1)
    print("(The Mirror took great offense to that)")

    time.sleep(3)
    print("THE MIRROR NOW CHALLENGES YOU TO A SMASH BROS ULTIMATE DUEL!")
    print("Do you accept his challenge? Yes / No")
    ans1= input(">>")

    if ans1 in answer_yes:
        return smash_bros_duel
    elif ans1 in answer_no:
        print("idk what to tell you, like were you expecting to survive The Mirror crashing on top of you or something?")
        print("=== You died ===")
        goback = input("Go back one scene? ")
        if goback in answer_yes:
            return no_look_mirror
    
def smash_bros_duel(ctx):
    """ justin kondratenko """
    import time
    
    print("You pick up your controller and turn on your switch, showing no remorse to The Mirror.")
    print("Pick your fighter:")
    fighters=["Mario","Donkey Kong","Link","Samus","Yoshi","Kirby","Fox","Pickachu"]
    index=1
    for fighter in fighters:
        print(str(index) + ")" + fighter)
        index+=1

    fighter_chosen=fighters[int(input("Enter a number: "))-1] # -1 because index of array starts at 0
    delay=2
    print("You've chosen "+fighter_chosen+" and the mirror also chose "+fighter_chosen+" (because get it, it's a mirror, ikr funny let's move on).")
    time.sleep(delay*2)

    match_progression=["The Match as begun","\nBoth of you are evenly matched","\nBoth of you are about to deal the final blow"]
    for phrase in match_progression:
        print(phrase, end="", flush=True)
        for i in range(3):
            time.sleep(1)
            print(".", end="", flush=True)
        time.sleep(delay)
        
    print("\nCan you be the one to finish him first?")
    time.sleep(delay)
    for i in range(3):
        time.sleep(1)
        print(str(3-i))
    time.sleep(delay/2)
    input("Press B -> Enter! ")
    
    print("YOU HIT HIM WITH A STRONG SPECIAL ATTACK, DEFEATING THE MIRROR AND PUTTING IT BACK WHERE IT BELONGS!")
    print("After a hard day of showing The Mirror who's boss, shall you go downstairs to found out what The Rock is cooking? Yes / No")
    ans1=input(">>")
    if ans1 in answer_yes:
        return yes_rock_cooking
    if ans1 in answer_no:
        return no_rock_cooking

def yes_rock_cooking(ctx):

    print ("The Rock is cooking spaghetti for the dinner. He is struggling with the receipe he found online. \n\n Would you like to help him with cooking or sit at the dinning table playing game?")
    ans = input ("\nYes for help.\nNo for playing game.\n>> ")
    
    if ans in answer_yes:
        return help_cooking
    return playing_game

def help_cooking (ctx):

    def selection():
        ingredients = ["Fresh garlic", "Hot pepper flakes", "Red Wine", "Herbs", "Cheese"]

        i= 1
        for ingredient in ingredients: 
            print (str(i)+ ")" + ingredient)
            i+=1

        answer = ingredients[int (input(">>"))-1]

        if answer == "Herbs":
            print("You have chosen" + answer + """ to add to the Rock's spaghetti.
            CONGRATULATION!!!! 
            That's the exact missing ingredient for the perfect spaghetii.""")
            in_dev()    
        elif answer == "Fresh garlic":
            print ("The Rock has already added "+ answer + ". It is fortunate that you did not ruin his spaghetti." )
            choose_again = input ("Would you like to select another ingredient?")
            if choose_again in answer_yes: 
                selection()
            in_dev()
        elif answer == "Hot pepper flakes":
            print("The Rock has already added " + answer + " . You ruined his speghetti with this strong spice")
            import time 
            for i in range(5):
                time.sleep(0.5)
                print(".", end="", flush = True)
            print("The Rock got SUPER ANGRY and punch you in the face.")
            print("=== You died ===")
            in_dev()
        elif answer == "Red Wine":
            print ("The Rock has already added "+ answer + ". It is fortunate that you did not ruin his spaghetti." )
            choose_again = input ("Would you like to select another ingredient?")
            if choose_again in answer_yes: 
                selection()
            in_dev()
        elif answer == "Cheese":
            print ("The Rock has already added "+ answer + ". It is fortunate that you did not ruin his spaghetti." )
            choose_again = input ("Would you like to select another ingredient?")
            if choose_again in answer_yes: 
                selection()
            in_dev()
                        
    print ("\nYou realize that he forgot to add one important ingredient in his spaghetii. You decide to help.\n\nSelect your ingredient:")
    selection()

    
def playing_game (ctx):
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

def escape_the_matrix(ctx):
    """
Truc Le (Chuck Le)
    """
    import time 

    for i in range(3):
        time.sleep(1)
        print(".", end="", flush=True)

    print("""First action you take: 

            1) Join a computer sciene club for references.
            2) Learn from a Indian guy on YouTube.
            3) Enrolling in a university in Vietnam since it's cheaper. Majoring in ComSci.""")

    act = int(input(">>> "))
    match act:
            case 1:
                print("You tride your best from zero. Being a kettle made it challenging, but you also gained lots of knowledge. \n\nYou earned yourself the first prize, the club's signature hat.")
                time.sleep(5)
                print("\nUnfortunately, after ~3 months being in the club. You fell distached and the club was not how you imagined it would be.\n\nYou decided to left the club.")
                time.sleep(5)
                print("\nAs a purnishment, the club president casted a curse on who dare to abandon the way. It was written in the club's constitution, but who reads it anyways...\n\nYou pray to God")
                time.sleep(5)
                print("\nWILL HE ANSWER...???")
                say = input(">>>> ")
                if say in answer_yes:
                    return jesus_saved_you
                if say in answer_no:
                    print("The curse made you turn into something totally different from a kettle")
                    print("\n****************************************")
                    time.sleep(4)
                    return no_kettle_scene
            case 2:
                print("You find out the rumors were true. Those Indian YouTubers are really helpful.\n\nAt the end of the video, there is a redeem link. Will you click on it?")
                rep = input(">>> ")
                if rep in answer_yes:
                    print("You gained a coupon to another online lesson:")
                    time.sleep(3)
                    print("\nHow To Become A Millionaire While Doing Almost Nothing")
                    time.sleep(4)
                    print("\nYou followed just to go bankrupt and had to start over again. Some *lesson* you learned.")
                    print("\n****************************************")
                    return escape_the_matrix
                if rep in answer_no:
                    print("Makes sense. You are better at containing tea than clicking on any link.\n\nYou started to doubt greatly about the path you have chosen.")
                    print("\n****************************************")
                    time.sleep(3)
                    return escape_the_matrix
            case 3:
                print("You went to far...\nYou got trauma...\nYou craved a spa. The Rock's SPAghetti")
                time.sleep(4)
                print("\n****************************************")
                return yes_rock_cooking

def no_rock_cooking(ctx):
    """
Truc Le (Chuck Le)
    """
    import time 

    for i in range(3):
        time.sleep(1)
        print(".", end="", flush=True)

    print("You realize why went through all that fighting when you can be the rules maker of your own game? Escaping the maxtrix")
    print(" ====> You decided to be the first kettle to become a game developer")
    return escape_the_matrix

play(name_scene)
