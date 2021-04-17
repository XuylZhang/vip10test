# try:
#     f = open("test.txt","r")
# except:
#     # open("test.txt","w")
#     print("文件不存在")
# finally:
#     f.close()



# try:
#     print(num)
# except BaseException:
#     print("有错误")



# try:
#     print(1/0)
#     print(num)
# except (ZeroDivisionError,IndexError,ImportError,NameError) as error:
#     print(error)

# try:
#     print(1)
# except Exception:
#     print('有错误')
# else:
#     print("我是else，没有错误")

try:
    f = open("test1.TXT","r")
except:
    f = open("test1.TXT","w")
else:
    print("我是else，没有错误")
finally:
    f.close()
    print("文件已关闭")

