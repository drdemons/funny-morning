from dataclasses import dataclass
from slack_sdk import WebClient


@dataclass
class SClient:
    token: str
    channel: str
    message: str

    def send_message(self, message):
        client = WebClient(self.token)
        client.chat_postMessage(
            channel=f'#{self.channel}',
            text=f'{self.message}\n{message}')
