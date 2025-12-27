from Utils.Writer import Writer
from shared import connected_ips
import random


class LobbyInfoMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23457
        self.player = player

    def encode(self):
        ping_ms = random.randint(15, 60)  # фейк пинг
        ip_count = len(connected_ips)

        message = (
            f'Jump Brawl v28\n'
            f'TG: @JumpBrawll\n'
            f'Beta Test\n'
            f'Пинг: {ping_ms}ms\n'
            f'Онлайн: {ip_count}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n' # НЕ УБИРАЙ \n
        )

        self.writeVint(0)
        self.writeString(message)
        self.writeVint(0)
