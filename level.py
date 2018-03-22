# Level Class
# Set the enemies, bosses, etc. for current level
import pygame
from enemy import Enemy
from powerUp import PowerUp
from boss import Boss

class Level(object):
    def __init__(self, currentLevel):
        self.currentLevel = currentLevel
        
        self.musicList = {'1': pygame.mixer.Sound('sounds/songs/gluttony.wav'),   # Gluttony
                          '2': pygame.mixer.Sound('sounds/songs/greed.wav'),      # Greed
                          '3': pygame.mixer.Sound('sounds/songs/lust.wav'),       # Lust
                          '4': pygame.mixer.Sound('sounds/songs/sloth.wav'),      # Sloth
                          '5': pygame.mixer.Sound('sounds/songs/envy.wav'),       # Envy
                          '6': pygame.mixer.Sound('sounds/songs/pride.wav'),      # Pride
                          '7': pygame.mixer.Sound('sounds/songs/wrath.wav'),      # Wrath
                          '8': pygame.mixer.Sound('sounds/songs/boss.wav')}       # Devil

        self.backgroundImages = {'1': pygame.image.load('images/backgrounds/gluttony.jpg'), # Gluttony
                                 '2': pygame.image.load('images/backgrounds/greed.jpg'),    # Greed
                                 '3': pygame.image.load('images/backgrounds/lust.jpg'),     # Lust
                                 '4': pygame.image.load('images/backgrounds/sloth.jpg'),    # Sloth
                                 '5': pygame.image.load('images/backgrounds/envy.jpg'),     # Envy
                                 '6': pygame.image.load('images/backgrounds/pride.jpg'),    # Pride
                                 '7': pygame.image.load('images/backgrounds/wrath.jpg'),    # Wrath
                                 '8': pygame.image.load('images/backgrounds/devil.jpg')}    # Devil
                      
        self.enemies = None
        self.powerUps = None
        self.song = None
        self.backGround = None
        self.boss = None

    def setLevelObs(self, currentLevel): # Sets the unique number of enemies, powerUps, and Boss
        self.song = self.musicList[str(currentLevel)]
        self.backGround = self.backgroundImages[str(currentLevel)]

        if self.currentLevel == 1: # Gluttony
            self.enemies = [Enemy(currentLevel), Enemy(currentLevel), Enemy(currentLevel), Enemy(currentLevel), Enemy(currentLevel)] #5 enemies
            self.powerUps = [PowerUp(currentLevel), PowerUp(currentLevel)] # 2 power ups
            self.boss = Boss(currentLevel)
                                 
        elif self.currentLevel == 2: # Greed
            self.enemies = [Enemy(currentLevel), Enemy(currentLevel), Enemy(currentLevel)] # 3 enemies
            self.powerUps = [PowerUp(currentLevel), PowerUp(currentLevel), PowerUp(currentLevel)] # 3 power ups
            self.boss = Boss(currentLevel)
                                 
        elif self.currentLevel == 3: # Lust
            self.enemies = [Enemy(currentLevel), Enemy(currentLevel), Enemy(currentLevel)] # 3 enemies
            self.powerUps = [PowerUp(currentLevel)] # 1 power up
            self.boss = Boss(currentLevel)
                                 
        elif self.currentLevel == 4: # Sloth
            self.enemies = None # no enemies
            self.powerUps = [PowerUp(currentLevel), PowerUp(currentLevel), PowerUp(currentLevel), PowerUp(10)] # 4 power ups
            self.boss = Boss(currentLevel)
                                 
        elif self.currentLevel == 5: # Envy
            self.enemies = [Enemy(currentLevel), Enemy(currentLevel), Enemy(currentLevel), Enemy(currentLevel), Enemy(currentLevel)] # 5 enemies
            self.powerUps = [PowerUp(currentLevel), PowerUp(currentLevel)] # 2 power ups
            self.boss = Boss(currentLevel)
                                 
        elif self.currentLevel == 6: # Pride
            self.enemies = [Enemy(currentLevel), Enemy(currentLevel), Enemy(currentLevel),
                            Enemy(currentLevel), Enemy(currentLevel), Enemy(currentLevel)] # 6 enemies
            self.powerUps = [PowerUp(currentLevel), PowerUp(currentLevel)] # 2 power ups
            self.boss = Boss(currentLevel)
                                 
        elif self.currentLevel == 7: # Wrath
            self.enemies = None # No enemies
            self.powerUps = None # No power ups
            self.boss = Boss(currentLevel)
                                 
        elif self.currentLevel == 8: # Devil
            self.enemies = None # No enemies
            self.powerUps = None # No power ups
            self.boss = Boss(currentLevel) 
                                 
    def getBoss(self):
        return self.boss

    def getSong(self):
        return self.song

    def getEnemies(self):
        return self.enemies

    def getPowerUps(self):
        return self.powerUps

    def getBackground(self):
        return self.backGround
