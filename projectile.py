from dataclasses import dataclass
from player import Player
from abc import ABC, abstractmethod
from enemy import Entity, Enemy

# TODO: May not be needed and could just use Entity
class Projectile(ABC):
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
@dataclass
class PlayerMissle(Projectile):
    pos_x: int = super().pos_x
    pos_y: int = super().pos_y
    damage: int = 1
    
    def animate(self):
        pass
    
    def update(self, speed):
        pass

@dataclass
class EnemyMissle(Projectile):
    pos_x: int = super().pos_x
    pos_y: int = super().pos_y
    damage: int = 1
    
    def animate(self):
        pass
    
    def update(self, speed):
        pass