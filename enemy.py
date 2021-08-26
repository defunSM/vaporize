import pygame
import os
from typing import List
from abc import ABC, abstractmethod
from entity import Entity

ENEMY_WIDTH, ENEMY_HEIGHT = 91, 91
BLUE_UFO_HEALTH, BLUE_UFO_ARMOR = 100, 0


# TODO: Add attributes that are specific to enemy classes 
class Enemy(Entity):
    """Enemy class sprites"""

            
class BlueUFO(Enemy):
    """Weakest UFO class requires position and its assets to draw inheriting from the enemy class."""
    def __init__(self):
        BLUEUFO_LOCATION = (400, 50)
        BLUEUFO_ASSET_LOCATION = ["Assets", "PNG"]
        BLUEUFO_SPRITES = ['ufoBlue.png']
        UFO_SCALE = (ENEMY_WIDTH, ENEMY_HEIGHT)
        
        super(BlueUFO, self).__init__(BLUEUFO_LOCATION, BLUEUFO_ASSET_LOCATION, BLUEUFO_SPRITES, UFO_SCALE)
        
    def animate(self):
        """Animates the Idle animation for the sprite"""
        super(BlueUFO, self).animate()
    
    def update(self, speed):
        """Updates the sprite for UFO, speed is an float between 0 and 1 to control speed of animation."""
        super(BlueUFO, self).update(speed)