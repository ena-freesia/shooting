import pygame
from pygame.locals import *
import sys

def main():

    (w,h) = (400, 400)
    (x,y) = (w//2, h//2)
    pygame.init()
    pygame.display.set_mode((w,h))
    pygame.display.set_caption("Test")  
    screen = pygame.display.get_surface()

    clock = pygame.time.Clock()
    
    running = True

    while running:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        keystates = pygame.key.get_pressed()
        if keystates[K_ESCAPE]:
            running = False
        if keystates[K_LEFT]:
            x -= 1
        if keystates[K_RIGHT]:
            x += 1
        if keystates[K_UP]:
            y -= 1
        if keystates[K_DOWN]:
            y += 1

        if x < 0:
            x = 0
        if x > w:
            x = w
        if y < 0:
            y = 0
        if y > h:
            y = h

        screen.fill((0,20,0,0))
        pygame.draw.circle(screen, (0,200,0), (x,y), 5)
        pygame.display.update() #flip()
        
        clock.tick(30)
          
    pygame.quit()            
                        
if __name__ == "__main__":
    main()