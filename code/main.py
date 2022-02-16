import pygame
from animator import Animator
from sprite_info_calculator import SpriteInfoCalculator
from config import sprite_sheet, animation_window
import utils

pygame.init()
animation_display = pygame.display.set_mode((animation_window["width"],animation_window["height"]))

sprite_img = pygame.image.load(f"res/{sprite_sheet['name']}")
sprite_info = SpriteInfoCalculator(sprite_img, sprite_sheet["animation_row"], sprite_sheet["frame_count"], sprite_sheet["row_count"])
sprites_coordinates = sprite_info.get_sprite_coordinates()
sprites = []

for display_row in range (int(animation_window["height"] / sprite_info.sprite_height)): 
	sprite = Animator(display_row, sprite_info.sprite_height, animation_window["width"])
	sprites.append(sprite)


running = True
while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False 

	animation_display.fill(animation_window["background_color"])

	for sprite in sprites:
		animation_frame_index = sprite.get_animation_frame_index(sprite_sheet["frame_count"])
		sprite_pos = sprite.update_sprite_postion()
		animation_display.blit(sprite_img, sprite_pos, sprites_coordinates[animation_frame_index])

	pygame.display.update() 

pygame.quit()