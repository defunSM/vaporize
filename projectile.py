from dataclasses import dataclass
from player import Player

@dataclass
class Projectile(Player):
    pos_x: int = super().pos_x
    pos_y: int = super().pos_y
    damage: int = 1
    
    def animate(self):
        pass
    
    def update(self, speed):
        pass