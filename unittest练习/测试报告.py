import HTMLTestRunner,unittest

filename = 'D:\\code\\vip10test\\report\\result.html'
# 打开报告
fp = open(filename,'wb')

runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'百度搜索测试报告',description=u'用例执行情况：')

Suite1 = unittest.defaultTestLoader.discover('unittest练习', pattern='test*.py', top_level_dir=None)

runner.run(Suite1)

# 关闭报告
fp.close()