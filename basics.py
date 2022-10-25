import functools

class GameData:
	played_scenes = []

def in_dev(ctx):
	print("===NEXT SCENE IS IN DEVELOPMENT===")

def ended(ctx):
	print("===THE GAME HAS ENDED===")

def scene(func):
	@functools.wraps(func)
	def wrapper_scene(ctx):
		ctx.played_scenes.append(func.__name__)
		next_scene = func(ctx)
		if next_scene == None:
			return ended
		return next_scene
	wrapper_scene.scene = True
	return wrapper_scene

def play(scene):
	ctx = GameData()
	while hasattr(scene, "scene"):
		scene = scene(ctx)

	scene(ctx)
	print("You played: " + str(GameData.played_scenes))
