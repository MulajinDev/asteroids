import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")

    #initialize pygame
    pygame.init()

    #set up screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #create clock and deltatime
    clock = pygame.time.Clock()
    dt = 0

    #create groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    #add to groups
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)

    #create player
    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    #create asteroidField
    asteroidField = AsteroidField()

    #main game loop
    while True:
        #check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #update updatables
        updatables.update(dt)

        #check collisions
        for asteroid in asteroids:
            if asteroid.collide(player1):
                print("Game over!")
                return

        #fill screen black
        screen.fill(000000)

        #draw drawables
        for drawable in drawables:
            drawable.draw(screen)

        #refresh display
        pygame.display.flip()

        #set to REFRESH_RATE fps
        dt = clock.tick(REFRESH_RATE) / 1000


if __name__ == "__main__":
    main()
