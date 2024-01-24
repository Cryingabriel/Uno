import pygame
import math
from pygame.math import Vector2
from cards import card

screen = pygame.display.set_mode((800,800))
class Player():
    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos, ypos)
        self.cards = []
    
    def draw(self):
        pygame.draw.rect(screen, (200,200,200), (self.pos.x, self.pos.y,80,80))

    
    def inventory(self):
        pass

    def move(self, mouse):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mouse = event.pos
                if mouse[0] > self.pos.x:
                    self.pos.x = mouse[0] - 40
                elif mouse[0] < self.pos.x:
                    self.pos.x = mouse[0] -40
                
                if mouse[1] > self.pos.y:
                    self.pos.y = mouse[1] -40
                elif mouse[1] < self.pos.y:
                    self.pos.y = mouse[1] - 40
        