"""
This file contains a collection of utility
functions
"""
import pygame

def is_animation_running(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    return running

def generate_next_frame(frame, background_color, sprites, sprite_sheet, sprite_img, sprite_coordinates):
    frame.fill(background_color)

    for sprite in sprites:
        animation_frame_index = sprite.get_animation_frame_index(sprite_sheet["frame_count"])
        sprite_pos = sprite.update_sprite_postion()
        frame.blit(sprite_img, sprite_pos, sprite_coordinates[animation_frame_index])
    return frame