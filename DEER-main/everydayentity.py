import json
import logging
import os

logging.basicConfig(filename='output.log', 
        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG)
install_mp_handler()
logger = logging.getLogger(__name__)
logger.info(f'Logger start: {os.uname()[1]}')

data = json.load('train.json')
logger.info(type(data))