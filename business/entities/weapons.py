"""Module of the weapons"""

import math
from abc import abstractmethod
from business.world.interfaces import IGameWorld
from business.handlers.cooldown_handler import CooldownHandler
from business.entities.bullet import Bullet

class Weapon():
    """Represents the weapons"""
    def __init__(self, bullet_name: str, shoot_cooldown: int, bullet_speed: float, bullet_damage: int):
        self.__bullet_name = bullet_name
        self.__shoot_cooldown = shoot_cooldown
        self.__bullet_speed = bullet_speed
        self.__bullet_damage = bullet_damage
        self._cooldown_handler = CooldownHandler(shoot_cooldown)

    @property
    def bullet_name(self):
        """Returns the level bullet name of the weapon"""
        return self.__bullet_name

    @property
    def shoot_cooldown(self):
        """Returns the shoot cooldown of the weapon"""
        return self.__shoot_cooldown

    @property
    def bullet_speed(self):
        """Returns the bullet speed of the weapon"""
        return self.__bullet_speed

    @property
    def bullet_damage(self):
        """Returns the bullet damage of the weapon"""
        return self.__bullet_damage

    @property
    def cooldown_handler(self):
        """Returns the cooldown handler of the weapon"""
        return self._cooldown_handler


    @abstractmethod
    def shoot(self, world: IGameWorld):
        """Abstract method to shoot a bullet"""
        pass

class PistolWeapon(Weapon):
    """Class that represents a pistol weapon"""

    def __init__(self):
        super().__init__("PistolBullet", shoot_cooldown=500, bullet_speed=5.0, bullet_damage=10)

    def shoot(self, world: IGameWorld, src_x: float, src_y: float, target_x: float, target_y: float):
        if self._cooldown_handler.is_action_ready():
            bullet = Bullet(src_x, src_y, target_x, target_y, self.bullet_speed)
            world.add_bullet(bullet)
            self.cooldown_handler.put_on_cooldown()

class ShotgunWeapon(Weapon):
    """Class that represents a shotgun weapon"""

    def __init__(self):
        super().__init__("ShotgunBullet", shoot_cooldown=600, bullet_speed=4.0, bullet_damage=10)

    def shoot(self, world: IGameWorld, src_x: float, src_y: float, target_x: float, target_y: float):
        if self.cooldown_handler.is_action_ready():
            base_dir_x = target_x - src_x
            base_dir_y = target_y - src_y
            base_distance = math.hypot(base_dir_x, base_dir_y)

            if base_distance > 0:
                base_dir_x /= base_distance
                base_dir_y /= base_distance
            
            for angle_offset in [-0.1, -0.05, 0, 0.05, 0.1]:
                offset_dir_x = base_dir_x * math.cos(angle_offset) - base_dir_y * math.sin(angle_offset)
                offset_dir_y = base_dir_x * math.sin(angle_offset) + base_dir_y * math.cos(angle_offset)

                bullet = Bullet(src_x, src_y, 
                                src_x + offset_dir_x * self.bullet_speed, 
                                src_y + offset_dir_y * self.bullet_speed, 
                                self.bullet_speed)
                world.add_bullet(bullet)

            self.cooldown_handler.put_on_cooldown()

class MinigunWeapon(Weapon):
    """Class that represents a minigun weapon"""

    def __init__(self):
        super().__init__("MinigunBullet", shoot_cooldown=100, bullet_speed=6.0, bullet_damage=8)

    def shoot(self, world: IGameWorld, src_x: float, src_y: float, target_x: float, target_y: float):
        if self._cooldown_handler.is_action_ready():
            bullet = Bullet(src_x, src_y, target_x, target_y, self.bullet_speed)
            world.add_bullet(bullet)
            self.cooldown_handler.put_on_cooldown()
