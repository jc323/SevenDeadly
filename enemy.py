# Enemy
import pygame
from entity import Entity
from spriteAnimation import SpriteImSeqs

class Enemy(Entity):
    def __init__(self, currentLevel):
        Entity.__init__(self)
        
        self.currentLevel = currentLevel


        # Loading in spriteSheets
        self.gluttonsheet = pygame.image.load("images/enemies/GluttonSpriteSheet.png")
        self.gangstersheet = pygame.image.load("images/enemies/GangsterSpriteSheet.png")
        self.hulasheet = pygame.image.load("images/enemies/HulaSpriteSheet.png")
        self.wrathsheet = pygame.image.load("images/enemies/EnvySpriteSheet.png")
        self.pridesheet = pygame.image.load("images/enemies/PrideSpriteSheet.png")

        
        self.gangsterIms = SpriteImSeqs(self.gangstersheet, (1, 3), (192, 240), (0, 0))
        self.gluttonIms = SpriteImSeqs(self.gluttonsheet, (2, 2), (205, 202), (0, 0))
        self.hulaIms = SpriteImSeqs(self.hulasheet, (1, 3), (192,240), (0, 0))
        self.wrathIms = SpriteImSeqs(self.wrathsheet, (1, 2), (192,240), (0, 0))
        self.prideIms = SpriteImSeqs(self.pridesheet, (2, 2), (189, 218), (0, 0))

        #pride
        self.prideIms.createAction("walkRight", [i for i in range(3)])
        self.prideIms.createAction("walkLeft", [i for i in range(3)])
        self.prideIms.createAction("jump", [1])
        #ganster
        self.gangsterIms.createAction("walkRight", [i for i in range(3)])
        self.gangsterIms.createAction("walkLeft", [i for i in range(3)])
        self.gangsterIms.createAction("jump", [1])
        
        #glutton
        self.gluttonIms.createAction("rollRight", [i for i in range(4)])
        self.gluttonIms.createAction("rollLeft", [i for i in range(4)])

        #hula
        self.hulaIms.createAction("dance", [i for i in range(3)])

        #wrath
        self.wrathIms.createAction("whip", [i for i in range(2)])


        #actions
        #pride
        self.prideJump = self.prideIms.action("jump")
        self.prideWalkRight = self.prideIms.action("walkRight")
        self.prideWalkLeft = self.prideIms.action("walkLeft")
        #gangster
        self.gangsterJump = self.gangsterIms.action("jump")
        self.gangsterWalkRight = self.gangsterIms.action("walkRight")
        self.gangsterWalkLeft = self.gangsterIms.action("walkLeft")
        #glutton
        self.rollRight = self.gluttonIms.action("rollRight")
        self.rollLeft = self.gluttonIms.action("rollLeft")
        #hula
        self.hulaDance = self.hulaIms.action("dance")
        #wrath
        self.wrathWhip = self.wrathIms.action("whip")

        self.enemyImages = {'1': pygame.transform.scale(self.rollRight[1], (40,40)),             # Gluttony
                            '2': pygame.transform.scale(self.gangsterWalkRight[1], (40,40)),     # Greed
                            '3': pygame.transform.scale(self.hulaDance[1], (40,40)),                 # Lust
                            '4': None,                                                           # Sloth
                            '5': pygame.transform.scale(self.wrathWhip[1], (40,40)),             # Envy
                            '6': pygame.transform.scale(self.prideWalkRight[1], (40,40)),        # Pride
                            '7': None,                                                           # Wrath
                            '8': None }                                                          # Devil
        
        #Done with all spriting

        self.image = pygame.transform.scale(self.enemyImages[str(currentLevel)], (50,50))

        self.health = None
        self.attack = None
        self.speed = None
        self.attackType = None

        self.Xpos = None
        self.Ypos = None
        #ANIMATE Using self.enemyIms.action("")

        self.constructAux()

    def constructAux(self):
        if self.currentLevel == 1: # Gluttony
            self.health = 40
            self.attack = 10
            self.speed = 10
            self.attackType = "Roll"
            
        elif self.currentLevel == 2: # Greed
            self.health = 50
            self.attack = 5
            self.speed = 5
            self.attackType = "Shoot"
            
        elif self.currentLevel == 3: # Lust
            self.health = 80
            self.attack = 0
            self.speed = 0
            self.attackType = "Sing"
            
        elif self.currentLevel == 4: # Sloth
            print "Error, should not be enemies on this level"
            
        elif self.currentLevel == 5: # Envy
            self.health = 100
            self.attack = 20
            self.speed = 10
            self.attackType = "Whip"
            
        elif self.currentLevel == 6: # Pride
            self.health = 50
            self.attack = 5
            self.speed = 10
            self.attackType = "Shoot"
            
        elif self.currentLevel == 7: # Wrath
            print "Error, should not be enemies on this level"
            
        elif self.currentLevel == 8: # Devil
            print "Error, should not be enemies on this level"

    def attackHit(self, target):
        target.setHealth(target.getHealth() - self.attack)

    def attackLaunch(self, player):            
        if self.attackType == "Roll":
            print player.getXpos()
            print self.Xpos, "self"
            if player.getXpos() < self.Xpos: # Roll left
                self.rect.right -= self.speed/2
            elif playet.getXpos() > self.Xpos:
                self.rect.left += self.speed/2
                
        elif self.attackType == "Shoot":
            bullet = Bullet(attack, target, self.Xpos, self.Ypos, self.direction)
            
        elif self.attackType == "Sing":
            if target.getXpos() > self.Xpos: # Pull target left 5 pixels
                target.bumpXpos(-5)
            else:                            # Pull target right 5 pixels
                target.bumpXpos(5)
                
        elif self.attackType == "Whip":
            if collision: #collision between self and target
                self.attackHit(target)
            
    def update(self):
        pass
        #update position

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

    def getLoc(self):
        return (self.Xpos, self.Ypos)

    def bumpXpos(self, xChange): # if hit by enemy, move over
        self.Xpos += xChange

    def createRect(self):
        self.rect = pygame.Rect(self.Xpos, self.Ypos, 22, 20)
