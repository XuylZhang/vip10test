
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
#
# urlstr = "http://httpbin.org/post"
#
# paramdict = {"qq群名":"selenium","qq群号":"106014970"}
# #先导入 json 模块，用 dumps 方法转化成 json 格式
# # paramjson = json.dumps(paramdict)
# # r = requests.post(url=urlstr,data=paramjson)
# # 使用json传参
# r = requests.post(url=urlstr,json=paramdict)
#
# print(r.text) # 获取结果---str类型
#
# print(r.json()) # 以json的格式查看结果
# print(r.json().get("origin"))


# # data传参
# urlstr = "https://www.wanandroid.com/user/login"
#
# headersdict1 = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
# headersdict = {"User-Agent":"Mozilla/5.0 "}
#
# paramjson = {"username":"xuyl","password":"123456"}
#
# # r = requests.post(url = urlstr,headers = headersdict, json = paramjson)
# r = requests.post(url=urlstr,data=paramjson)
#
# print(r.text)
# print(r.json()['data']['username'])
# if (r.json()['data']['username'] == paramjson['username']):
#     print('登陆成功')



# 发送https请求（ssl）----打开fiddler后报错不一样，降低requests版本 2.1.0 或 2.0.0
# ValueError: check_hostname requires server_hostname
# urlstr = "https://passport.cnblogs.com/user/signin"
# requests.packages.urllib3.disable_warnings()
# r = requests.get(urlstr,verify=False)
# print(r.status_code)



# session

# help(requests.session())

urlstr = "https://www.wanandroid.com/user/login"

headersdict1 = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
headersdict = {"User-Agent":"Mozilla/5.0 "}

s = requests.session()
paramjson = {"username":"xuyl","password":"123456"}

# r = requests.post(url = urlstr,headers = headersdict, json = paramjson)
r = s.post(url=urlstr,data=paramjson)

print("****",r.text)
# print(r.json()['data']['username'])
# if (r.json()['data']['username'] == paramjson['username']):
#     print('登陆成功')
r2 = s.get("https://www.wanandroid.com/lg/todo/list/0")

print("***",r2.text)