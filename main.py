import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)
    
    Asteroid.containers = (asteroids, updatable, drawable, )

    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for asteroid_shape in asteroids:
            if (asteroid_shape.check_collisions(player)):
                print("Game over")
                return
            for shot in shots:
                if (asteroid_shape.check_collisions(shot)):
                    asteroid_shape.split()
            
        
        screen.fill("black")
        
        for drawable_player in drawable:
            drawable_player.draw(screen)
            
        pygame.display.flip()


        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()