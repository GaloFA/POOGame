"""This module contains the MonsterSpawner class."""

import logging
import random

import pygame

import settings
from business.entities.monster import Monster
from business.world.interfaces import IGameWorld, IMonsterSpawner
from presentation.sprite import MonsterSprite
from business.handlers.cooldown_handler import CooldownHandler

BASE_COOLDOWN = 250
class MonsterSpawner(IMonsterSpawner): #
    """Spawns monsters in the game world."""

    def __init__(self):
        self.__logger = logging.getLogger(__name__)
        self.__spawn_cooldown = CooldownHandler(1000)

    def update(self, world: IGameWorld):
        self.spawn_monster(world)

    def spawn_monster(self, world: IGameWorld):
        pos_x = random.randint(0, settings.WORLD_WIDTH)
        pos_y = random.randint(0, settings.WORLD_HEIGHT)
        monster = Monster(pos_x, pos_y, MonsterSprite(pos_x, pos_y))
        world.add_monster(monster)
        self.__logger.debug("Spawning monster at (%d, %d)", pos_x, pos_y)
