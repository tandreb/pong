import pygame.sprite

RADIUS = 10
BALL_SPEED = 8


class Ball(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.radius = RADIUS
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        self.rect = self.image.get_rect()
        self.speed_x = BALL_SPEED
        self.speed_y = BALL_SPEED
        pygame.draw.circle(self.image, pygame.Color('white'), (self.radius, self.radius), self.radius)

    def update(self):
        self.move()

    def move(self):
        if self.rect.centery >= self.screen_height or self.rect.centery <= 0:
            self.speed_y *= -1
        if self.rect.centerx >= self.screen_width or self.rect.centerx <= 0:
            self.reset_ball()

        self.rect.centerx += self.speed_x
        self.rect.centery += self.speed_y

    def collided_with_player(self, player):
        if abs(self.rect.left - player.rect.right) <= 5 and self.speed_x < 0:
            self.speed_x*= -1
        if abs(self.rect.right - player.rect.left) <= 5 and self.speed_x > 0:
            self.speed_x *= -1
        if abs(self.rect.top - player.rect.bottom) <= 5 and self.speed_y <0:
            self.speed_y *= -1
        if abs(self.rect.bottom - player.rect.top) <= 5 and self.speed_y > 0:
            self.speed_y *= -1


    def reset_ball(self):
        self.rect.centerx = self.screen_width // 2
