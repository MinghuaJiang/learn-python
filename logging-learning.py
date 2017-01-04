import logging

logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s %(message)s')
logging.info("hello world")
logging.warn("something wrong")
logging.error("exception occured")
