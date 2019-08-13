import pygame
from pygame.locals import *
import sys

class Player:
    """自機"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y
        
class Bullet:
    """弾"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

def main():

    (w,h) = (400, 400)
    pygame.init()
    pygame.display.set_mode((w,h))
    pygame.display.set_caption("Test")  
    screen = pygame.display.get_surface()

    clock = pygame.time.Clock()
    
    running = True

    player = Player(w//2, h//2)
    bullets = []
    while running:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        keystates = pygame.key.get_pressed()
        if keystates[K_ESCAPE]:
            running = False
        if keystates[K_LEFT]:
            player.x -= 1
        if keystates[K_RIGHT]:
            player.x += 1
        if keystates[K_UP]:
            player.y -= 1
        if keystates[K_DOWN]:
            player.y += 1

        if keystates[K_SPACE]:
            bullets.append(Bullet(player.x, player.y))

        if player.x < 0:
            player.x = 0
        if player.x > w:
            player.x = w
        if player.y < 0:
            player.y = 0
        if player.y > h:
            player.y = h

        for bullet in bullets:
            bullet.y -= 1
            if bullet.y < 50:
                bullets.remove(bullet)

        screen.fill((0,20,0,0))
        pygame.draw.circle(screen, (0,200,0), (player.x,player.y), 5)
        for bullet in bullets:
            pygame.draw.circle(screen, (0, 0, 200), (bullet.x, bullet.y), 3)
        pygame.display.update() #flip()
        
        clock.tick(30)
          
    pygame.quit()            
                        
if __name__ == "__main__":
    main()