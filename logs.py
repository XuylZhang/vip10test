import logging

def logs():
    logging.basicConfig(level=logging.INFO,format='%(name)s-%(asctime)s-%(levelname)s-%(message)s')
    loger = logging.getLogger('XUTest')
    return loger
loger = logs()
if __name__ == '__main__':
    loger.info('ceshi')