import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_MOVE_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_CD
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        #set rotation
        self.rotation = 0
        self.shot_cd = 0

    #determine triangle shape for player
    def triangle(self):
        #define triangle directions
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        #calculate corners
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]
    
    #draw player to a screen
    def draw(self, screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)
    
    #rotate player direction
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    #move player position
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_MOVE_SPEED * dt

    #shoot
    def shoot(self):
        if self.shot_cd > 0:
            return
        shot = Shot(self.position.x,self.position.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shot_cd = PLAYER_SHOOT_CD

    #update player and handle keystrokes
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(0-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(0-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        #update shot_cd
        if self.shot_cd > 0:
            self.shot_cd -= dt