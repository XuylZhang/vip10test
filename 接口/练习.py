
import requests,json

# get请求，params设置参数--字典
# urlstr = "https://www.wanandroid.com/article/query"
# paramdict = {"k":"Python"}
# r = requests.get(url = urlstr,params = paramdict)
# print(r.text)
# print(r.status_code) #状态码
# print(r.json)

#content自动解码gzip和deflate压缩
# r = requests.get("https://www.baidu.com")
# print(r.url)
# print(r.encoding) # 编码
# print(r.text)
# print(r.content) #获取返回内容，自动解码gzip
# print(r.headers)
# print(r.cookies)

#help
# help(requests)


# post请求

urlstr = "http://httpbin.org/post"

paramdict = {"qq群名":"selenium","qq群号":"106014970"}
#先导入 json 模块，用 dumps 方法转化成 json 格式
# paramjson = json.dumps(paramdict)
# r = requests.post(url=urlstr,data=paramjson)
# 使用json传参
r = requests.post(url=urlstr,json=paramdict)

print(r.text) # 获取结果

print(r.json()) # 以json的格式查看结果