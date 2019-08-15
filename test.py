import sys
import pygame
from pygame.locals import *


class Point:
    """座標"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y, s):
        self.x += x * s
        self.y += y * s


class Circle(Point):
    """円"""
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def hit(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        dr = self.r + other.r
        return dr ** 2 > dx ** 2 + dy ** 2

class Player(Circle):
    """自機"""
    def __init__(self, x, y):
        super().__init__(x, y, 5)

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 200, 0), (self.x, self.y), self.r)

class Bullet(Circle):
    """弾"""
    def __init__(self, x, y):
        super().__init__(x, y, 3)

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 200), (self.x, self.y), self.r)

class Enemy(Circle):
    """敵"""
    def __init__(self, x, y):
        super().__init__(x, y, 10)

    def draw(self, screen):
        pygame.draw.circle(screen, (200, 0, 0), (self.x, self.y), self.r)

def main():

    (w,h) = (1280, 720)
    pygame.init()
    pygame.display.set_mode((w,h))
    pygame.display.set_caption("Test")
    screen = pygame.display.get_surface()

    clock = pygame.time.Clock()

    running = True

    player = Player(w//2, h//2)
    enemys = []
    bullets = []
    counter = 0
    while running:

        counter += 1

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        keystates = pygame.key.get_pressed()
        if keystates[K_ESCAPE]:
            running = False

        # move player+
        key_x = 0
        key_y = 0
        if keystates[K_LEFT]:
            key_x -= 1
        if keystates[K_RIGHT]:
            key_x += 1
        if keystates[K_UP]:
            key_y -= 1
        if keystates[K_DOWN]:
            key_y += 1

        player.move(key_x, key_y, 5)

        # 弾生成
        if keystates[K_SPACE] and counter%5 == 0:
            bullets.append(Bullet(player.x, player.y))
        
        # 敵生成
        if counter%10 == 0:
            if len(enemys) > 5:
                continue
            enemys.append(Enemy(w, 50))

        if player.x < 0:
            player.x = 0
        if player.x > w:
            player.x = w
        if player.y < 0:
            player.y = 0
        if player.y > h:
            player.y = h

        # 弾消去
        for bullet in bullets:
            bullet.move(0, -1, 10)
            if bullet.y < 0:
                bullets.remove(bullet)

        # 敵消去
        for enemy in enemys:
            enemy.move(-1, 0, 5)
            if enemy.x < 0:
                enemys.remove(enemy)

        for bullet in bullets:
            for enemy in enemys:
                if bullet.hit(enemy):
                    bullets.remove(bullet)
                    enemys.remove(enemy)
        
        


        screen.fill((0,20,0,0))
        player.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        for enemy in enemys:
            enemy.draw(screen)
        pygame.display.update() #flip()

        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()