# 导入
import requests,json
# # 发送请求
# urlstr = "http://www.wanandroid.com"
# r = requests.get(url=urlstr)
# # 打印
# print(r.text) #直接以str方式打印，不解码
# print(r.status_code)
# print(r.content) #自动解码

# urlstr = "http://www.wanandroid.com/article/query"
# paramsdict = {"k":"Android"}
#
# r = requests.get(url=urlstr,params=paramsdict)
#
# print(r.status_code)
# # print(r.text)
# print(r.headers)
# print(r.cookies)
# print(r.url)
# print(r.encoding)
# print(r.raw)
# print(r.raise_for_status())


# urlstr = "http://httpbin.org/post"
#
# paramsdict = {"微信群":"上班聊天摸鱼","群号":"123456789"}
# paramsjson = json.dumps(paramsdict)
#
# r = requests.post(url=urlstr,data=paramsjson)
# print(r.text)
#
# print(r.json())

# 准备数据
urlstr = "https://www.wanandroid.com/user/login"
# 发送请求
paramsdict = {"username":"xuyl","password":"123456"}
# header = {"User-Agent":"Mozilla/6.0"}
# 获取结果
# r = requests.post(url=urlstr,data=paramsdict,headers = header)
# print(r.text)
# print(r.headers)
# print(r.json()['data']['username'])


# 断言接口（1-状态码；2-错误码；3-错误提示信息；4-接口返回的某个关键字段）
# if r.status_code == 200 :
#     if r.json()['errorCode'] == 0:
#         if r.json()['data']['username'] == paramsdict['username']:
#             print('登录成功')
#     elif r.json()['errorCode'] == -1:
#         print(r.json()['errorMsg'])
# else:
#     print('请求失败')

