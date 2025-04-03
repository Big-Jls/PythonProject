import logging
logger = logging.getLogger('__name__')
# logging.basicConfig(filename='test.log',level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# logger.error('出错了')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.setLevel('DEBUG')
logger.error('出错了')