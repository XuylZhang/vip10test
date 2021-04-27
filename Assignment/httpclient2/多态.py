# 父类
class Dog(object):
    def print1(self):
        print("我是父类，没啥用")
# 多个子类重写父类方法
class RedDog(Dog):
    def print1(self):
        print("我是RedDog")
class BlueDog(Dog):
    def print1(self):
        print("我是BlueDog")

# 将不同的子类对象传给调用者
class Man():
    def dog(self,m):
        print(f"我是调用者--------------")
        m.print1()
# 创建不同的子类
a = RedDog()
b = BlueDog()
# 将不同的子类对象传给调用者
m = Man()
m.dog(a)
m.dog(b)

