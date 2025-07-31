import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"grey",self.position,self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        #kill self
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            #I'm small, no split needed
            return
        else:
            #I'm not small, split me
            #get a split angle
            new_dir = random.uniform(20,50)

            #set velocities for new asteroids
            a1_velo = self.velocity.rotate(new_dir)
            a2_velo = self.velocity.rotate(0-new_dir)

            #get a new asteroid size
            a_rad = self.radius - ASTEROID_MIN_RADIUS

            #spawn 2 asteroids
            a1 = Asteroid(self.position.x, self.position.y, a_rad)
            a2 = Asteroid(self.position.x, self.position.y, a_rad)

            #set asteroid velocities and increase speed
            a1.velocity = a1_velo * 1.2
            a2.velocity = a2_velo * 1.2