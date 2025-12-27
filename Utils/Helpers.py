import string
import random

class Helpers:
    game1 = [{"LogicGameObjects": 2}, {"id": 1, "hp": 3000, "immun": True, "UltiPress": False, "UltiCharge": 0, "battleX": 3150, "battleY": 6725, "angle": 270}, {"id": 228, "hp": 3000, "immun": True, "UltiPress": False, "UltiCharge": 0, "battleX": 3150, "battleY": 3725, "angle": 180}]
    rooms = []

    def __init__(self):
        # Набор для хранения уникальных токенов
        self.generated_tokens = set()

    def randomStringDigits(self):
        """Генерирует уникальный случайный токен из букв и цифр длиной 40 символов"""
        lettersAndDigits = string.ascii_letters + string.digits
        while True:
            token = ''.join(random.choice(lettersAndDigits) for _ in range(40))
            if token not in self.generated_tokens:
                self.generated_tokens.add(token)
                return token

    def randomID(self):
        """Генерирует случайный 9-значный ID"""
        return int(''.join([str(random.randint(0, 9)) for _ in range(9)]))

    def randomClubID(self):
        """Генерирует случайный 9-значный ID для клуба"""
        return int(''.join([str(random.randint(0, 9)) for _ in range(9)]))