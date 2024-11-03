"""This module defines the Game class."""

import logging
import time
import pygame
import settings
from business.exceptions import DeadPlayerException
from business.handlers.collision_handler import CollisionHandler
from business.handlers.death_handler import DeathHandler
from business.world.interfaces import IGameWorld
from presentation.interfaces import IDisplay, IInputHandler
from presentation.pause_menu import PauseMenu
from presentation.level_menu import NivelMenu
from business.entities.player import Player
from business.entities.items import DiccionarioClass


class Game:
    """
    Main game class.

    This is the game entrypoint.
    """

    def __init__(self, display: IDisplay, game_world: IGameWorld, input_handler: IInputHandler):
        self.__clock = pygame.time.Clock()
        self.__display = display
        self.__world = game_world
        self.__input_handler = input_handler
        self.__running = True
        self.__pause_menu = PauseMenu(display.screen)
        self.__level_menu = NivelMenu(display.screen)
        self.__items_inicializados = False  # SI NO FUNCIONA BORRAR
        self.__is_paused = False
        self.__is_level_up_menu_active = False
        self.start_ticks = pygame.time.get_ticks()  # Tiempo de inicio
        self.elapsed_time = 0  # Tiempo transcurrido en segundos
        self.previous_level = self.__world.player.level

    def __process_game_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # pylint: disable=E1101
                self.__running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.__is_paused = not self.__is_paused

    def __handle_pause_menu(self):
        self.__pause_menu.draw()
        pygame.display.flip()
        if pygame.mouse.get_pressed()[0]:
            action = self.__pause_menu.check_click(pygame.mouse.get_pos())
            if action == "r":
                self.__is_paused = False
            elif action == "q":
                self.__running = False
            elif action == "sq":
                self.__running = False
            else:
                self.__is_paused = False

    def __handle_level_up_menu(self):
        if not self.__items_inicializados:  # Verifica si los ítems no han sido inicializados
            self.initialize_items()

        if pygame.mouse.get_pressed()[0]:
            action = self.__level_menu.check_click(pygame.mouse.get_pos())
            if action == "item1":
                self.__items_inicializados = False
            if action == "item2":
                self.__items_inicializados = False
            if action == "item3":
                self.__items_inicializados = False
            if action == "skip":
                self.__items_inicializados = False
            if action == "reroll":
                self.reroll_items()
            self.__is_level_up_menu_active = False  # Cerrar menú de nivel

    def initialize_items(self):
        Diccionario_Clases = DiccionarioClass()
        diccionario_items = Diccionario_Clases.select_random_items()
        item_cards = self.__level_menu.colocar_items(diccionario_items)
        self.__level_menu.draw(item_cards)
        pygame.display.flip()
        self.__items_inicializados = True  # Marcar como inicializado

    def reroll_items(self):
        self.__items_inicializados = False  # Asegúrate de reinicializar los ítems

    def run(self):
        """Starts the game loop."""
        while self.__running:
            try:
                self.__process_game_events()

                if self.__is_paused:
                    self.__handle_pause_menu()
                    continue

                current_level = self.__world.player.level
                if current_level > self.previous_level:
                    self.__is_level_up_menu_active = True
                    self.previous_level = current_level

                if self.__is_level_up_menu_active:
                    self.__handle_level_up_menu()
                    continue

                self.elapsed_time = (
                    pygame.time.get_ticks() - self.start_ticks) / 1000
                self.__input_handler.process_input()
                self.__world.update()
                CollisionHandler.handle_collisions(self.__world)
                DeathHandler.check_deaths(self.__world)
                self.__display.render_frame()

                self.__clock.tick(settings.FPS)
            except DeadPlayerException:
                self.__running = False
