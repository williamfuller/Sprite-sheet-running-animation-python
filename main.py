import pygame
from src.animator import Animator
from src.sprite_info_calculator import SpriteInfoCalculator
from config import sprite_sheet, animation_window
import src.utils as utils

pygame.init()
animation_display = pygame.display.set_mode((animation_window["width"],animation_window["height"]))

sprite_img = pygame.image.load(f"res/{sprite_sheet['name']}")
sprite_info = SpriteInfoCalculator(sprite_img, sprite_sheet["animation_row"], sprite_sheet["frame_count"], sprite_sheet["row_count"])
sprite_coordinates = sprite_info.get_sprite_coordinates()
sprites = []

for display_row in range (int(animation_window["height"] / sprite_info.sprite_height)): 
	sprite = Animator(display_row, sprite_info.sprite_height, animation_window["width"])
	sprites.append(sprite)


running = True
while running:

	running = utils.is_animation_running(running)

	animation_display.fill(animation_window["background_color"])
	animation_display = utils.generate_next_frame(animation_display, 
												  animation_window["background_color"], 
												  sprites, sprite_sheet, 
												  sprite_img, 
												  sprite_coordinates
												)

	pygame.display.update() 

pygame.quit()