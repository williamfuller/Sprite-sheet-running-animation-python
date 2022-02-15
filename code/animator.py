import random
import time

class Animator():
	def __init__(self, display_row, sprite_height, window_max_width):
		self.animation_speed = self.__get_random_aniation_speed()

		self.display_row = display_row
		self.sprite_size = sprite_height
		self.sprite_x = 0

		self.window_max_width = window_max_width

	def __get_random_aniation_speed(self):
		return random.randrange(4, 26, 2)

	def get_animation_frame_index(self, frame_count, start_frame):
		return int((time.time() - start_frame) * self.animation_speed % frame_count)

	def update_sprite_postion(self):
		sprite_y = self.display_row * self.sprite_size
		self.sprite_x += 0.01* self.animation_speed

		if self.sprite_x > self.window_max_width:
			self.sprite_x = 0
			self.animation_speed = self.__get_random_aniation_speed()

		return (self.sprite_x, sprite_y)
