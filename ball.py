# CS-386 Pong
# Amy Nguyen-Dang

import pygame
from pygame.sprite import Sprite


class Ball(Sprite):
    """Class to manage the ball"""
    def __init__(self, settings, screen, sounds, stats, sb):
        """Create a ball at the center of the screen"""
        super(Ball, self).__init__()
        self.screen = screen
        self.settings = settings
        self.sounds = sounds
        self.stats = stats
        self.sb = sb
        self.radius = self.settings.ball_radius
        self.color = self.settings.ball_color
        self.x = self.settings.screen_width // 2
        self.y = self.settings.screen_height // 2

        # Save ball rect
        self.rect = pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

        # Ball speed
        self.ball_speedX = self.settings.ball_speedX
        self.ball_speedY = self.settings.ball_speedY

    def draw_ball(self):
        """Draw the ball"""
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def update(self, p1, p2):
        """Move the ball across the screen."""
        self.x += int(self.ball_speedX)
        self.y += int(self.ball_speedY)

        self.rect.x = self.x
        self.rect.y = self.y

        # check for winner and stop game
        self.check_for_winner()

        # check for collisions and screen boundaries
        self.check_all_paddle_collisions(p1, p2)
        self.check_screen_boundary()

    def check_screen_boundary(self):
        """Check when the ball reaches the screen boundaries"""

        # Ball hits the screen boundaries
        if self.x >= self.settings.screen_width or self.x <= 0 or self.y <= 0 or self.y >= self.settings.screen_height:
            # Reset ball and update score
            if self.x >= self.settings.screen_midX:
                self.stats.player_score += 1
                self.sb.prep_player_score()
            else:
                self.stats.ai_score += 1
                self.sb.prep_ai_score()

            self.sounds.play_sound(self.sounds.scored, 0)
            self.reset()

    def check_for_winner(self):
        """check for the winner and stop the game"""
        if self.stats.player_score == self.stats.winning_score:
            self.stats.winner = "p1"

        elif self.stats.ai_score == self.stats.winning_score:
            self.stats.winner = "p2"

        if self.stats.winner != "none":
            self.stats.game_active = False
            self.sb.prep_winning_screen()
            self.sounds.play_sound(self.sounds.game_win, 0)

    def check_paddle_collision(self, paddle):
        """Check paddle collisions and bounce back"""
        collision = pygame.sprite.collide_rect(paddle, self)

        if collision:
            self.sounds.play_sound(self.sounds.bump, 0)
            self.change_ball_speed(paddle)

    def check_all_paddle_collisions(self, p1, p2):
        self.check_paddle_collision(p1.top_paddle)
        self.check_paddle_collision(p1.bottom_paddle)
        self.check_paddle_collision(p1.side_paddle)
        self.check_paddle_collision(p2.top_paddle)
        self.check_paddle_collision(p2.bottom_paddle)
        self.check_paddle_collision(p2.side_paddle)

    def change_ball_speed(self, paddle):
        """Change ball speed and direction"""
        paddle_length = self.settings.paddle_length

        if paddle.type == "top" or paddle.type == "bottom":
            self.ball_speedY = -self.ball_speedY

            # adjust horizontal movement
            deltax = self.x - (paddle.x + paddle_length / 2)
            self.ball_speedX = deltax * self.settings.ball_velocity

        if paddle.type == "side":
            self.ball_speedX = - self.ball_speedX

            # adjust horizontal movement
            deltay = self.y - (paddle.y + paddle_length / 2)
            self.ball_speedY = deltay * 0.35

    def reset(self):
        """Rest ball position and speed"""
        self.x = self.settings.screen_width // 2
        self.y = self.settings.screen_height // 2
        self.ball_speedX = self.settings.random_speed()
        self.ball_speedY = self.settings.random_speed()
