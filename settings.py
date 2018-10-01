# CS-386 Pong
# Amy Nguyen-Dang

import random


# noinspection PyAttributeOutsideInit
class Settings:

    def __init__(self):

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_midX = self.screen_width // 2
        self.screen_bg_color = (42, 78, 110)
        self.screen_padding = 30
        self.FPS = 30

        # Ball Settings
        self.ball_radius = 15
        self.ball_color = (255, 255, 255)

        # Paddle settings
        self.paddle_width = 15
        self.paddle_length = 100
        self.paddle_p1_color = (0, 255, 159)
        self.paddle_p2_color = (255, 149, 0)
        self.paddle_speed = 15

        # Net settings
        self.net_width = 5
        self.net_height = 30
        self.net_color = (81, 137, 188)
        self.net_offset = 25

        # Scoreboard settings
        self.scoreboard_text_color = (243, 248, 254)
        self.scoreboard_border_color = (255, 89, 0)
        self.scoreboard_font_size = 70

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize all dynamic settings"""
        # Ball speed settings
        self.ball_speedX = self.random_speed()
        self.ball_speedY = self.random_speed()
        self.ball_velocity = 0.20

        # AI player settings
        self.ai_follow = 35
        self.ai_speed = 6

    @staticmethod
    def random_speed():
        """Generate a random ball speed and direction"""
        return random.choice([i for i in range(-9, 9) if i not in [0, -1, -2, -3, 1, 2, 3]])
