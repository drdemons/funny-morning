from dataclasses import dataclass
# sync требуется для того что бы клиент работал синхронно.
from telethon.sync import TelegramClient
import logging


@dataclass
class Client:
    api_id: int
    api_hash: str
    diggers: int
    message: str

    def __create_client(self):
        client = TelegramClient('client', self.api_id, self.api_hash)
        client.start()
        return client

    def send_message(self, message):
        telegram_client = self.__create_client()
        message_response = telegram_client.send_message(self.diggers, f'{self.message}\n{message}')
        logging.info(f'Send message response {message_response}')
        telegram_client.disconnect()
