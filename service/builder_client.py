from service.slask_client import SClient
from service.telegram_client import TClient


def __clients():
    return {
        'telegram': __tclient_build,
        'slack': __sclient_build
    }


def __tclient_build(user_config):
    clients_ = user_config['clients']
    telegram = clients_['telegram']
    message = user_config['message']
    return TClient(telegram['api_id'],
                   telegram['api_hash'],
                   telegram['group_id'],
                   message['text'])


def __sclient_build(user_config):
    clients_ = user_config['clients']
    slack_ = clients_['slack']
    message = user_config['message']
    return SClient(
        slack_['token'],
        slack_['channel'],
        message['text']
    )


def build(user_config):
    clients_props = user_config['clients']
    keys = clients_props.keys()
    return [__clients()[key](user_config) for key in keys]
