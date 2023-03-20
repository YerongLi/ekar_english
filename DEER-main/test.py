import logging
import multiprocessing
logging(filename='test.log')
logger =  multiprocessing.get_logger()

def print(i):
	logger.info(i)
with Pool(2) as p:
  _ = tqdm.tqdm(p.imap(print, range(30)), total=30)


