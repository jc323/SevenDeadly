import pygame
import random
import os

class SpriteImSeqs(object):
    """Class to contain sprite-sheet, ordered hashes of sprite-images,
       and hashes with lists of sprites indexed by action names"""

    def __init__(self, spriteSheet, rowcols, sizeXY, initOffset = (0, 0)):
        """takes sprite sheet, number of rows and columns, image size (x, y),
            and initial offset for the upper left corner of the first sprite image"""
        self.imhash = {}
        self.sprites = spriteSheet
        numrows, numcols = rowcols
        self.w, self.h = sizeXY
        i = 0
        for row in range(numrows):
            for col in range(numcols):
                self.imhash[i] = self.sprites.subsurface((col*self.w, row*self.h, self.w, self.h))
                self.imhash[row, col] = self.imhash[i]
                i += 1
        self.actions = {}

    def createAction(self, act, imList):
        """create an action named 'act' with images designated in imList
            imList is either list of integers or list of (row, col) tuples"""
        if type(imList[0]) == type(()):
            # process list of (row, col) values
            self.actions[act] = [ self.imhash[row, col] for row, col in imList]
        else:
            # process list of ints
            self.actions[act] = [ self.imhash[i] for i in imList ]

    def action(self, act):
        try:
            return self.actions[act]
        except:
            print "error: action", act, "not found"
            return []
        
    def getW(self):
        return self.w
    def getH(self):
        return self.h
        
    
