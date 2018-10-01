# CS-386 Pong
# Amy Nguyen-Dang

import pygame
from button import Button


# noinspection PyAttributeOutsideInit
class StartScreen:
    """A class to show the start screen"""

    def __init__(self, settings, screen):
        """Initialize all start screen attributes"""
        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Prepare start screen
        self.prep_title()
        self.prep_subtitle()

        # Create the play button
        self.play_button = Button(self.screen, "Play", self.settings.scoreboard_text_color,
                                  self.settings.paddle_p1_color)

    def prep_title(self):
        """Prepare the title screen"""
        font = pygame.font.SysFont(None, 100)
        text_color = self.settings.scoreboard_text_color
        title_str = "PONG"

        # Create and position the Title
        self.title_image = font.render(title_str, True, text_color, self.settings.screen_bg_color)
        self.title_rect = self.title_image.get_rect()
        self.title_rect.x = self.settings.screen_midX - (self.title_rect.width // 2)
        self.title_rect.y = self.settings.screen_padding * 3

    def prep_subtitle(self):
        """Prepare the title screen"""
        font = pygame.font.SysFont(None, 100)
        text_color = self.settings.scoreboard_border_color
        subtitle_str = "AI -- NO WALLS"

        # Create and position the Title
        self.subtitle_image = font.render(subtitle_str, True, text_color, self.settings.screen_bg_color)
        self.subtitle_rect = self.subtitle_image.get_rect()
        self.subtitle_rect.x = self.settings.screen_midX - (self.subtitle_rect.width // 2)
        self.subtitle_rect.top = self.title_rect.bottom + self.settings.screen_padding

    def show_start_screen(self):
        """Draw the title and subtitle."""
        self.screen.blit(self.title_image, self.title_rect)
        self.screen.blit(self.subtitle_image, self.subtitle_rect)

        # Draw the play button
        self.play_button.draw_button()
