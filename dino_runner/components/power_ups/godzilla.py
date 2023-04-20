from dino_runner.utils.constants import GODZILLA, GODZILLA_TYPE
from dino_runner.components.power_ups.power_up import PowerUp

class Godzilla(PowerUp):
    def __init__(self):
        self.image = GODZILLA
        self.type = GODZILLA_TYPE
        super().__init__(self.image, self.type)