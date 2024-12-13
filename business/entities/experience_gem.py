"""Module for the ExperienceGem class."""

from business.entities.entity import Entity
from business.entities.interfaces import IExperienceGem
from presentation.sprite import ExperienceGemSprite, SpeedGemSprite, DamageGemSprite, DefenceGemSprite, HealthGemSprite


class ExperienceGem(Entity, IExperienceGem):
    """Represents an experience gem in the game world."""

    def __init__(self, pos_x: float, pos_y: float, amount: int):
        super().__init__(pos_x, pos_y, ExperienceGemSprite(pos_x, pos_y))
        self.__amount = amount

    def json_format(self):
        return {
            'pos_x': self.pos_x,
            'pos_y': self.pos_y,
            'amount': self.__amount,
        }

    @staticmethod
    def load_experience_gem_from_json(gem_data) -> IExperienceGem:
        """Creates an experience gem from JSON data."""
        src_x = gem_data['pos_x']
        src_y = gem_data['pos_y']
        amount = gem_data['amount']

        return ExperienceGem(src_x, src_y, amount)

    @property
    def amount(self) -> int:
        return self.__amount

    def __str__(self):
        return f"ExperienceGem(amount={self.__amount}, pos=({self.pos_x}, {self.pos_y}))"


class SpeedGem(Entity, IExperienceGem):
    """Gema temporal que incrementa la velocidad del jugador"""

    def __init__(self, pos_x: float, pos_y: float, amount: int, speed_boost: int, duration: int):
        super().__init__(pos_x, pos_y, SpeedGemSprite(pos_x, pos_y))
        self.__speed_boost = speed_boost
        self.__duration = duration
        self.__amount = amount

    def json_format(self):
        return {
            'pos_x': self.pos_x,
            'pos_y': self.pos_y,
            'amount': self.__amount,
            'boost': self.__speed_boost,
            'duration': self.__duration,
        }

    @staticmethod
    def load_experience_gem_from_json(gem_data) -> IExperienceGem:
        """Creates an experience gem from JSON data."""
        src_x = gem_data['pos_x']
        src_y = gem_data['pos_y']
        amount = gem_data['amount']
        boost = gem_data['boost']
        duration = gem_data['duration']

        return SpeedGem(src_x, src_y, amount, boost, duration)

    def apply_effect(self, player):
        """Applies a temporary speed boost to the player."""
        pass

    @property
    def amount(self) -> int:
        return self.__amount

    def __str__(self):
        return (f"SpeedGem(amount={self.amount}, pos=({self.pos_x}, {self.pos_y}), "
                f"speed_boost={self.__speed_boost}, duration={self.__duration})")


class DamageGem(Entity, IExperienceGem):
    """Gema temporal que incrementa el daño del jugador"""

    def __init__(self, pos_x: float, pos_y: float, amount: int, damage_boost: int, duration: int):
        super().__init__(pos_x, pos_y, DamageGemSprite(pos_x, pos_y))
        self.__damage_boost = damage_boost
        self.__duration = duration
        self.__amount = amount

    def json_format(self):
        return {
            'pos_x': self.pos_x,
            'pos_y': self.pos_y,
            'amount': self.__amount,
            'boost': self.__damage_boost,
            'duration': self.__duration,
        }

    @staticmethod
    def load_experience_gem_from_json(gem_data) -> IExperienceGem:
        """Creates an experience gem from JSON data."""
        src_x = gem_data['pos_x']
        src_y = gem_data['pos_y']
        amount = gem_data['amount']
        boost = gem_data['boost']
        duration = gem_data['duration']

        return DamageGem(src_x, src_y, amount, boost, duration)

    def apply_effect(self, player):
        """Applies a temporary damage boost to the player."""
        pass

    @property
    def amount(self) -> int:
        return self.__amount

    def __str__(self):
        return (f"DamageGem(amount={self.amount}, pos=({self.pos_x}, {self.pos_y}), "
                f"damage_boost={self.__damage_boost}, duration={self.__duration})")


class DefenceGem(Entity, IExperienceGem):
    """Gema temporal que incrementa la defensa del jugador"""

    def __init__(self, pos_x: float, pos_y: float, amount: int, defence_boost: int, duration: int):
        super().__init__(pos_x, pos_y, DefenceGemSprite(pos_x, pos_y))
        self.__defence_boost = defence_boost
        self.__duration = duration
        self.__amount = amount

    def json_format(self):
        return {
            'pos_x': self.pos_x,
            'pos_y': self.pos_y,
            'amount': self.__amount,
            'boost': self.__defence_boost,
            'duration': self.__duration,
        }

    @staticmethod
    def load_experience_gem_from_json(gem_data) -> IExperienceGem:
        """Creates an experience gem from JSON data."""
        src_x = gem_data['pos_x']
        src_y = gem_data['pos_y']
        amount = gem_data['amount']
        boost = gem_data['boost']
        duration = gem_data['duration']

        return DefenceGem(src_x, src_y, amount, boost, duration)

    def apply_effect(self, player):
        """Applies a temporary defence boost to the player."""
        pass

    @property
    def amount(self) -> int:
        return self.__amount

    def __str__(self):
        return (f"DefenceGem(amount={self.amount}, pos=({self.pos_x}, {self.pos_y}), "
                f"defence_boost={self.__defence_boost}, duration={self.__duration})")


class HealthGem(Entity, IExperienceGem):
    """Gema que incrementa la vida del jugador"""

    def __init__(self, pos_x: float, pos_y: float, amount: int, health_boost: int, duration: int):
        super().__init__(pos_x, pos_y, HealthGemSprite(pos_x, pos_y))
        self.__health_boost = health_boost
        self.__duration = duration
        self.__amount = amount

    def json_format(self):
        return {
            'pos_x': self.pos_x,
            'pos_y': self.pos_y,
            'amount': self.__amount,
            'boost': self.__health_boost,
            'duration': self.__duration,
        }

    @staticmethod
    def load_experience_gem_from_json(gem_data) -> IExperienceGem:
        """Creates an experience gem from JSON data."""
        src_x = gem_data['pos_x']
        src_y = gem_data['pos_y']
        amount = gem_data['amount']
        boost = gem_data['boost']
        duration = gem_data['duration']

        return HealthGem(src_x, src_y, amount, boost, duration)

    def apply_effect(self, player):
        """Applies a temporary defence boost to the player."""
        pass

    @property
    def amount(self) -> int:
        return self.__amount

    def __str__(self):
        return (f"DefenceGem(amount={self.amount}, pos=({self.pos_x}, {self.pos_y}), "
                f"defence_boost={self.__health_boost}, duration={self.__duration})")
