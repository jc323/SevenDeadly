# Fire
import pygame
from pygame.locals import *
from entity import *
from spriteAnimation import SpriteImSeqs


class Fire(Entity):
    def __init__(self, x, y):
    	"""Handles the creation and images of spikes in the game class;
        they are the A in level creation."""
        Entity.__init__(self)
        self.fireSpriteSheet = pygame.image.load("images/FireSpriteSheet.png")
        self.fireSpriteSheet.convert_alpha()
        self.flameIms = SpriteImSeqs(self.fireSpriteSheet, (3, 5), (58, 136), (0, 0))

        self.flameIms.createAction("burn", [i for i in range(15)])
        self.flames = self.flameIms.action("burn")
                                                           
        self.image = pygame.transform.scale(self.flames[1], (22, 32))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = Rect(x, y, 23, 32)
