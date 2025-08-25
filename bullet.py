import pygame
from circleshape import CircleShape
from constants import PLAYER_SHOT_SPEED, SHOT_RADIUS



class Shot(CircleShape):
    def __init__(self, x, y, direction):
        super().__init__(x, y, SHOT_RADIUS)
        # direction should be a normalized Vector2
        self.velocity = direction * PLAYER_SHOT_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt