# CS-386 Pong
# Amy Nguyen-Dang

from paddle import Paddle


# noinspection PyAttributeOutsideInit
class Player:
    """A class to manage players"""
    def __init__(self, settings, screen, color, player=True):
        """Create a player or AI player"""
        self.settings = settings
        self.screen = screen
        self.score = 0
        self.player = player
        self.color = color

        # Create the top, bottom and side paddles
        if self.player:
            self.create_player_paddles()
            self.moving_right = False
            self.moving_left = False
            self.moving_up = False
            self.moving_down = False

        else:
            self.create_ai_paddles()

    def update(self, ball=0):
        """Update paddle movement"""
        if self.player:
            move = (self.moving_left, self.moving_right, self.moving_up, self.moving_down)
            self.side_paddle.player_movement(move)
            self.top_paddle.player_movement(move)
            self.bottom_paddle.player_movement(move)
        else:
            self.side_paddle.ai_movement(ball)
            self.top_paddle.ai_movement(ball)
            self.bottom_paddle.ai_movement(ball)

    def get_horiz_paddle_size(self):
        return self.settings.paddle_length, self.settings.paddle_width

    def get_verti_paddle_size(self):
        return self.settings.paddle_width, self.settings.paddle_length

    def get_bottom_y(self):
        return self.settings.screen_height - self.settings.paddle_width

    @staticmethod
    def get_top_y():
        return 0

    def get_side_y(self):
        return self.settings.screen_height // 2 - (self.settings.paddle_length // 2)

    def create_ai_paddles(self):
        """Create all AI paddles on the right side of the screen"""
        midx = self.settings.screen_midX
        right_midx = (self.settings.screen_width - midx) // 2 + midx - (self.settings.paddle_length // 2)

        # For top and bottom paddles
        size = self.get_horiz_paddle_size()

        # create top paddle
        y = self.get_top_y()
        pos = (right_midx, y)
        self.top_paddle = Paddle(self.settings, self.screen, self.color, pos, size, "top")

        # create bottom paddle
        y = self.get_bottom_y()
        pos = (right_midx, y)
        self.bottom_paddle = Paddle(self.settings, self.screen, self.color, pos, size, "bottom")

        # create side paddle
        size = self.get_verti_paddle_size()
        x = self.settings.screen_width - self.settings.paddle_width
        y = self.get_side_y()
        pos = (x, y)
        self.side_paddle = Paddle(self.settings, self.screen, self.color, pos, size, "side")

    def create_player_paddles(self):
        """Create all three player paddles"""
        midx = self.settings.screen_midX
        left_midx = midx // 2 - (self.settings.paddle_length // 2)

        # For top and bottom paddles
        size = self.get_horiz_paddle_size()

        # create top paddle
        y = self.get_top_y()
        pos = (left_midx, y)
        self.top_paddle = Paddle(self.settings, self.screen, self.color, pos, size, "top")

        # create bottom paddle
        y = self.get_bottom_y()
        pos = (left_midx, y)
        self.bottom_paddle = Paddle(self.settings, self.screen, self.color, pos, size, "bottom")

        # create side paddle
        size = self.get_verti_paddle_size()
        x = self.x = 0
        y = self.get_side_y()
        pos = (x, y)
        self.side_paddle = Paddle(self.settings, self.screen, self.color, pos, size, "side")

    def draw_all_paddles(self):
        """Draw all player paddles"""
        self.top_paddle.draw_paddle()
        self.bottom_paddle.draw_paddle()
        self.side_paddle.draw_paddle()
