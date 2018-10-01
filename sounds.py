# CS-386 Pong
# Amy Nguyen-Dang

import pygame
import os


# noinspection PyAttributeOutsideInit
class Sounds:
    dir = 'sound_effects'

    def __init__(self):
        """Initialize sound mixer"""
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.mixer.init()
        pygame.mixer.set_num_channels(10)
        self.load_sounds()

    def load_sounds(self):
        """Load all sound files"""
        self.game_win = pygame.mixer.Sound(os.path.join(self.dir, 'you_win.wav'))
        self.bump = pygame.mixer.Sound(os.path.join(self.dir, 'bump.wav'))
        self.scored = pygame.mixer.Sound(os.path.join(self.dir, 'Hit_Hurt.wav'))

    @staticmethod
    def play_sound(sound_effect, loop):
        """Play a sound effect"""
        channel = pygame.mixer.find_channel()
        if channel:
            channel.play(sound_effect, loop)
