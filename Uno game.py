import pygame
from pygame.math import Vector2
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800,800))
mousepos = (0,0)

playerPos = Vector2(mousepos[0], mousepos[1])
mexit = False
timer = 30


while not mexit:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mexit =  True
    
    if timer == 0:
        pass
    


    
    
    
    
    
    
    
    
    #Render Section
    screen.fill((0,0,0))

pygame.quit()