import pygame
import os

class Entity(pygame.sprite.Sprite):
    
    def __init__(self, position, location_of_assets, assets, scale):
        super().__init__()
        self.pos_x, self.pos_y = position
        self.is_animating = False
        self.sprites = []

        #location_of_assets = ["Assets", "PNG"]
        #assets = ["playerShip2_orange.png"]

        # TODO: Seperate the creation of the sprites
        # Appending Idle assets for player, unpacking for location of sprite
        for asset in assets:
            self.sprites.append(
                pygame.transform.scale(
                    pygame.image.load(os.path.join(*location_of_assets, asset)),
                    scale,
                )
            )

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = position
        

    """Animates the Idle animation for the sprite"""

    def animate(self):
        self.is_animating = True

    """Updates the sprite for the player, speed is an float between 0 and 1 to
    control speed of animation."""

    def update(self, speed):
        if self.is_animating:
            self.current_sprite += speed
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            self.image = self.sprites[int(self.current_sprite)]

            self.rect = (self.pos_x, self.pos_y)