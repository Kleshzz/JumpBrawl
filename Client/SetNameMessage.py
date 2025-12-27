from Logic.Commands.Server.LogicChangeAvatarNameCommand import LogicChangeAvatarNameCommand
from Server.Home.AvatarNameChangeFailedMessage import AvatarNameChangeFailedMessage
from Utils.Reader import BSMessageReader

class SetNameMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.username = self.read_string()
        self.state = self.read_Vint()

    def process(self):
        if not self.username:
            AvatarNameChangeFailedMessage(self.client, self.player).send()
            return
        
        if not (2 <= len(self.username) <= 20):
            AvatarNameChangeFailedMessage(self.client, self.player).send()
            return
        
        self.player.name = self.username
        LogicChangeAvatarNameCommand(self.client, self.player, 0).send()