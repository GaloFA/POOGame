"""This module contains the Monster class, which represents a monster entity in the game."""

from typing import List

from business.entities.entity import MovableEntity
from business.entities.interfaces import IDamageable, IHasPosition, IHasSprite, IMonster
from business.handlers.cooldown_handler import CooldownHandler
from business.handlers.collision_handler import CollisionHandler
from business.world.interfaces import IGameWorld, IPlayer
from presentation.sprite import Sprite


class Monster(MovableEntity, IMonster):
    """A monster entity in the game."""

    def __init__(self, src_x: int, src_y: int, sprite: Sprite):
        super().__init__(src_x, src_y, 2, sprite)
        self.__health: int = 10
        self.__damage = 10
        self.__attack_range = 50
        self.__attack_cooldown = CooldownHandler(1000)
        self._logger.debug("Created %s", self)

    def attack(self, target: IPlayer):
        """Attacks the target."""
        if not self.__attack_cooldown.is_action_ready():
            return

        if self._get_distance_to(target) < self.__attack_range:
            target.take_damage(self.damage_amount)
            self.__attack_cooldown.put_on_cooldown()

    @property
    def damage_amount(self):
        return self.__damage

    def __get_direction_towards_the_player(self, world: IGameWorld):
        direction_x = world.player.pos_x - self.pos_x
        if direction_x != 0:
            direction_x = direction_x // abs(direction_x)

        direction_y = world.player.pos_y - self.pos_y
        if direction_y != 0:
            direction_y = direction_y // abs(direction_y)

        return direction_x, direction_y

    #def __movement_collides_with_entities(
    #    self, dx: float, dy: float, entities: List[IHasSprite]
    #) -> bool:
    #    new_position = self.sprite.rect.move(dx, dy).inflate(-10, -10)
    #    return any(e.sprite.rect.colliderect(new_position) for e in entities)
    #
    #
    #
    #
    #
    #
    #

    def update(self, world: IGameWorld):
        direction_x, direction_y = self.__get_direction_towards_the_player(world)
        if (direction_x, direction_y) == (0, 0):
            return

        colliding_pairs = CollisionHandler.detect_monster_collisions(world.monsters)

        #dx, dy = direction_x * self.speed, direction_y * self.speed
        
        colliding_monsters = {monster for pair in colliding_pairs for monster in pair}

        if self not in colliding_monsters:
            self.move(direction_x, direction_y)

        if self in colliding_monsters:
            for monster_a, monster_b in colliding_pairs:
                if self == monster_a or self == monster_b:
                    closest_monster = min(
                        [monster_a, monster_b],
                        key=lambda m: (
                            (m.pos_x - world.player.pos_x) ** 2 + (m.pos_y - world.player.pos_y) ** 2
                        ),
                    )

                    closest_monster.move(direction_x, direction_y)

        if self.__health <= 0:
            world.remove_monster(self)

        self.attack(world.player)

        super().update(world)

    def __str__(self):
        return f"Monster(hp={self.health}, pos={self.pos_x, self.pos_y})"

    @property
    def health(self) -> int:
        return self.__health

    def take_damage(self, amount):
        self.__health = max(0, self.__health - amount)
        print(f"HEALTH:{self.__health}")
        self.sprite.take_damage()
