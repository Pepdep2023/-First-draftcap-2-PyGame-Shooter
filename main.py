import pygame
import random
#initialize pygame
pygame.init()
#creating screen for the game
screen = pygame.display.set_mode((1000,800))

#Title and Icon
pygame.display.set_caption("SHOOTER")
icon = pygame.image.load('ufo (2).png')
pygame.display.set_icon(icon)

#Player
player_image = pygame.image.load('spaceship.png')
player_image = pygame.transform.scale(player_image, (60, 60))
playerX = 500
playerY = 650

#Enemy
enemy_image = pygame.image.load('final-boss.png')
enemy_image = pygame.transform.scale(enemy_image, (40, 40))
enemyX = random.randint(0,1000)
enemyY = random.randint(100,100)
enemyX_change = 0

def player(x,y):
    screen.blit(player_image,(x,y))

def enemy(x,y):
    screen.blit(enemy_image,(x,y))   

playerX_change = playerX
#Game loop(window doesn't close down or hanging)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Screen colour:RBG(Red,Blue and Green)
        screen.fill((0,255,255))
    
        #If keystrock is pressed check weather it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = playerX_change - 10
                # player(playerX + 10, playerY)
            if event.key == pygame.K_RIGHT:
                playerX_change = playerX_change + 10
                # player(playerX - 10, playerY)
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # playerX_change = 10
                # player(playerX + 10, playerY)
 
 # Prevent the player from moving off the screen
    if playerX_change <= 0:
        playerX_change = 0
    elif playerX_change + 50 >= 1000:
        playerX_change = 1000 - 50
    if playerY <= 0:
       playerY = 0
    elif playerY + 50 >= 800:
        playerY = 800 - 50

 #write 'player()' after screen.fill
    # playerX += playerX_change
    player(playerX_change, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
    # playerX_change = 0
        
