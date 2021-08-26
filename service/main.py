import logging
import time
from datetime import datetime

import schedule

import config
import generator
from service.builder_client import build


def job(user_config):
    clients = build(user_config)

    anecdote = generator.generate()
    logging.info(f'received anecdote {anecdote}\n')
    for client in clients:
        logging.info(client)
        client.send_message(anecdote)


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
