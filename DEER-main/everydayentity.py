import json
import logging
import os

from multiprocessing_logging import install_mp_handler

logging.basicConfig(filename='output.log', 
        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG)
install_mp_handler()
logger = logging.getLogger(__name__)
logger.info(f'Logger start: {os.uname()[1]}')

data = json.loads(open('../train.json', encoding='utf-8'))
logger.info(type(data))