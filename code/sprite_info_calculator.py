class SpriteInfoCalculator:

	def __init__(self, sprite_sheet, animation_row, frame_count, row_count):
		self.frame_count = frame_count
		self.animation_row = animation_row

		self.spritesheet_width, self.spritesheet_height = sprite_sheet.get_rect().size
		self.sprite_width ,self.sprite_height =  round(self.spritesheet_width/frame_count), round(self.spritesheet_height/row_count)
		print(self.sprite_width ,self.sprite_height )

	def get_sprite_coordinates(self):
		sprite_coordinates = []

		for frame in range(self.frame_count):
			sprite_coordinates.append((self.sprite_width * frame,
								(self.animation_row-1) * self.sprite_height, 
								self.sprite_width, 
								self.sprite_height))

		return sprite_coordinates