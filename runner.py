#!/usr/bin/env python3
"""Runs the game"""
import pygame

import settings
from business.entities.player import Player
from business.world.game_world import GameWorld
from business.world.monster_spawner import MonsterSpawner
from business.world.tile_map import TileMap
from game import Game
from presentation.display import Display
from presentation.input_handler import InputHandler
from presentation.sprite import PlayerSprite


def initialize_player():
    """Initializes the player object"""
    x, y = settings.WORLD_WIDTH//2, settings.WORLD_HEIGHT//2
    return Player(x, y, PlayerSprite(x, y), 100)


def initialize_game_world(display):
    """Initializes the game world with a display dependency"""
    monster_spawner = MonsterSpawner()
    tile_map = TileMap()
    player = Player(settings.WORLD_WIDTH//2, settings.WORLD_HEIGHT//2, PlayerSprite(settings.WORLD_WIDTH//2, settings.WORLD_HEIGHT//2), 100)
    return GameWorld(monster_spawner, tile_map, player)


def restart_game():
    """Reinicia La Partida"""
    main()


def main():
    """Main function to run the game"""
    # Initialize pygame
    pygame.init()  # pylint: disable=E1101

    # Initialize the game objects
    
    display = Display()
    world = initialize_game_world(display)
    display.load_world(world)
    input_handler = InputHandler(world)

    # Create a game instance and start it
    game = Game(display, world, input_handler, restart_game)
    game.run()

    # Properly quit Pygame
    pygame.quit()  # pylint: disable=E1101


if __name__ == "__main__":
    main()
