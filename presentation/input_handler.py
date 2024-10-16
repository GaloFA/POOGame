"""This module contains the InputHandler class, which handles user input for the game."""

import pygame
import settings

from business.world.game_world import GameWorld
from business.handlers.death_handler import DeathHandler
from presentation.interfaces import IInputHandler


class InputHandler(IInputHandler):
    """Handles user input for the game."""

    def __init__(self, world: GameWorld):
        self.__world = world
        self.__death_handler = DeathHandler()

    def __example_method(self, keys):

        if keys[pygame.K_w]:
            self.__world.player.move(0, -1)

        if keys[pygame.K_s]:
            self.__world.player.move(0, 1)

        if keys[pygame.K_a]:
            self.__world.player.move(-1, 0)

        if keys[pygame.K_d]:
            self.__world.player.move(1, 0)

    def process_input(self):
        #posx = self.__world.player.pos_x
        #posy = self.__world.player.pos_y
        keys = pygame.key.get_pressed()
        self.__example_method(keys)
