import time
from datetime import datetime

import schedule
import logging
import config
import generator
from telegram_client import Client


def job(user_config):
    telegram = user_config['telegram']
    client = Client(telegram['api_id'],
                    telegram['api_hash'],
                    telegram['group_id'])

    anecdote = generator.generate()
    logging.info(f'received anecdote {anecdote}\n')
    message_response = client.send_message(anecdote)
    logging.info(f'Send message response {message_response}')


def weekday_job(name_job, params, send_time=None):
    week = datetime.today().weekday()
    if send_time is not None and week < 4:
        schedule.every().day.at(send_time).do(name_job, params)


def main():
    user_config = config.read()
    scheduler = user_config['scheduler']
    weekday_job(job, user_config, scheduler['time'])

    while True:
        schedule.run_pending()
        time.sleep(scheduler['sleep'])


if __name__ == '__main__':
    logging.info('Start service complete')
    main()

