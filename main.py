from basics import in_dev, scene, play

@scene
def name_scene(ctx):
	name = input("Enter your name: ")
	ctx.name = name
	yn = input("Would you like to be a kettle? ").lower()
	if yn == 'y':
		return yes_kettle_scene
	else:
		return no_kettle_scene

@scene
def yes_kettle_scene(ctx):
	in_dev()

@scene
def no_kettle_scene(ctx):
	in_dev()

play(name_scene)
