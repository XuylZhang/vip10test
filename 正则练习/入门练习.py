"""
功能描述：
创建者：xuyanliang
创建时间：
实现步骤：
    1-
    2-
    3-

"""
import re
str1 = "one1two2three3four4"

kk = re.compile("\d")
result = kk.findall(str1)
print(result)