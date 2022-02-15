import pygame
import time
from animator import Animator
from sprite_info_calculator import SpriteInfoCalculator
from config import sprite_sheet, animation_window

pygame.init()

sprite_img = pygame.image.load(f"res/{sprite_sheet['name']}")

sprite_info = SpriteInfoCalculator(sprite_img, sprite_sheet["animation_row"], sprite_sheet["frame_count"], sprite_sheet["row_count"])
sprites_coordinates = sprite_info.get_sprite_coordinates()

# initializing animation
current_image = 0
start_frame = time.time()

#pygame below
WIDTH = animation_window["width"]
HEIGHT = animation_window["height"]
sprites = []

for display_row in range (int(HEIGHT / sprite_info.sprite_height)): 
	sprite = Animator(display_row, sprite_info.sprite_height, animation_window["width"])
	sprites.append(sprite)

BLACK = (255, 255, 255)
sprite_pos = (0, 0)
animation_display = pygame.display.set_mode((WIDTH,HEIGHT))

running = True
while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False 

	animation_display.fill(animation_window["background_color"])

	for sprite in sprites:
		animation_frame_index = sprite.get_animation_frame_index(sprite_sheet["frame_count"], start_frame)
		sprite_pos = sprite.update_sprite_postion()
		animation_display.blit(sprite_img, sprite_pos, sprites_coordinates[animation_frame_index])

	pygame.display.update() 

pygame.quit()
quit()