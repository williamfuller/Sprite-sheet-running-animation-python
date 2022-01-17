import random
import time
class Animate():
	def __init__(self, start_level, sprite_size):
		self.fps = random.randrange(4, 26, 2) #calculated here needed for later
		self.start_level = start_level
		self.sprite_size = sprite_size
		self.sprite_x = 0

	def speed(self, noi, current_image, start_frame):
		self.noi = noi
		self.current_image = current_image
		self.start_frame = start_frame
		current_image = int((time.time() - start_frame) * self.fps % noi)
		return(current_image)

	def move(self):
		sprite_y = self.start_level * self.sprite_size	#45 is the total height of sprite
		self.sprite_x += 0.05*(self.fps)
		if self.sprite_x > 800:
			self.sprite_x = 0
			self.fps = random.randrange(4, 26, 2)
		return((self.sprite_x, sprite_y))
