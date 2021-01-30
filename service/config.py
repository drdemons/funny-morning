import yaml
import os
from glob import glob
import logging


def read():
    logging.info(os.environ['PROFILE'])
    with open(__change_config(), 'r') as config:
        try:
            return yaml.safe_load(config)
        except yaml.YAMLError as exc:
            logging.error(exc)


def __change_config():
    if os.environ['PROFILE'] == 'dev':
        return 'config.yml'
    if os.environ['PROFILE'] == 'prod':
        return glob('/run/secrets/config')[0]
