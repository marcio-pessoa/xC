"""
pong.py

Author: Marcio Pessoa <marcio.pessoa@gmail.com>
Contributors: none

Change log:
2019-01-01
        * Version: 0.2
        * Changed: Python 3 ready.

2018-07-22
        * Version: 0.01b
        * Added: First version.
"""

import sys
import os
import random
from xC.echo import verbose, level, \
    echo, echoln, erro, erroln, warn, warnln, info, infoln, code, codeln

if sys.version_info >= (3, 0):
    import contextlib
    with contextlib.redirect_stdout(None):
        import pygame
        from pygame.locals import *
else:
    with open(os.devnull, 'w') as f:
        oldstdout = sys.stdout
        sys.stdout = f
        import pygame
        from pygame.locals import *
        sys.stdout = oldstdout


class Screensaver:

    def __init__(self, screen):
        """
        description:
        """
        self.version = '0.2'
        self.screen = screen
        self.running = False
        self.set()

    def start(self):
        """
        description:
        """
        infoln('Screensaver...')
        infoln('Starting...', 1)
        self.running = True
        self.reset()

    def reset(self):
        """
        description:
        """
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill([0, 0, 0])  # Black
        pygame.mouse.set_visible(False)

    def set(self):
        """
        description:
        """
        self.type = 'black'
        self.types = ['black', 'squares', 'lines', 'circles']

    def set_type(self, type=None):
        """
        description:
        """
        if type in self.types:
            self.type = type
            return
        if type == 'random':
            self.type = random.choice(self.types)
            return

    def run(self):
        """
        description:
        """
        if self.type == 'black':
            self.__black()
        elif self.type == 'squares':
            self.__squares()
        elif self.type == 'lines':
            self.__lines()
        elif self.type == 'circles':
            self.__circles()
        self.screen.blit(self.background, [0, 0])

    def stop(self):
        """
        description:
        """
        self.running = False
        pygame.mouse.set_visible(True)
        infoln("Exiting...", 1)

    def __black(self):
        pass

    def __lines(self):
        color = [random.randrange(0, 255),
                 random.randrange(0, 255),
                 random.randrange(0, 255)]
        position = [random.randrange(0, self.background.get_size()[0]),
                    random.randrange(0, self.background.get_size()[1])]
        size = [random.randrange(0, self.background.get_size()[0] -
                position[0]),
                random.randrange(0, self.background.get_size()[1] -
                position[1])]
        rect = [position[0], position[1], size[0], size[1]]
        pygame.draw.line(self.background, color,
                         position,
                         size)

    def __squares(self):
        color = [random.randrange(0, 255),
                 random.randrange(0, 255),
                 random.randrange(0, 255)]
        position = [random.randrange(0, self.background.get_size()[0]),
                    random.randrange(0, self.background.get_size()[1])]
        size = [random.randrange(0, self.background.get_size()[0] -
                position[0]),
                random.randrange(0, self.background.get_size()[1] -
                position[1])]
        rect = [position[0], position[1], size[0], size[1]]
        pygame.draw.rect(self.background, color, rect)

    def __circles(self):
        color = [random.randrange(0, 255),
                 random.randrange(0, 255),
                 random.randrange(0, 255)]
        position = [random.randrange(0, self.background.get_size()[0]),
                    random.randrange(0, self.background.get_size()[1])]
        radius = random.randrange(0, self.background.get_size()[0] / 16)
        pygame.draw.circle(self.background, color, position, radius)
