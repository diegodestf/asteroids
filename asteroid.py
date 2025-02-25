import pygame, random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

asteroids = pygame.sprite.Group()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()


class Asteroid(CircleShape):
    containers = (asteroids, updatable, drawable)

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white",(self.position.x, self.position.y), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)

            first_asteroid_velocity = self.velocity.rotate(angle)
            second_asteroid_velocity = self.velocity.rotate(-angle)


            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)

            new_asteroid.velocity = first_asteroid_velocity * 1.5
            new_asteroid_two.velocity = second_asteroid_velocity * 1.5


    


