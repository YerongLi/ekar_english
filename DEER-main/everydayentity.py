import json
import logging
import os
import pickle

from multiprocessing_logging import install_mp_handler

logging.basicConfig(filename='output.log', 
        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG)
logging.FileHandler('output.log', encoding='utf8')
install_mp_handler()
logger = logging.getLogger(__name__)
logger.info(f'Logger start: {os.uname()[1]}')
vocabulary = set()
with open('../train.json', encoding='utf-8') as f:
	for line in f.readlines():
		vocabulary.update(eval(line)['question'].split(':'))
with open('../test.json', encoding='utf-8') as f:
	for line in f.readlines():
		vocabulary.update(eval(line)['question'].split(':'))
with open('../validation.json', encoding='utf-8') as f:
	for line in f.readlines():
		vocabulary.update(eval(line)['question'].split(':'))
logger.info(len(vocabulary))

pickle.dump(vocabulary, open('vocab.pkl', 'wb'))