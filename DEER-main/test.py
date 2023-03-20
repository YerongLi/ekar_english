import logging
import multiprocessing

logging.basicConfig(filename='test.log', 
        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG)

logger =  multiprocessing.get_logger()

def print(i):
	logger.info(i)
with Pool(2) as p:
  _ = tqdm.tqdm(p.imap(print, range(30)), total=30)


