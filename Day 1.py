import pygame
#initialize pygame
pygame.init()
#creating screen for the game
screen = pygame.display.set_mode((1000,800))
#Game loop(window doesn't close down or hanging)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

