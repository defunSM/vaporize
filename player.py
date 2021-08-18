import pygame
import os

PLAYER_WIDTH, PLAYER_HEIGHT = 87, 105

class Player(pygame.sprite.Sprite):
    """Initializing player sprites with pygame.image.load"""
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_animating = False
        self.sprites = []
        
        assets = ['playerShip2_orange.png']
        
        # Appending Idle assets for player
        for asset in assets:
            self.sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'PNG', asset)), (PLAYER_WIDTH, PLAYER_HEIGHT)))
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = (pos_x, pos_y)
        #self.rect.topleft = [pos_x, pos_y]
    
    """Animates the Idle animation for the sprite"""
    def animate(self):
        self.is_animating = True

    """Updates the sprite for the player, speed is an float between 0 and 1 to control speed of animation."""
    def update(self, speed):
        if self.is_animating == True:
            self.current_sprite += speed
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            self.image = self.sprites[int(self.current_sprite)]
            
            self.rect = (self.pos_x, self.pos_y)