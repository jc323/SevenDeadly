# Driver

import pygame
from pygame import *
from sys import exit
import time as pause

# import other class objects
from entity import Entity
from player import Player
from platform import Platform
from powerUp import PowerUp
from fire import Fire
from boss import Boss
from enemy import Enemy
from level import Level

# camera for scrolling
from camera import *

pygame.init()

############################################################################################
# Title Screen
def titleScreen():
    title = True # True while the game waits for the user to make a choice
    
    music = pygame.mixer.Sound('sounds/songs/titleSong.wav')
    music.play()
    
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH) # information comes from the camera class
    screen_rect = screen.get_rect() # get the screen rect
    pygame.display.set_caption("Seven Deadly") # Window caption
    background_image = pygame.transform.scale(pygame.image.load("images/intro/title.png"),
                                             (WIN_WIDTH, WIN_HEIGHT)) # Load the title background

    # All of the button images
    play = pygame.image.load('images/intro/play.png')
    play2 = pygame.image.load('images/intro/play2.png')
    tut = pygame.image.load('images/intro/tutorial.png')
    tut2 = pygame.image.load('images/intro/tutorial2.png')
    
    # Blit the initial images to the screen; order: PLAY, TUT
    screen.blit(background_image, (0,0))
    b1 = screen.blit(play, (WIN_WIDTH/2.45, WIN_HEIGHT*.6))
    b2 = screen.blit(tut, (WIN_WIDTH/2.8, WIN_HEIGHT*.8))

    # We want the cursor on the main menu and tutorial screen.
    pygame.mouse.set_visible(True)

    # Keep the title screen looping while the user makes a decision;
    # checks for clicking within a image to perform the action (color changes when scrolled over)
    while title == True:
        for e in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if e.type == QUIT: # "X"ed out of the game
                raise SystemExit()
            if e.type == MOUSEMOTION: # If the user scrolls over one of the buttons change to the alternate color
                if b1.collidepoint(pos):
                    screen.blit(play2, (WIN_WIDTH/2.45, WIN_HEIGHT*.6))
                elif b2.collidepoint(pos):
                    screen.blit(tut2, (WIN_WIDTH/2.8, WIN_HEIGHT*.8))
                else: # Show the original background image if the user is not scrolled over the image
                    screen.blit(play, (WIN_WIDTH/2.45, WIN_HEIGHT*.6))
                    screen.blit(tut, (WIN_WIDTH/2.8, WIN_HEIGHT*.8))
            if e.type == MOUSEBUTTONDOWN:
                if b1.collidepoint(pos):
                    title = False
                    music.stop()

                    main() # Click to start the game
                if b2.collidepoint(pos):
                    tutorial(music) # Click to go to the tutorial screen

        pygame.display.update() # Update the display

################################################################################################################
# Tutorial Menu
def tutorial(music):
    tutstatus = True # True if still on tutorial screen

    # Display Settings
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    screen_rect = screen.get_rect()
    pygame.display.set_caption("Seven Deadly")
    background_image = pygame.transform.scale(pygame.image.load("images/intro/tutscreen.png"), (WIN_WIDTH, WIN_HEIGHT)) # Tutorial background
    screen.blit(background_image, (0,0))

    # Menu buttons
    menu = pygame.image.load('images/intro/play.png')
    menu2 = pygame.image.load('images/intro/play2.png')

    m1 = screen.blit(menu, (WIN_WIDTH*.8, WIN_HEIGHT*.8))

    # Continue running while the status is True
    while tutstatus == True:
        for e in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if e.type == QUIT: # "X"ed out of the game
                raise SystemExit()
            if e.type == MOUSEMOTION:
                if m1.collidepoint(pos): # Scrolling over the Main Menu button, so change the image so the user knows they are on it
                    screen.blit(menu2, (WIN_WIDTH*.8, WIN_HEIGHT*.8))
                else:
                    screen.blit(menu, (WIN_WIDTH*.8, WIN_HEIGHT*.8)) # Change back to the normal image since the user is no longer on it
            if e.type == MOUSEBUTTONDOWN:
                if m1.collidepoint(pos):
                    music.stop()
                    main() # Clicked to start the game
        pygame.display.update()

#################################################################################
# Game Loop
def main():
    currentLevel = 1
    
    while currentLevel < 9:

        timer = pygame.time.Clock()
        screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH) # Set the screen information
        screen_rect = screen.get_rect()
        pygame.mouse.set_visible(False)
        cutScreenImage = pygame.transform.scale(pygame.image.load("images/cutScreens/" + str(currentLevel) +".png"), (WIN_WIDTH, WIN_HEIGHT))
        
        screen.blit(cutScreenImage, (0,0))
        pygame.display.update()
        pygame.time.delay(3000)
        
        
        # Load Level class and store info
        level = Level(currentLevel)
        level.setLevelObs(currentLevel)
        song = level.getSong()
        background = level.getBackground()
        boss = level.getBoss()
        enemies = level.getEnemies()
        powerUps = level.getPowerUps()

        # Create Player
        player = Player()
        if currentLevel == 4:
            player.setSpeed(4)
        # Load music
        song.play()
        print "song Starteddd"

        # Load Level Objects with platforms
        """KEY FOR LEVELS
        P = Platform
        C = player starting position
        F = Fire
        E = Enemy
        B = Boss
        U = Power Up
        """
        platforms = []
    
        entities = pygame.sprite.Group()
        powerUpSprites = pygame.sprite.Group()
        fires = pygame.sprite.Group()
        enemySprites = pygame.sprite.Group()
        bossSprite = pygame.sprite.Group()
        bulletSprites = pygame.sprite.Group()

        x = 0
        y = 0

        level = open('levels/level' + str(currentLevel) + '.txt', 'r')

        powerCounter = 0
        enemyCounter = 0
        
        for row in level:
            for col in row:
                if col == "P":
                    p = Platform(x, y) # Place a platform at the given x,y
                    platforms.insert(0, p) # Insert it into the platforms list
                    entities.add(p) # Add to entities so it appears on screen
                if col == "C":
                    player.setXpos(x)
                    player.setYpos(y) # Set the player along with the x,y of the starting position
                    player.createRect()
                    entities.add(player)
                if col == "F":
                    fire = Fire(x, y) # Load a fire at the x,y found 
                    entities.add(fire) # Add the fire to the entities
                    fires.add(fire) # Add the fire to the spike sprite group for collison purposes
                if col == "U":
                    pUp = powerUps[powerCounter] # Load a power up image at the given x,y
                    pUp.setXpos(x)
                    pUp.setYpos(y)
                    pUp.createRect()
                    entities.add(pUp) # Power up to the entities
                    powerUpSprites.add(pUp) # add power up to the powerUps sprite group
                    powerCounter+=1
                if col == "E":
                    enemy = enemies[enemyCounter] # Load an enemy image at the given x,y
                    enemy.setXpos(x)
                    enemy.setYpos(y)
                    enemy.createRect()
                    entities.add(enemy) # Add the enemy to the entities
                    enemySprites.add(enemy) # add enemy to the enemies sprite group
                    enemyCounter+=1
                if col == "B":
                    boss.setXpos(x) # Load a boss image at the given x,y
                    boss.setYpos(y)
                    boss.createRect()
                    entities.add(boss) # Add the boss to the entities
                    bossSprite.add(boss) # add boss to the boss sprite group
            
            
                x += 32
            y += 32
            x = 0
        
        # Load Background for level
        background_rect = background.get_rect()

        total_level_width  = len('level'[0])*32
        total_level_height = len('level')*32
        camera = Camera(complex_camera, total_level_width, total_level_height)

        
        bossDead = False
        nextLevel = True
        playerAlive = True

        #animation needs
        FPS = 60
        cycletime = 0
        newnr = 0
        oldnr = -1
        picnr = 0
        interval = .075

        #interaction needs
        buttonPressed = False
        upPressed = False
        rightPressed = False
        leftPressed = False
        spacePressed = False
        direction = True #True means right
        
        while bossDead == False and playerAlive == True:
            pygame.display.set_caption("Seven Deadly | " + " | FPS: " + str(int(timer.get_fps())))
            asize = ((screen_rect.w // background_rect.w + 1) * background_rect.w, (screen_rect.h // background_rect.h + 1) * background_rect.h)
            bg = pygame.Surface(asize)

            # Create the background
            for x in range(0, asize[0], background_rect.w):
                for y in range(0, asize[1], background_rect.h):
                    screen.blit(background, (x, y))
            
            # Load controls
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise SystemExit()
                if event.type == pygame.KEYDOWN:
                    buttonPressed = True
                    if event.key == K_RIGHT:
                        rightPressed = True
                        direction = True
                        if event.key == K_UP:
                            upPressed = True
                    if event.key == K_LEFT:
                        leftPressed = True
                        direction = False
                        if event.key == K_UP:
                            upPressed = True
                    if event.key == K_UP:
                        upPressed = True
                    if event.key == K_SPACE:
                        spacePressed = True
                        bullet = player.attackLaunch()
                        bulletSprites.add(bullet)
                        entities.add(bullet)


                elif event.type == pygame.KEYUP:
                    if event.key == K_RIGHT:
                        rightPressed = False
                    if event.key == K_LEFT:
                        leftPressed = False
                    if event.key == K_UP:
                        upPressed = False
                    if rightPressed and leftPressed and upPressed and spacePressed == False:
                        buttonPressed = False


            for joe in bulletSprites:
                joe.update(screen, bg)
                hitSprites = pygame.sprite.spritecollide(joe, entities, False, pygame.sprite.collide_mask)
                for sprite in hitSprites:
                    for plats in platforms:
                        if sprite == plats:
                            entities.remove(joe)
                            bulletSprites.remove(joe)
                    for enemy in enemySprites:
                        if sprite == enemy:
                            bullet.attackHit(enemy)
                            entities.remove(joe)
                            bulletSprites.remove(joe)
                            if enemy.getHealth() <= 0:
                                entities.remove(enemy)
                    for boss in bossSprite:
                         if sprite == boss:
                            bullet.attackHit(boss)
                            entities.remove(joe)
                            bulletSprites.remove(joe)
                            if boss.getHealth() <= 0:
                                entities.remove(boss)
                                bossDead = True
                                          
                
            #Animate
            if buttonPressed:
                milliseconds = timer.tick(FPS)
                seconds = milliseconds / 1000.0
                cycletime += seconds
                if cycletime > interval:
                    cycletime = 0
                    newnr += 1

                if upPressed:
                    picnr = newnr % len(player.jonJump)
                    
                if rightPressed:
                    picnr = newnr % len(player.jonWalkRight)
                    if upPressed:
                        picnr = newnr % len(player.jonJump)

                if leftPressed:
                    picnr = newnr % len(player.jonWalkLeft)
                    if upPressed:
                        picnr = newnr % len(player.jonJump)
                
                oldnr = newnr
                                

            # Play the level
            for power in powerUpSprites:
                if pygame.sprite.spritecollide(player, powerUpSprites, True, pygame.sprite.collide_mask):
                    power.collected(player)
                    print player.getHealth()

            # Enemy attacking
            for enemy in enemySprites:
                if player.getDist(enemy) < 100:
                    enemy.attackLaunch(player)
                    
            hitSprite = pygame.sprite.spritecollide(player, enemySprites, False, pygame.sprite.collide_mask)
            for sprite in hitSprite:
                enemy.attackHit(player)

            # Boss attacking
            for boss in bossSprite:
                x = 5

                
            # Player range limits?
            # Update healths?

            # Player collision with fire; if true, 50 damage the player
            if pygame.sprite.spritecollide(player, fires, False, pygame.sprite.collide_mask):
                player.setHealth(player.getHealth()-50)

            if player.getHealth() <= 0:
                nextLevel = False
                playerAlive = False

            camera.update(player)

            # Update the player and everything else
            player.update(upPressed, leftPressed, rightPressed, platforms, screen, bg, direction, picnr)

            for e in entities:
                screen.blit(e.image, camera.apply(e))

            pygame.display.update() # Update the display

        if nextLevel == True:
            currentLevel += 1
                               
        else:
            currentLevel = currentLevel

        pygame.display.update()

        song.stop()
    print "You Win"
    quit()
    
##########################################################################################
# Load the title screen to start the game        
titleScreen()




