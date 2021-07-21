import unittest

if __name__ == '__main__':
    Suite1 = unittest.defaultTestLoader.discover('unittest练习',pattern='test*.py',top_level_dir=None)

    discover1 = unittest.TestLoader().discover('unittest练习',pattern='test*.py',top_level_dir=None)

    runner = unittest.TextTestRunner()
    runner.run(Suite1)
    runner.run(discover1)