import pygame.sprite

PLAYER_WIDTH = 5
PLAYER_HEIGHT = 80


class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.speed_max = 7
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(pygame.Color('white'))
        self.rect = self.image.get_rect(center=(40, self.screen_height // 2))

    def update(self):
        self.get_input()

    def get_input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.rect.y -= self.speed_max
        if key[pygame.K_DOWN]:
            self.rect.y += self.speed_max
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height
