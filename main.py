import pygame

GAME_WIDTH = 800
GAME_HEIGHT = 600
PLAYER_WIDTH = 10
PLAYER_HEIGHT = 60

class Ball(pygame.sprite.Sprite):
    pass

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.surface = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = self.surface.get_rect(topleft=(40, 40))
        self.surface.fill((255,255,255))

    def draw(self, surface_to_draw_on):
        surface_to_draw_on.blit(self.surface, self.rect)


    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.rect.y -= 1
        if key[pygame.K_DOWN]:
            self.rect.y += 1

    def update(self, surface_to_draw_on):
        self.move()
        self.draw(surface_to_draw_on)

def main_loop():
    pygame.init()
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    is_running = True
    player = Player()
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Close the program any way you want, or troll users who want to close your program.
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    raise SystemExit

        surface.fill((0,0,0))
        player.update(surface)
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main_loop()
