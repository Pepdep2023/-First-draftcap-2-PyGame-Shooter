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

#Game loop(window doesn't close down or hanging)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
#If keystrock is pressed check weather it is right or left

# Screen colour:RBG(Red,Blue and Green)
        screen.fill((0,255,255))
        playerY -= 0.5
        print(playerY)

 #write 'player()' after screen.fill
        player(playerX,playerY)
        pygame.display.update()

