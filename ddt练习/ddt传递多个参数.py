
import unittest
from ddt import ddt,data,unpack

data_list = [[1,2],[3,4]]

@ddt
class TestDdt(unittest.TestCase):

    @data((1,1))
    @unpack
    def test_ddt1(self,value1,value2):
        print('---',value1,value2)
        self.assertEqual(value1,value2)


    @data([1,2],[3,3])
    @unpack
    def test_ddt2(self,value1,value2):
        print('+++',value1,value2)
        self.assertEqual(value1,value2)

    @data(*data_list)
    @unpack
    def test_add3(self,value1,value2):
        print('===',value1,value2)
        self.assertEqual(value1,value2)
if __name__ == '__main__':
    unittest.main(verbosity=2)
