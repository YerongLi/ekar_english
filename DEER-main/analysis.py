import json
import logging
import os
logging.basicConfig(filename='output.log', 
        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG)
# install_mp_handler()
logger = logging.getLogger(__name__)
logger.info(f'Logger start: {os.uname()[1]}')

dataset = json.load(open('extract_wiki/dataset_0.50_undir2dir_0.74.json'))
for i, datapoint in enumerate(dataset):
	# dict_keys(['pair', 'sim', 'entity', 'target', 'source', 'triple'])
	logger.info(datapoint['pairs'])
	if i > 5: break