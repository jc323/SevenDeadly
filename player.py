# Player
from spriteAnimation import SpriteImSeqs
from entity import Entity
import pygame
import math
from bullet import Bullet

class Player(Entity):
    def __init__(self):
        Entity.__init__(self)
        
        #load spriteSheet for player
        self.jonSpriteSheet = pygame.image.load("images/JonSpriteSheet.png")
        self.jonSpriteSheet.convert_alpha()
        self.jonIms = SpriteImSeqs(self.jonSpriteSheet, (2,2), (189, 218), (0, 0))
        
        self.rect = None
        
        #createActions
        self.jonIms.createAction("walkRight", [i for i in range(3)])
        self.jonIms.createAction("walkLeft", [i for i in range(3)])
        self.jonIms.createAction("jump", [3])

        #actions
        self.jonWalkRight = self.jonIms.action("walkRight")
        self.jonWalkLeft = self.jonIms.action("walkLeft")
        self.jonJump = self.jonIms.action("jump")

        self.health = 100
        self.attack = 10
        self.speed = 8
        self.attackType = "Shoot"
        self.direction = "left"

        self.Xpos = None
        self.Ypos = None
        self.yvel = 0
        self.xvel = 0
        
        self.FPS = 60
        self.cycletime = 0
        self.newnr = 0
        self.oldnr = -1
        self.picnr = 0
        self.interval = .075
        self.onGround = True
        self.leftPress = False

        
        self.image = pygame.transform.scale(self.jonWalkRight[1],(50,50))
        self.mask = pygame.mask.from_surface(self.image)

    def attackLaunch(self):
        bullet = Bullet(self.attack, self.rect.left, self.rect.top+10, self.direction)
        return bullet

    def update(self, up, left, right, platforms, screen, bg, direction, picnr):
        
        if up and not(left or right):
            if self.onGround:
                self.yvel -= 13
                self.onGround = False
                self.animate(self.jonJump, picnr, self.direction)
                
        if right:
            self.xvel = self.speed
            self.animate(self.jonWalkRight, picnr, self.direction)
            if self.onGround and up:
                self.yvel -= 13
                self.onGround = False
            if up:
                self.animate(self.jonJump, picnr, self.direction)

        if left:
            self.xvel = -self.speed
            self.animate(self.jonWalkLeft, picnr, self.direction)
            if self.onGround and up:
                self.yvel -= 13
                self.onGround = False
            if up:
                self.animate(self.jonJump, picnr, self.direction)

        if self.onGround == False:
            self.yvel += .95

        if not (left or right):
            self.xvel = 0

        #increment in x and y direction
        self.rect.left += self.xvel
                        
        self.oldnr = self.newnr

        self.collide(self.xvel, 0, platforms)

        self.rect.top += self.yvel
        
        #assume we are in air
        self.onGround = False

        #do collisions
        self.collide(0, self.yvel, platforms)

        self.direction = direction
                    
    #update position
    #potentially animate here
    def animate(self, action, picnr, direction):
        if direction == False:
            self.picture = pygame.transform.scale(action[picnr], (50,50))
            self.image = pygame.transform.flip(self.picture, 1, 0)
        else:
            self.image = pygame.transform.scale(action[picnr], (50,50))


    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if self.rect.colliderect(p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.yvel = 0

                    
    def setHealth(self, newHealth):
        self.health = newHealth

    def setSpeed(self, newSpeed):
        self.speed = newSpeed

    def setAttack(self, newAttack):
        self.attack = newAttack

    def setXpos(self, Xpos):
        self.Xpos = Xpos

    def setYpos(self, Ypos):
        self.Ypos = Ypos

    def getW(self):
        return self.jonIms.getW()

    def getH(self):
        return self.jonIms.getH()
    
    def getHealth(self):
        return self.health

    def getSpeed(self):
        return self.speed

    def getAttack(self):
        return self.attack

    def getXpos(self):
        return self.Xpos

    def getYpos(self):
        return self.Ypos

    def getDirection(self):
        return self.direction

    def getDist(self, enemy):       
        xDist = self.rect.left - enemy.getXpos()
        yDist = self.rect.top - enemy.getYpos()
        dist = math.sqrt((xDist*xDist)+(yDist*yDist))
        return math.fabs(dist)
    
    def bumpXpos(self, xChange): # if hit by enemy or siren sing, move over
        self.Xpos += xChange

    def createRect(self):
        self.rect = pygame.Rect(self.Xpos, self.Ypos, 32, 50)
