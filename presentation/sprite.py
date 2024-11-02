"""Module for the Sprite class."""

import pygame

import settings
from presentation.tileset import Tileset


class Sprite(pygame.sprite.Sprite):
    """A class representing a sprite."""

    def __init__(self, image: pygame.Surface, rect: pygame.Rect, *groups):
        self._image: pygame.Surface = image
        self._rect: pygame.Rect = rect
        super().__init__(*groups)
        self.__is_in_damage_countdown = 0
        self.__original_image: pygame.Surface = image

    @property
    def image(self) -> pygame.Surface:
        """The image of the sprite.

        Returns:
            pygame.Surface: The image of the sprite.
        """
        return self._image

    @property
    def rect(self) -> pygame.Rect:
        """The rect of the sprite.

        Returns:
            pygame.Rect: The rect of the sprite. A rect is a rectangle
            that defines the position and size of the sprite.
        """
        return self._rect

    def update_pos(self, pos_x: float, pos_y: float):
        """Update the position of the sprite.

        Args:
            pos_x (float): The x-coordinate of the sprite.
            pos_y (float): The y-coordinate of the sprite.
        """
        self._rect.center = (int(pos_x), int(pos_y))

    def __restore_image(self):
        self._image = self.__original_image.copy()

    def __change_color(self, color: tuple[int, int, int]):
        self._image = self.__original_image.copy()  # Make a copy of the original image
        # Change color pylint: disable=E1101
        self._image.fill(color, special_flags=pygame.BLEND_MULT)
        self._image.set_colorkey((0, 0, 0))  # Set transparency if necessary

    def __decrease_damage_countdown(self):
        self.__is_in_damage_countdown -= 1
        if self.__is_in_damage_countdown <= 0:
            self.__is_in_damage_countdown = 0
            self.__restore_image()

    def take_damage(self):
        """Take damage."""
        self.__change_color((255, 0, 0))
        self.__is_in_damage_countdown = 30

    def update(self, *args, **kwargs):
        """Update the sprite behavior"""
        super().__init__(*args, **kwargs)
        if self.__is_in_damage_countdown > 0:
            self.__decrease_damage_countdown()


class PlayerSprite(Sprite):
    """A class representing the player sprite."""

    ASSET_IDLE = "./assets/adventurer-idle-00.png"
    # A new asset for the running animation
    ASSET_RUN = "./assets/character/Run.png"

    TILE_WIDTH = 64
    TILE_HEIGHT = 64
    IDLE_COLUMNS = 4
    RUN_COLUMNS = 6

    def __init__(self, pos_x: float, pos_y: float):
        image: pygame.Surface = pygame.image.load(
            PlayerSprite.ASSET_IDLE).convert_alpha()
        image = pygame.transform.scale(image, settings.TILE_DIMENSION)
        rect: pygame.Rect = image.get_rect(center=(int(pos_x), int(pos_y)))

        super().__init__(image, rect)

class ZombieSprite(Sprite):
    """A class representing the zombie sprite."""

    ASSET = "./assets/entities/monsters/zombie/zombie.png"
    TILE_WIDTH = 20
    TILE_HEIGHT = 26
    SIZE_MULTIPLIER = 4

    def __init__(self, pos_x: float, pos_y: float):
        tileset = Tileset(ZombieSprite.ASSET, ZombieSprite.TILE_WIDTH * ZombieSprite.SIZE_MULTIPLIER,
                          ZombieSprite.TILE_HEIGHT * ZombieSprite.SIZE_MULTIPLIER, 1, 1)

        image: pygame.Surface = tileset.get_tile(0)
        rect: pygame.Rect = image.get_rect(center=(int(pos_x), int(pos_y)))

        super().__init__(image, rect)

class SkeletonSprite(Sprite):
    """A class representing the skeleton sprite."""

    ASSET = "./assets/entities/monsters/skeleton/skeleton.png"
    TILE_WIDTH = 22
    TILE_HEIGHT = 32
    SIZE_MULTIPLIER = 4

    def __init__(self, pos_x: float, pos_y: float):
        tileset = Tileset(SkeletonSprite.ASSET, SkeletonSprite.TILE_WIDTH * SkeletonSprite.SIZE_MULTIPLIER,
                          SkeletonSprite.TILE_HEIGHT * SkeletonSprite.SIZE_MULTIPLIER, 1, 1)

        image: pygame.Surface = tileset.get_tile(0)
        rect: pygame.Rect = image.get_rect(center=(int(pos_x), int(pos_y)))

        super().__init__(image, rect)

class OrcSprite(Sprite):
    """A class representing the orc sprite."""

    ASSET = "./assets/entities/monsters/orc/orc.png"
    TILE_WIDTH = 22
    TILE_HEIGHT = 16
    SIZE_MULTIPLIER = 5

    def __init__(self, pos_x: float, pos_y: float):
        tileset = Tileset(OrcSprite.ASSET, OrcSprite.TILE_WIDTH * OrcSprite.SIZE_MULTIPLIER,
                          OrcSprite.TILE_HEIGHT * OrcSprite.SIZE_MULTIPLIER, 1, 1)

        image: pygame.Surface = tileset.get_tile(0)
        rect: pygame.Rect = image.get_rect(center=(int(pos_x), int(pos_y)))

        super().__init__(image, rect)

class WerewolfSprite(Sprite):
    """A class representing the werewolf sprite."""

    ASSET = "./assets/entities/monsters/werewolf/werewolf.png"
    TILE_WIDTH = 36
    TILE_HEIGHT = 32
    SIZE_MULTIPLIER = 3

    def __init__(self, pos_x: float, pos_y: float):
        tileset = Tileset(WerewolfSprite.ASSET, WerewolfSprite.TILE_WIDTH * WerewolfSprite.SIZE_MULTIPLIER,
                          WerewolfSprite.TILE_HEIGHT * WerewolfSprite.SIZE_MULTIPLIER, 1, 1)

        image: pygame.Surface = tileset.get_tile(0)
        rect: pygame.Rect = image.get_rect(center=(int(pos_x), int(pos_y)))

        super().__init__(image, rect)

class BulletSprite(Sprite):
    """A class representing the bullet sprite."""

    def __init__(self, pos_x: float, pos_y: float):
        image = pygame.Surface(
            (5, 5), pygame.SRCALPHA)  # pylint: disable=E1101
        pygame.draw.circle(image, (255, 255, 0), (2, 2), 5)
        rect: pygame.Rect = image.get_rect(center=(int(pos_x), int(pos_y)))

        super().__init__(image, rect)


class ExperienceGemSprite(Sprite):
    """A class representing the experience gem sprite."""

    ASSET = "./assets/experience_gems.png"

    def __init__(self, pos_x: float, pos_y: float):
        tileset = Tileset(
            ExperienceGemSprite.ASSET, settings.TILE_HEIGHT, settings.TILE_HEIGHT, 2, 2
        )
        image: pygame.Surface = tileset.get_tile(0)
        rect: pygame.Rect = image.get_rect(center=(int(pos_x), int(pos_y)))

        super().__init__(image, rect)
