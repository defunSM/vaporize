from dataclasses import dataclass
from player import Player
from abc import ABC, abstractmethod
from enemy import Entity, Enemy

# TODO: May not be needed and could just use Entity
class Projectile(Entity):
    """Abstract class used for building various projectiles emitted from Player, Enemy classes as such have similar abstract methods of animate and update for drawing and rendering the sprite of the projectile"""
    @abstractmethod
    def animate(self):
        pass
    
    @abstractmethod
    def update(self):
        pass

# TODO: Decide what the missle class should be responsible for
# TODO: Change up the Entity class so that pos_x and pos_y can be accessed globally
# TODO: How to handle sprites and movement of the missiles
# TODO: Handle how to destroy a missile after a certain time or on contact

PLAYER_MISSILE_WIDTH = 20
PLAYER_MISSLE_HEIGHT = 20

class PlayerMissle(Entity):
    def __init__(self, player):
        PLAYER_MISSLE_SCALE = (PLAYER_MISSILE_WIDTH, PLAYER_MISSLE_HEIGHT)
        super(PlayerMissle, self).__init__((player.pos_x, player.pos_y), ["Assets", "PNG", "Lasers"],["laserBlue01.png", "laserBlue02.png", "laserBlue03.png", "laserBlue04.png","laserBlue05.png", "laserBlue06.png", "laserBlue07.png"], PLAYER_MISSLE_SCALE)
        self.is_animating = True
        
    def update(self, speed):
        if self.is_animating:
            self.current_sprite += speed
            self.pos_y -= 5
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            self.image = self.sprites[int(self.current_sprite)]

            self.rect = (self.pos_x, self.pos_y)
        
class EnemyMissle(Projectile):
    def animate(self):
        pass
    
    def update(self, speed):
        pass