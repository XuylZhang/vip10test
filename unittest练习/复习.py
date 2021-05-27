import unittest

class TestFunT(unittest.TestCase):

    def setUp(self) -> None:
        self.a = 3
        self.b = 5

    def test_add(self):
        self.assertEqual(8,self.a + self.b)
    def test_sub(self):
        self.assertEqual(3,self.b - self.a)

if __name__ == '__main__':
    # unittest.main(verbosity=2)
    suite1 = unittest.TestSuite()
    suite1.addTest(TestFunT('test_add'))
    runner = unittest.TextTestRunner()
    runner.run(suite1)