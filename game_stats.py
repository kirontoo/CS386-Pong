# CS-386 Pong
# Amy Nguyen-Dang


# noinspection PyAttributeOutsideInit
class GameStats:
    """Track statistics for Pong."""

    def __init__(self):
        """Initialize statistics."""
        self.reset_stats()

        # Start pong in a inactive state.
        self.game_active = False

        # Set winning number
        self.winning_score = 5
        self.screen_delay_start = ""

    def reset_stats(self):
        """Reset all statistics that can change during the game."""
        self.player_score = 0
        self.ai_score = 0
        self.winner = "none"
        self.game_active = False
        self.show_start_screen = False
