import logging

config = {
    'format': '[%(levelname)s][%(filename)s:%(lineno)d] %(message)s',
    'filename': 'log.log',
    'filemode': 'a',
    'level': logging.INFO
}

logging.basicConfig(**config)
