import pygame
import os

ENEMY_WIDTH, ENEMY_HEIGHT = 91, 91
BLUE_UFO_HEALTH, BLUE_UFO_ARMOR = 100, 0

class Enemy(pygame.sprite.Sprite):
    """Initializing player sprites with pygame.image.load"""
    def __init__(self, pos_x, pos_y, assets):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_animating = False
        self.sprites = []
        
        # Sprite that is being used for the Enemy class
        #assets = ['ufoBlue.png']
        
        # Appending Idle assets for Enemy
        for asset in assets:
            self.sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'PNG', asset)), (ENEMY_WIDTH, ENEMY_HEIGHT)))
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = (pos_x, pos_y)
        #self.rect.topleft = [pos_x, pos_y]
    
    
    def animate(self):
        """Animates the Idle animation for the sprite"""
        self.is_animating = True

    
    def update(self, speed):
        """Updates the sprite animation, speed is an float between 0 and 1 to control speed of animation."""
        if self.is_animating == True:
            self.current_sprite += speed
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            self.image = self.sprites[int(self.current_sprite)]
            
            self.rect = (self.pos_x, self.pos_y)
            
            
class BlueEnemyUFO(Enemy):
    """Weakest UFO class requires position and its assets to draw inheriting from the enemy class."""
    def __init__(self, pos_x, pos_y, assets = ['ufoBlue.png']):
        super(BlueEnemyUFO, self).__init__(pos_x, pos_y, assets)
        
    def animate(self):
        """Animates the Idle animation for the sprite"""
        super(Enemy, self).animate()
    
    def update(self, speed):
        """Updates the sprite for UFO, speed is an float between 0 and 1 to control speed of animation."""
        super(Enemy, self).update()