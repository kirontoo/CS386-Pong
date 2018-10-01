# CS-386 Pong
# Amy Nguyen-Dang

import pygame
from pygame.sprite import Sprite


class Paddle(Sprite):
    def __init__(self, settings, screen, color, pos, size, type):
        """Create a paddle"""
        super(Paddle, self).__init__()
        self.screen = screen
        self.settings = settings
        self.width, self.height = size
        self.type = type
        self.screen_rect = screen.get_rect()

        self.color = color
        self.x, self.y = pos

        # Save paddle rect
        self.rect = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def draw_paddle(self):
        """Draw the paddle"""
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def player_movement(self, move):
        """Move paddle to follow mouse movement"""
        move_left, move_right, move_up, move_down = move

        # Move side paddle up and down
        if self.type == "side":
            if move_up and self.rect.top > 0:
                self.y -= self.settings.paddle_speed

            if move_down and self.rect.bottom < self.screen_rect.bottom:
                self.y += self.settings.paddle_speed
        else:
            # Move top and bottom paddle left and right
            if move_left and self.rect.left > 0:
                self.x -= self.settings.paddle_speed

            if move_right and self.rect.right <= self.settings.screen_midX - (self.settings.net_width // 2):
                self.x += self.settings.paddle_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def ai_movement(self, ball):
        """AI Paddle follows the ball movement"""
        if self.type == "side":
            self.side_paddle_ai_movement(ball.y)

        if self.type == "top" or self.type == "bottom":
            self.top_bottom_paddle_ai_movement(ball.x)

    def side_paddle_ai_movement(self, ball_y):
        """Side AI paddle follows the ball movement"""
        center_y = self.y + (self.height / 2)

        # Follow the ball's movement
        if center_y < ball_y - self.settings.ai_follow:
            self.y += self.settings.ai_speed
        elif center_y > ball_y + self.settings.ai_follow:
            self.y -= self.settings.ai_speed

        self.rect.y = self.y

    def top_bottom_paddle_ai_movement(self, ball_x):
        """Top and bottom AI paddle follows the ball movement"""
        center_x = self.x + (self.width / 2)

        # Follow the ball's movement
        if center_x < ball_x - self.settings.ai_follow:
            self.x += self.settings.ai_speed
        elif center_x > ball_x + self.settings.ai_follow:
            self.x -= self.settings.ai_speed

        net = self.settings.screen_midX + (self.settings.net_width // 2)

        # Limit the paddle's horizontal movement
        if self.x <= net:
            self.x = net

        if self.rect.right > self.settings.screen_width:
            self.x = self.settings.screen_width - (self.width // 2)

        self.rect.x = self.x
