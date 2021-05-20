from myfun import *
import unittest


class TestMyFun(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('所有测试用例前的准备工作')

    @classmethod
    def tearDownClass(cls):
        print('所有测试用例后的清理工作')


    def setUp(self):
        print('一条测试用例前的准备工作')


    def tearDown(self):
        print('一条测试用例后的清理工作')


    @unittest.skip('临时跳过这个测试用例add')
    def test_add(self):
        self.assertEqual(3,add(1,2))
        self.assertNotEqual(4,add(1,2))# 测试add
        print('测试add')

    def test_minus(self):
        self.skipTest('跳过测试minus')
        self.assertEqual(1,minus(3,2))# 测试minus
        print('测试minus')
    def test_multi(self):
        self.assertEqual(8,multi(2,4))# 测试multi
        # self.assertEqual(6,multi(2,4))# 测试multi
        print('测试multi')
    def test_divide(self):
        self.assertEqual(3,divide(9,3))# 测试divide
        self.assertEqual(2.5,divide(5,2))
        print('测试divide')

if __name__ == '__main__':
    # test1 = TestMyFun()
    unittest.main(verbosity=2)