# Power Up
import pygame
from pygame.locals import *
from entity import Entity

class PowerUp(Entity):
    def __init__(self, currentLevel):
        Entity.__init__(self)
        self.currentLevel = currentLevel
        self.powerUpSound = pygame.mixer.Sound('sounds/powerUp.wav')

        self.powerUpImages = {'1': pygame.image.load('images/powerUps/gluttony.png'),   # Gluttony
                              '2': pygame.image.load('images/powerUps/greed.png'),      # Greed
                              '3': pygame.image.load('images/powerUps/lust.png'),       # Lust
                              '4': pygame.image.load('images/powerUps/sloth.png'),      # Sloth
                              '5': pygame.image.load('images/powerUps/envy.png'),       # Envy
                              '6': pygame.image.load('images/powerUps/pride.png'),      # Pride
                              '10': pygame.image.load('images/powerUps/slothKiller.png')}#Sloth kill    
                              

        self.image = pygame.transform.scale(self.powerUpImages[str(currentLevel)], (30, 30))
        self.mask = pygame.mask.from_surface(self.image)
        self.image.convert_alpha()
        self.rect = None

        self.Xpos = None
        self.Ypos = None

    # When power up collected, apply appropriate stat boost to player
    def collected(self, player):
        if self.currentLevel == 1: # Gluttony
            player.setHealth(player.getHealth()+10) # 10 HP boost
        if self.currentLevel == 2: # Greed
            player.setAttack(player.getAttack()+10) # 10 Attack boost
        if self.currentLevel == 3: # Lust
            player.setSpeed(player.getSpeed()+5)    # 5 Speed decrease (slow sirens' pull)
        if self.currentLevel == 4: # Sloth
            player.setSpeed(player.getSpeed()+1)    # 5 Speed increase (outrun sloth quicker)
        if self.currentLevel == 5: # Envy
            player.setAttack(player.getAttack()+10) # 10 Attack boost
        if self.currentLevel == 6: # Pride
            player.setHealth(player.getHealth()+10) # 10 HP boost
        if self.currentLevel == 7: # Wrath
            print "Error, should not be power up on this level"
        if self.currentLevel == 8: # Devil
            print "Error, should not be power up on this level"
        if self.currentLevel == 10: # Special one-shot power up for sloth end
            player.setAttack(player.getAttack()+100000)

    def getXpos(self):
        return self.Xpos

    def getYpos(self):
        return self.Ypos

    def setXpos(self, Xpos):
        self.Xpos = Xpos

    def setYpos(self, Ypos):
        self.Ypos = Ypos

    def createRect(self):
        self.rect = pygame.Rect(self.Xpos, self.Ypos, 22, 20)
