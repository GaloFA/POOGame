""" Module that contains respresentation of the pause menu"""
import pygame
from presentation.design_elements import Button, Title
import settings


class PauseMenu:
    def __init__(self, screen):
        """Initializes the PauseMenu object with buttons for resuming and quitting."""
        self.screen = screen

        self.resume_button = Button(settings.SCREEN_WIDTH//2-100, settings.SCREEN_HEIGHT //
                                    2 - 50, 200, 50, "Reanudar", (0, 200, 0), (255, 255, 255))
        self.quit_button = Button(settings.SCREEN_WIDTH//2-100, settings.SCREEN_HEIGHT //
                                  2 + 50, 200, 50, "Salir", (200, 0, 0), (255, 255, 255))
        self.save_and_quit_button = Button(settings.SCREEN_WIDTH//2-100, settings.SCREEN_HEIGHT //
                                           2 + 150, 200, 50, "Salir y guardar", (200, 0, 0), (255, 255, 255))
        self.titulo = Title("MENU PAUSA", settings.SCREEN_WIDTH //
                            2, settings.SCREEN_HEIGHT//2-200, 150, (255, 255, 255))

        self.overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        self.overlay.fill((62, 62, 62))
        self.buttons = [self.resume_button,
                        self.quit_button, self.save_and_quit_button]
        self.titles = [self.titulo]

    def draw(self):
        self.screen.blit(self.overlay, (0, 0))

        # Dibujar los botones
        for title in self.titles:
            title.draw(self.screen)

        for button in self.buttons:
            button.draw(self.screen)

    def check_click(self, mouse_pos):
        if self.resume_button.is_clicked(mouse_pos):
            return "r"
        if self.quit_button.is_clicked(mouse_pos):
            return "q"
        if self.save_and_quit_button.is_clicked(mouse_pos):
            return "sq"
        return None
