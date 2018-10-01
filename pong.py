# CS-386 Pong
# Amy Nguyen-Dang

import pygame
import sys

from settings import Settings
from ball import Ball
from player import Player
from sounds import Sounds
from scoreboard import Scoreboard
from game_stats import GameStats
from start_screen import StartScreen


# noinspection PyAttributeOutsideInit
class Pong:
    def __init__(self):
        """Initiate pong game settings and objects"""
        pygame.init()
        pygame.display.set_caption("Pong")

        self.settings = Settings()
        self.clock = pygame.time.Clock()

        # Create a screen
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        # Create sound object
        self.sounds = Sounds()

        # Create the start screen
        self.start_screen = StartScreen(self.settings, self.screen)

        # Create an instance to store game statistics and create a scoreboard.
        self.stats = GameStats()
        self.sb = Scoreboard(self.settings, self.screen, self.stats)

        # Create all game objects
        self.create_objects()

    def run_game(self):
        """Run the game"""
        while True:
            # Limit FPS
            self.clock.tick(self.settings.FPS)

            # Watch for keyboard events
            self.check_events()

            # While game is active, update game object movement
            if self.stats.game_active:
                self.ball.update(self.p1, self.p2)
                self.p1.update()
                self.p2.update(self.ball)

            # Update the screen
            self.update_screen()

    def check_events(self):
        """Check for any keyboard events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.check_play_button(mouse_x, mouse_y)
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def check_keydown_events(self, event):
        """Check all keydown events"""
        if event.key == pygame.K_RIGHT:
            self.p1.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.p1.moving_left = True
        elif event.key == pygame.K_UP:
            self.p1.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.p1.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def check_keyup_events(self, event):
        """Check all key up events"""
        if event.key == pygame.K_RIGHT:
            self.p1.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.p1.moving_left = False
        elif event.key == pygame.K_UP:
            self.p1.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.p1.moving_down = False

    def check_play_button(self, mouse_x, mouse_y):
        """Check if the play button has been pressed."""
        button_clicked = self.start_screen.play_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked and not self.stats.game_active:
            # Reset all settings
            self.settings.initialize_dynamic_settings()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

            # Reset the game statistics.
            self.stats.reset_stats()
            self.stats.game_active = True

            # Reset the scoreboard images.
            self.sb.reset_scoreboard()

            # Reset game objects
            self.ball.reset()

    def create_objects(self):
        """Create all game objects"""
        self.ball = Ball(self.settings, self.screen, self.sounds, self.stats, self.sb)
        self.p1 = Player(self.settings, self.screen, self.settings.paddle_p1_color)
        self.p2 = Player(self.settings, self.screen, self.settings.paddle_p2_color, False)

    def update_screen(self):
        """Update the screen"""
        self.screen.fill(self.settings.screen_bg_color)

        if self.stats.game_active:
            self.stats.show_start_screen = False

            # Draw the net
            self.sb.draw_net()

            # draw all objects
            self.ball.draw_ball()
            self.p1.draw_all_paddles()
            self.p2.draw_all_paddles()

            # Draw the scoreboard information
            self.sb.show_scores()

        # Show the winner
        elif self.stats.winner != "none":
                self.sb.show_scores()
                self.start_screen.play_button.draw_button()
                pygame.mouse.set_visible(True)
        else:
            # Show the start screen
            self.start_screen.show_start_screen()

        # Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == "__main__":
    # call the main function
    Pong().run_game()
