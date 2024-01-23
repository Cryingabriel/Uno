import pygame
import math
from pygame.math import Vector2
from Uno import screen
from cards import card

class Player():
    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos, ypos)
        self.cards = []
    
    def draw(self):
        pygame.draw.rect(screen, (200,200,200), (80,80,80,80))

    
    def inventory(self):
        pass

    def move(self, mousex, mousey):
        self.pos.x = mousex
        self.pos.y = mousey