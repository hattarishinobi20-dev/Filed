from Utils.Reader import BSMessageReader
from Packets.Messages.Server.Login.ServerHelloMessage import ServerHelloMessage
from Packets.Messages.Server.Login.LoginOkMessage import LoginOkMessage
from Packets.Messages.Server.Home.OwnHomeDataMessage import OwnHomeDataMessage

class ClientHelloMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_int()
        self.read_int()

        self.major = self.read_int()
        self.minor = self.read_int()
        self.build = self.read_int()

        self.fingerprint_sha = self.read_string()

        self.read_int()
        self.read_int()

    def process(self):
        if self.major != 13:
            self.player.err_code = 8
            LoginFailedMessage(self.client, self.player, "Your client is outdated, click below to download the new version!").send()
        else:
            ServerHelloMessage(self.client, self.player).send()
        LoginOkMessage(self.client, self.player).send()
        OwnHomeDataMessage(self.client, self.player).send()
