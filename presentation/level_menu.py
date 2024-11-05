import pygame
from presentation.design_elements import Button, Title, Container, ItemCard
import settings
from business.entities.items import *


class NivelMenu:
    def __init__(self, screen):
        """Inicializa el menú de nivelación con opciones y botones para rerollear y skipear."""
        self.screen = screen
        button_color = (50, 50, 50)
        button_text_color = (255, 255, 255)
        self.container = Container(
            settings.SCREEN_WIDTH//2-300, settings.SCREEN_HEIGHT//2-310, 600, 620, (84, 79, 79))

        self.title1 = Title(
            "¡SUBES DE NIVEL!", settings.SCREEN_WIDTH//2, settings.SCREEN_HEIGHT//2-210, 80, (255, 255, 255))
        # Botones de opciones de nivelación

        # Botones de reroll y skip
        self.reroll_button = Button(
            settings.SCREEN_WIDTH-250, settings.SCREEN_HEIGHT // 2 -
            50, 200, 50, "REROLL", button_color, button_text_color
        )
        self.skip_button = Button(
            settings.SCREEN_WIDTH-250, settings.SCREEN_HEIGHT // 2 +
            50, 200, 50, "SKIP", button_color, button_text_color
        )

        self.item_card1 = ItemCard(settings.SCREEN_WIDTH//2-250, settings.SCREEN_HEIGHT//2-125, 500, 100, "Ebony Wings",
                                   "Bombards in a circling zone.", "./assets/experience_gems.png", is_new=True)
        self.item_card2 = ItemCard(settings.SCREEN_WIDTH//2-250, settings.SCREEN_HEIGHT//2, 500, 100, "Ebony Wings",
                                   "Bombards in a circling zone.", "./assets/experience_gems.png", is_new=True)
        self.item_card3 = ItemCard(settings.SCREEN_WIDTH//2-250, settings.SCREEN_HEIGHT//2+125, 500, 100, "Ebony Wings",
                                   "Bombards in a circling zone.", "./assets/experience_gems.png", is_new=True)
        self.overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        self.overlay.fill((42, 42, 42))

        # Lista de botones
        self.buttons = [
            self.reroll_button,
            self.skip_button,
        ]

    # SE ENCARGA DE RECIBIR EL DICCIONARIO CON LOS 3 ITEMS ELEGIDOS Y REMPLAZA TODA LA INFO DE ESTOS EN LA ITEM_CARD

    def colocar_items(self, dic: dict):
        # Crear una lista para almacenar los ItemCard
        item_cards = []

        # Definir las posiciones para cada ItemCard
        posiciones = [
            (settings.SCREEN_WIDTH // 2 - 250, settings.SCREEN_HEIGHT // 2 - 125),
            (settings.SCREEN_WIDTH // 2 - 250, settings.SCREEN_HEIGHT // 2),
            (settings.SCREEN_WIDTH // 2 - 250, settings.SCREEN_HEIGHT // 2 + 125)
        ]

        # Iterar sobre el diccionario y las posiciones, hasta un máximo de 3 ítems
        for index, (key, item) in enumerate(dic.items()):
            if index < 3:  # Solo necesitamos los primeros 3 ítems
                x, y = posiciones[index]
                item_card = ItemCard(
                    x, y, 500, 100, str(item), item.description, item.image_path, is_new=True
                )
                item_cards.append(item_card)
        return item_cards

    def draw(self, item_cards):
        """Dibuja el menú de nivelación y sus botones en la pantalla."""
        self.screen.blit(self.overlay, (0, 0))

        self.container.draw(self.screen)
        self.title1.draw(self.screen)
        for item in item_cards:
            item.draw(self.screen)
        for button in self.buttons:
            button.draw(self.screen)

    def check_click(self, mouse_pos):
        """Comprueba si se ha hecho clic en alguno de los botones y devuelve el nombre de la opción."""
        if self.reroll_button.is_clicked(mouse_pos):
            return "reroll"
        elif self.skip_button.is_clicked(mouse_pos):
            return "skip"
        elif self.item_card1.is_clicked(mouse_pos):
            pass
            # return list(diccionario.keys())[0]  # Devuelve el primer ítem
        elif self.item_card2.is_clicked(mouse_pos):
            pass
            # return list(diccionario.keys())[1]  # Devuelve el segundo ítem
        elif self.item_card3.is_clicked(mouse_pos):
            pass
            # return list(diccionario.keys())[2]  # Devuelve el tercer ítem
        return None
