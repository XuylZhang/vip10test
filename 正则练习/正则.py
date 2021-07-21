"""
功能描述：
创建者：xuyanliang
创建时间：
实现步骤：
    1-
    2-
    3-

"""
import re,os
report_file = os.path.dirname(__file__) + "\\126Test20210720200530_report.html"
with open(report_file,'r',encoding='utf-8') as f:
    report_list = f.readlines()
    report_data = "\n".join(report_list)
print(report_data)

kk = re.compile('开始时间 : </strong> (\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})</p>')
# kk = re.compile('开始时间 : </strong>(.*?)</p>')
result = kk.findall(report_data)
print(result)

