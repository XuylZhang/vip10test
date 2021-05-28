from ddt import ddt,data,unpack
import unittest
from logs import logger
list1 = [1,2,3,4]
@ddt
class TestDdt(unittest.TestCase):
    @data(1)
    def test_ddt1(self,value1):
        logger.info(f'ddt1参数：{value1}')
        self.assertEqual(value1,1)

    @data(9,8,7)
    def test_ddt2(self,value1):
        logger.info(f'ddt2参数：{value1}')
        self.assertEqual(value1,4)

    @data(*list1)
    def test_ddt3(self,value1):
        logger.info(f'ddt3参数：{value1}')
        self.assertEqual(value1,3)

if __name__ == '__main__':
    unittest.main(verbosity=2)