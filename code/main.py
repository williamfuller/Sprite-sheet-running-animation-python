import pygame
import time
from Animation import Animate
from sprite_info_calculator import SpriteInfoCalculator
from config import sprite_sheet

pygame.init()

sprite_img = pygame.image.load(f"res/{sprite_sheet['name']}")

sprite_info = SpriteInfoCalculator(sprite_img, sprite_sheet["row"], sprite_sheet["frame_count"])
sprites_coordinates = sprite_info.get_sprite_coordinates()

#Sprite sheet info 
current_image = 0
start_frame = time.time()

#pygame below
WIDTH = 800
HEIGHT = 600
running_men = []

for items in range (int(HEIGHT / sprite_info.sprite_height)): #the num is the size of each sprite
	running_man = Animate(items, sprite_info.sprite_height)
	running_men.append(running_man)

BLACK = (255, 255, 255)
sprite_pos = (0, 0)
animation_display = pygame.display.set_mode((WIDTH,HEIGHT))

running = True
while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False 

	animation_display.fill(BLACK)

	for index in running_men: #makes the men appear and run 
		current_image = index.speed(sprite_sheet["frame_count"], current_image, start_frame)
		sprite_pos = index.move()
		animation_display.blit(sprite_img, sprite_pos, sprites_coordinates[current_image])

	pygame.display.update() 

pygame.quit()
quit()