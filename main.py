import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Shot
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    dt = 0

    Player.containers = [updatable, drawable]
    Asteroid.containers = [asteroids, updatable, drawable]
    AsteroidField.containers = [updatable]
    Shot.containers = [shots, updatable, drawable]

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        for asteroid in list(asteroids):
            if player.collide(asteroid):
                print("Game over!")
                pygame.quit()
                return
            for shot in list(shots):
                if shot.collide(asteroid):
                    asteroid.split()
                    shot.kill()
                    break

        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()