import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,'white', self.position,2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            second = self.velocity.rotate(random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            firt_ast = Asteroid(self.position[0], self.position[1], new_radius)
            firt_ast.velocity.rotate(random_angle) 
            sec_ast = Asteroid(self.position[0], self.position[1], new_radius)
            sec_ast.velocity.rotate(random_angle) 



            




