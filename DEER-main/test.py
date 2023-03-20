import logging
import multiprocessing
import tqdm
import time
from multiprocessing_logging import install_mp_handler

logging.basicConfig(filename='test.log', 
        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG)
install_mp_handler()
logger =  logging.getLogger(__name__)
logger.info('start')
def pt(i):
	# time.sleep()
	logger.info(i)
	return {i}
with multiprocessing.Pool(4) as p:
  r = list(tqdm.tqdm(p.imap(pt, range(30)), total=30))
print(result)


