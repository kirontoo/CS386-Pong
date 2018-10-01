# CS-386 Pong
# Amy Nguyen-Dang

import pygame


# noinspection PyAttributeOutsideInit
class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, settings, screen, stats):
        """Initialize scoreboard attributes"""
        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats

        # Font settings for scoring information
        self.text_color = self.settings.scoreboard_text_color
        self.font = pygame.font.SysFont(None, self.settings.scoreboard_font_size)

        # Prepare the initial score images
        self.reset_scoreboard()

    def prep_player_score(self):
        """Turn the player score into a rendered image."""

        # Create the player score image
        score_str = "{:,}".format(self.stats.player_score)
        self.player_score_image = self.font.render(score_str, True,
                                                   self.text_color, self.settings.screen_bg_color)

        # Display the score at the left side of the net
        self.player_score_rect = self.player_score_image.get_rect()
        self.player_score_rect.right = self.settings.screen_midX - (self.settings.net_width // 2) \
                                                                 - self.settings.screen_padding
        self.player_score_rect.top = self.settings.screen_padding

    def prep_ai_score(self):
        """Turn the AI score into a rendered image."""

        # Create the AI score image
        score_str = "{:,}".format(self.stats.ai_score)
        self.ai_score_image = self.font.render(score_str, True, self.text_color, self.settings.screen_bg_color)

        # Display the score at the left side of the net
        self.ai_score_rect = self.ai_score_image.get_rect()
        self.ai_score_rect.left = self.settings.screen_midX + (self.settings.net_width // 2) \
                                                            + self.settings.screen_padding
        self.ai_score_rect.top = self.settings.screen_padding

    def prep_winning_score(self):
        """Turn the AI score into a rendered image."""
        # Create the AI score image
        score_str = "{:,}".format(self.stats.winning_score)
        font = pygame.font.SysFont(None, 50)
        self.winning_score_image = font.render(score_str, True, self.text_color, self.settings.screen_bg_color)

        # Display the score at the left side of the net
        self.winning_score_rect = self.winning_score_image.get_rect()
        self.winning_score_rect.left = self.settings.screen_midX - (self.winning_score_rect.width // 2)
        self.winning_score_rect.top = self.settings.screen_padding * 4

    def prep_winning_screen(self):
        """Prepare a winning screen"""

        # Set winner message
        winner_str = "Winner: "
        if self.stats.winner == "p1":
            winner_str += "Player 1"
            text_color = self.settings.paddle_p1_color
        else:
            winner_str += "Player 2"
            text_color = self.settings.paddle_p2_color

        # Change font size
        font = pygame.font.SysFont(None, 100)

        # Position the text
        self.winning_screen_image = font.render(winner_str, True, text_color, self.settings.net_color)
        self.winning_screen_rect = self.winning_screen_image.get_rect()
        self.winning_screen_rect.x = self.settings.screen_midX - (self.winning_screen_rect.width // 2)
        self.winning_screen_rect.y = (self.settings.screen_height // 2) - (self.winning_screen_rect.height * 2)

    def prep_score_borders(self):
        """Prepare all borders for scoreboard"""

        # Player score border
        self.player_border = self.player_score_image.get_rect()
        self.player_border.x = self.player_score_rect.x - 2
        self.player_border.y = self.player_score_rect.y - 2
        self.player_border.width = self.player_score_rect.width + 4
        self.player_border.height = self.player_score_rect.height + 4

        self.player_border_pos = (self.player_border.x, self.player_border.y,
                                  self.player_border.width, self.player_border.height)

        # AI score border
        self.ai_border = self.ai_score_image.get_rect()
        self.ai_border.x = self.ai_score_rect.x - 2
        self.ai_border.y = self.ai_score_rect.y - 2
        self.ai_border.width = self.ai_score_rect.width + 4
        self.ai_border.height = self.ai_score_rect.height + 4

        self.ai_border_pos = (self.ai_border.x, self.ai_border.y,
                              self.ai_border.width, self.ai_border.height)

        # Winning score border
        self.winning_border = self.winning_score_image.get_rect()
        self.winning_border.x = self.winning_score_rect.x - 2
        self.winning_border.y = self.winning_score_rect.y - 2
        self.winning_border.width = self.winning_score_rect.width + 4
        self.winning_border.height = self.winning_score_rect.height + 4

        self.winning_border_pos = (self.winning_border.x, self.winning_border.y,
                                   self.winning_border.width, self.winning_border.height)

    def show_scores(self):
        """Draw all scores, winning number and borders to the screen"""

        border_color = self.settings.scoreboard_border_color
        pygame.draw.rect(self.screen, border_color, self.player_border)
        pygame.draw.rect(self.screen, border_color, self.ai_border)
        pygame.draw.rect(self.screen, border_color, self.winning_border)
        self.screen.blit(self.player_score_image, self.player_score_rect)
        self.screen.blit(self.ai_score_image, self.ai_score_rect)
        self.screen.blit(self.winning_score_image, self.winning_score_rect)

        # Show the winner
        if self.stats.winner != "none":
            self.screen.blit(self.winning_screen_image, self.winning_screen_rect)

    def draw_net(self):
        """Draw a net"""
        width = self.settings.net_width
        height = self.settings.net_height
        color = self.settings.net_color
        net_offset = self.settings.net_offset
        x = (self.settings.screen_width // 2) - (width // 2)
        y = 0

        num_of_boxes = self.settings.screen_height // height

        for box in range(num_of_boxes):
            pygame.draw.rect(self.screen, color, (x, y, width, height))
            y += (net_offset + height)

    def reset_scoreboard(self):
        self.prep_player_score()
        self.prep_ai_score()
        self.prep_winning_score()
        self.prep_score_borders()
