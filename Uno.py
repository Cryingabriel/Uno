import pygame
from pygame.math import Vector2
screen = pygame.display.set_mode((800,800))
import Players
from Players import Player
clock = pygame.time.Clock()
mousepos = (0,0)

playerPos = Vector2(400,400)
mexit = False
timer = 30


player1 = Player(playerPos.x, playerPos.y)

while not mexit:
    clock.tick(60)

    for event in pygame.event.get(): #Event queue
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            mexit =  True
    
    if timer == 0:
        pass
    


    
    #Render Section
    screen.fill((2,20,200))

    player1.move(playerPos.x, playerPos.y)

    pygame.display.flip()

pygame.quit()