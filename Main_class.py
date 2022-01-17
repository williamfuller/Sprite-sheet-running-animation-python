import pygame
import time
from Animation import Animate
from Calculate import Calculation

#sorting sprites and game initialise
def main():
	pygame.init()
	img = pygame.image.load('player-spritemap-v9.png')
	sprite_calcuation = Calculation(img)
	sprites_info = sprite_calcuation.calculate()
	sprites = sprites_info[0]
	sprite_height = sprites_info[1]
	#Sprite sheet info 
	noi = sprites_info[2] #number of images
	current_image = 0
	start_frame = time.time()

	#pygame below
	WIDTH = 800
	HEIGHT = 600
	running_men = []

	for items in range (int(HEIGHT / sprites_info[1])): #the num is the size of each sprite
		running_man = Animate(items, sprites_info[1])
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
			current_image = index.speed(noi, current_image, start_frame)
			sprite_pos = index.move()
			animation_display.blit(img, sprite_pos, sprites[current_image])

		pygame.display.update() 

	pygame.quit()
	quit()

if __name__ == '__main__':
	main()
