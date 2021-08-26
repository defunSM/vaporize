import pygame
import os
from entity import Entity

PLAYER_WIDTH, PLAYER_HEIGHT = 87, 105


class Player(Entity):
    """Initializing player sprite from the Entity class"""
    def __init__(self):
        PLAYER_SCALE = (PLAYER_WIDTH, PLAYER_HEIGHT)
        super(Player, self).__init__((50, 650), ["playerShip2_orange.png"], PLAYER_SCALE)
        
    
        
