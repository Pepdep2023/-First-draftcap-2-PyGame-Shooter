import pygame
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
player_image = pygame.transform.scale(player_image, (50, 50))
playerX = 500
playerY = 650

def player(x,y):
    screen.blit(player_image,(x,y))

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




 #write 'player()' after screen.fill
    # playerX += playerX_change
    player(playerX_change, playerY)
    pygame.display.update()
    # playerX_change = 0

