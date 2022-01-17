import pygame

class Calculation:

	def __init__(self, image):
		self.image = image

	def calculate(self):
		spritesheet_size = self.image.get_rect().size
		spritesheet_cols = 8
		spritesheet_rows = 4
		sprite_size = (spritesheet_size[0]/spritesheet_cols, spritesheet_size[1]/spritesheet_rows)
		#creating sprite array taking only line of interest
		line_interest = 4 - 1 
		sprites = []
		for items in range(spritesheet_cols):
			left, top, width, height = sprite_size[0], line_interest * sprite_size[1], sprite_size[0], sprite_size[1]
			left = items * left
			sprites.append((left,top,width,height))
		return((sprites, sprite_size[1], spritesheet_cols))
