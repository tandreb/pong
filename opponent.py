import pygame.sprite

OPPONENT_WIDTH = 5
OPPONENT_HEIGHT = 80


class Opponent(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.speed_max = 7
        self.movement = 7
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.Surface((OPPONENT_WIDTH, OPPONENT_HEIGHT))
        self.image.fill(pygame.Color('white'))
        self.rect = self.image.get_rect(center=(self.screen_width - 40, self.screen_height // 2))

    def update(self):
        self.rect.centery += self.movement

    def follow_ball(self, ball):
        if self.rect.centery < ball.rect.centery:
            self.movement = self.speed_max
        elif self.rect.centery > ball.rect.centery:
            self.movement = -self.speed_max
        elif self.rect.centery == ball.rect.centery:
            self.movement = 0
