import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, 2)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        random_angle = random.uniform(20, 50)
        vector_one = self.velocity.rotate(random_angle)
        vector_two = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        if new_radius < ASTEROID_MIN_RADIUS:
            self.kill()
            return
        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_one.velocity = vector_one * 1.2
        asteroid_two.velocity = vector_two * 1.2
        asteroid_one.add(Asteroid.containers)
        asteroid_two.add(Asteroid.containers)
        self.kill()

    def update(self, dt):
        self.position += (self.velocity * dt)

