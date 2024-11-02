class Item:
    """Clase base que representa un ítem genérico con niveles y efectos."""

    def __init__(self, nombre, descripcion, tipo_efecto, mejoras, imagen=None, sprite_config=None):
        """
        Inicializa un ítem con nombre, descripción, tipo de efecto, mejoras por nivel,
        y opcionalmente una imagen o sprite con configuración.
        """
        self.nombre = nombre
        self.descripcion = descripcion
        self.tipo_efecto = tipo_efecto
        self.mejoras = mejoras
        self.nivel = 1
        self.imagen = imagen  # Ruta de la imagen o sprite
        self.sprite_config = sprite_config or {}  # Configuración opcional del sprite

    def configurar_sprite(self, ancho=16, alto=16, filas=1, columnas=1):
        """Configura las propiedades del sprite, como ancho y alto."""
        self.sprite_config['ancho'] = ancho
        self.sprite_config['alto'] = alto
        self.sprite_config['filas'] = filas
        self.sprite_config['columnas'] = columnas

    def obtener_sprite(self, fila, columna):
        """Calcula la posición del sprite en la imagen de sprites."""
        ancho_sprite = self.sprite_config['ancho']
        alto_sprite = self.sprite_config['alto']
        x = columna * ancho_sprite
        y = fila * alto_sprite
        return (x, y)

    def subir_nivel(self):
        """Sube el nivel del ítem si no ha alcanzado el nivel máximo."""
        if self.nivel < len(self.mejoras):
            self.nivel += 1
            return f"{self.nombre} ha subido al nivel {self.nivel}!"
        else:
            return f"{self.nombre} ya está en el nivel máximo."

    def obtener_valor_efecto(self):
        return self.mejoras[self.nivel - 1]

    def aplicar_efecto(self, jugador):
        pass

    def __str__(self):
        """Devuelve una representación en cadena del ítem."""
        return f"{self.nombre} (Nivel {self.nivel}): {self.descripcion}"


class ItemSalud(Item):
    """Ítem que proporciona mejoras en salud."""

    def __init__(self):
        super().__init__(
            nombre="Elixir de Salud",
            descripcion="Aumenta la salud del jugador.",
            tipo_efecto="salud",
            mejoras=[20, 40, 60, 80, 100],
            imagen="./assets/item2.png"
        )

    def aplicar_efecto(self, jugador):
        jugador.salud += self.obtener_valor_efecto()


class ItemVelocidad(Item):
    """Ítem que proporciona mejoras en velocidad."""

    def __init__(self):
        super().__init__(
            nombre="Bota de Velocidad",
            descripcion="Aumenta la velocidad de movimiento del jugador.",
            tipo_efecto="velocidad",
            mejoras=[2, 4, 6, 8, 10],
            imagen="./assets/item2.png"
        )

    def aplicar_efecto(self, jugador):
        jugador.velocidad += self.obtener_valor_efecto()


class ItemDanio(Item):
    """Ítem que proporciona mejoras en daño."""

    def __init__(self):
        super().__init__(
            nombre="Furia del Guerrero",
            descripcion="Aumenta el daño infligido por el jugador.",
            tipo_efecto="daño",
            mejoras=[5, 10, 15, 20, 25],
            imagen="./assets/item2.png"
        )

    def aplicar_efecto(self, jugador):
        jugador.danio += self.obtener_valor_efecto()


class ItemDefensa(Item):
    """Ítem que proporciona mejoras en defensa."""

    def __init__(self):
        super().__init__(
            nombre="Escudo del Valiente",
            descripcion="Aumenta la defensa del jugador.",
            tipo_efecto="defensa",
            mejoras=[3, 6, 9, 12, 15],
            imagen="./assets/item2.png"
        )

    def aplicar_efecto(self, jugador):
        jugador.defensa += self.obtener_valor_efecto()


class ItemExperiencia(Item):
    """Ítem que proporciona mejoras en experiencia ganada."""

    def __init__(self):
        super().__init__(
            nombre="Amuleto de Sabiduría",
            descripcion="Aumenta la experiencia ganada por el jugador.",
            tipo_efecto="experiencia",
            mejoras=[50, 100, 150, 200, 250],
            imagen="./assets/item2.png"
        )

    def aplicar_efecto(self, jugador):
        jugador.experiencia += self.obtener_valor_efecto()


class ItemAutocuracion(Item):
    """Ítem que mejora la autocuración del jugador."""

    def __init__(self):
        super().__init__(
            nombre="Anillo de Autocuración",
            descripcion="Aumenta la cantidad de salud recuperada automáticamente.",
            tipo_efecto="autocuracion",
            mejoras=[1, 2, 3, 4, 5],
            imagen="./assets/item2.png"
        )

    def aplicar_efecto(self, jugador):
        jugador.autocuracion += self.obtener_valor_efecto()


class ItemCriticos(Item):
    """Ítem que aumenta la probabilidad de ataques críticos."""

    def __init__(self):
        super().__init__(
            nombre="Capa de Sombra",
            descripcion="Aumenta la probabilidad de infligir daño crítico.",
            tipo_efecto="critico",
            mejoras=[1, 2, 3, 4, 5],  # Porcentaje o puntos de probabilidad
            imagen="./assets/item2.png"
        )

    def aplicar_efecto(self, jugador):
        jugador.probabilidad_critico += self.obtener_valor_efecto()


class ItemVelocidadAtaque(Item):
    """Ítem que mejora la velocidad de ataque del jugador."""

    def __init__(self):
        super().__init__(
            nombre="Guantes de Agilidad",
            descripcion="Aumenta la velocidad de ataque del jugador.",
            tipo_efecto="velocidad_ataque",
            mejoras=[1, 2, 3, 4, 5],
            imagen="./assets/item2.png"
        )

    def aplicar_efecto(self, jugador):
        jugador.velocidad_ataque += self.obtener_valor_efecto()
