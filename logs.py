import logging

def logs():
    logging.basicConfig(level=logging.INFO,format='%(name)s-%(asctime)s-%(levelname)s-%(message)s')
    logger = logging.getLogger('XUTest')
    return logger
logger = logs()
if __name__ == '__main__':
    logger.info('ceshi')