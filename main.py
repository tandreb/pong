import pygame
import random

from ball import Ball
from player import Player

WIDTH = 800
HEIGHT = 600
FPS = 100

pygame.init()
# pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()  # For syncing the FPS

player = Player(WIDTH, HEIGHT)
ball = Ball(WIDTH, HEIGHT)
# group all the sprites together for ease of update
all_sprites = pygame.sprite.Group()
all_sprites.add(player, ball)

ball.rect.center = (WIDTH // 2, HEIGHT // 2)

# Game loop
running = True
while running:

    # 1 Process input/events
    clock.tick(FPS)  # will make the loop run at the same speed all the time
    for event in pygame.event.get():  # gets all the events which have occurred till now and keeps tab of them.
        # listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # 2 Update
    all_sprites.update()

    # 3 Draw/render
    screen.fill(pygame.Color('gray10'))
    pygame.draw.aaline(screen, pygame.Color('white'), (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    all_sprites.draw(screen)
    ########################

    # Your code comes here
    if pygame.sprite.collide_rect(player, ball):
        ball.collided_with_player(player)

    ########################

    # Done after drawing everything to the screen
    pygame.display.flip()

pygame.quit()
