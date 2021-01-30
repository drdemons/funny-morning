from dataclasses import dataclass
# sync требуется для того что бы клиент работал синхронно.
from telethon.sync import TelegramClient


@dataclass
class Client:
    api_id: int
    api_hash: str
    diggers: int

    def __create_client(self):
        client = TelegramClient('client', self.api_id, self.api_hash)
        client.start()
        return client

    def send_message(self, message):
        telegram_client = self.__create_client()
        return telegram_client.send_message(self.diggers, f'Всем привет! Внимание анекдот!\n{message}')
