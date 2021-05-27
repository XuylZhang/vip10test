import unittest
from ddt import ddt,data,unpack
from logs import loger
list_dict1 = [{'value1':1,'value2':2},{'value3':3,'value4':4}]
loger.info(list_dict1)

# @ddt
# class TestDdt1(unittest.TestCase):
#     @data()
