import logging
import multiprocessing
import tqdm
from multiprocessing_logging import install_mp_handler

logging.basicConfig(filename='test.log', 
        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG)
install_mp_handler()
logger =  multiprocessing.get_logger(__name_)
logger.info('start')
def p(i):
	logger.info(i)
with multiprocessing.Pool(2) as p:
  _ = tqdm.tqdm(p.imap(p, range(30)), total=30)


