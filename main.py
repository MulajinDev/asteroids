import pygame

from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #initialize pygame
    pygame.init()

    #set up screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #create clock and deltatime
    clock = pygame.time.Clock()
    dt = 0

    #create player
    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    #main game loop
    while True:
        #check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #fill screen black
        screen.fill(000000)

        #draw player
        player1.draw(screen)

        #refresh display
        pygame.display.flip()

        #set to REFRESH_RATE fps
        dt = clock.tick(REFRESH_RATE) / 1000


if __name__ == "__main__":
    main()
