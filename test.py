import pygame
import sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,500))
myfont = pygame.font.Font(None, 60)
inp = ""

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            inp += event.unicode

    screen.fill((0,0,0))
    txt = myfont.render(inp, True, (255,255,255))
    screen.blit(txt, (100,100))
    pygame.display.update()