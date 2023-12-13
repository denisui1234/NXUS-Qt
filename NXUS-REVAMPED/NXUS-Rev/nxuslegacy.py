print("Getting required files...")
import pygame
import os
screen = pygame.display.set_mode((600, 400))
icon = pygame.image.load("demo.png")
pygame.display.set_caption("NXUS REV")
pygame.display.set_icon(icon)

# Load and scale the background image
image = pygame.image.load("nzxt.png")
image = pygame.transform.scale(image, (600, 400))
using = True

while using:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            using = False
            
    screen.blit(image, (0, 0))
    pygame.display.flip()
    
pygame.quit()
input("you can now close the terminal")