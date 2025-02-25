import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

shots = pygame.sprite.Group()

class Shot(CircleShape):
    containers = (shots,)
    def __init__(self, x, y, radius):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white",(self.position.x, self.position.y), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt