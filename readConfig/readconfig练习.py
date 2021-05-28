
# 导包
import configparser,os
from logs import logger
# 实例化一个configparser对象来读取目标文件内容
conf = configparser.ConfigParser()
# 读取文件
file_path = os.path.dirname(os.path.dirname(__file__)) + r'/config.ini'
conf.read(file_path)

# 读取文件内容
# 1、sections
sections = conf.sections()
logger.info(f'config文件中sections：{sections}')

# 2、获取XXsection下的options
options = conf.options('mysql')
logger.info(f'mysql的options：{options}')

# 3、获取XXsection下的键值对
items = conf.items('mysql')
logger.info(f'mysql的items：{items}')

# 4、获取XXsection下的XXoption
option1 = conf.get('mysql','host')
logger.info(f'mysql下的host：{option1}')