import unittest
from ddt import ddt,data,unpack
from logs import logger
list_dict1 = [{'value1':1,'value2':2},{'value1':3,'value2':4}]
# logger.info(list_dict1)

@ddt
class TestDdt1(unittest.TestCase):
    @data(*list_dict1)
    @unpack
    def test_ddt1(self,value1,value2):
        logger.info(f'value1:{value1},value2:{value2}')
        self.assertEqual(value1,value2)



if __name__ == '__main__':
    unittest.main(verbosity=2)