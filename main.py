# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x, y, PLAYER_RADIUS)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()
    Shot.containers = (shot_group, updatable, drawable)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for draws in drawable:
            draws.draw(screen)
        updatable.update(dt)
        for obj in asteroids:
            for shot in shot_group:
                if shot.check_collision(obj):
                    shot.kill()
                    obj.split()
        for obj in asteroids:
            if obj.check_collision(player):
                print("Game over!")
                sys.exit()
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
