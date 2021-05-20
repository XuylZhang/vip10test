import  requests,json
# 准备数据
# urlstr1 = "https://www.wanandroid.com/user/login"
# urlstr2 = "https://www.wanandroid.com/lg/todo/list/0"
# # 发送请求
# paramsdict = {"username":"xuyl","password":"123456"}
#
# s = requests.session()
#
# r1 = s.post(urlstr1,data=paramsdict)
# print('*****',r1.text)
#
# r2 = s.get(urlstr2)
# print('***',r2.text)

# cookie
urlstr1 = "https://www.wanandroid.com/user/login"
urlstr2 = "https://www.wanandroid.com/lg/todo/list/0"
# 发送请求
paramsdict = {"username":"xuyl","password":"123456"}


r1 = requests.post(urlstr1,data=paramsdict)
print('*****',r1.text)
# cookie1 = r1.cookies

# print(r1.cookies)
# cookie1 = {
#     "JSESSIONID":r1.cookies['JSESSIONID']
# }
# r2 = requests.get(urlstr2 , cookies = cookie1)
# print('***',r2.text)

header2 = {
    'cookie':'JSESSIONID='+r1.cookies['JSESSIONID']
}

r2 = requests.get(urlstr2,headers = header2)
result = r2.text.find('已完成')
if result != -1 :
    print("success")