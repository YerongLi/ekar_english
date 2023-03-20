import json
import logging
import os
logging.basicConfig(filename='analysis.log', 
        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG)
# install_mp_handler()
logger = logging.getLogger(__name__)
logger.info(f'Logger start: {os.uname()[1]}')

dataset = json.load(open('extract_wiki/dataset_0.50_undir2dir_0.75.json'))
with open('pairs.txt', 'w') as f:
	for i, datapoint in enumerate(dataset):
		# dict_keys(['pair', 'sim', 'entity', 'target', 'source', 'triple'])
		k = 'pair'
		f.write(f'{datapoint["pair"][0].encode("utf-8"), datapoint["pair"][1].encode("utf-8")}\n')
		f.write(f'{datapoint["source"].encode("utf-8")}\n')
		if i > 200: break

logger.info(f'length {len(dataset)}')