import unittest

class TestFun(unittest.TestCase):
    def setUp(self):
        self.a = 20
        self.b = 10

    def test_add(self):
        result = self.a + self.b
        self.assertEqual(result,30)
        print('测试add')
    def test_sub(self):
        result = self.a - self.b
        self.assertEqual(result,10)
        print('测试sub')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestFun('test_add'))
    runner = unittest.TextTestRunner()
    runner.run(suite)