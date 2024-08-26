# Spritesheet.py built-in addon @pygstudio
# Version 1.0

import pygame


class SpriteSheet:
    def __init__(self, image_path, spritesheet_details) -> None:
        self.image_path = image_path
        self.spritesheet_details = spritesheet_details
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image.lock()

    def get_sprite(self, name):
        return self.image.subsurface(self.spritesheet_details[name])

    def render(self, name, surface, rect):
        surface.blit(self.image, rect, self.spritesheet_details[name])

class CostumeSpriteSheet:
    def __init__(self, image_path, sprite_size, init_number = 0) -> None:
        self.image_path = image_path
        self.sprite_size = sprite_size
        self.current_costume = init_number
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image_size = self.image.get_size()
        self.image.lock()

    def get_sprite_position(self, number):
        return number % self.image_size[0], number // self.image_size[0]

    def get_sprite_rect(self, number):
        return *self.get_sprite_position(number), *self.image_size

    def render(self, surface, rect):
        surface.blit(self.image, rect, self.get_sprite_rect(self.current_costume))

    def set_costume(self, number):
        self.current_costume = number

    def get_costume(self):
        return self.current_costume

    def get_sprite(self, number):
        return self.image.subsurface(self.get_sprite_rect(number))