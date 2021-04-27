class Dad(object):
    def __init__(self):
        self.str1 = "父类"
    def print1(self):
        print(f"我是父类，我的属性是{self.str1}")

class Mom(object):
    def __init__(self):
        self.str1 = "母类"
    def print1(self):
        print(f"我是母类，我的属性是{self.str1}")

class Son(Dad,Mom):
    def __init__(self):
        self.str1 = "子类"
    def print1(self):
        self.__init__()
        print(f"我是子类，我的属性是{self.str1}")
    def dad_print1(self):
        Dad.__init__(self)
        Dad.print1(self)
    def mom_print1(self):
        Mom.__init__(self)
        Mom.print1(self)

class Grandson(Son):
    pass
# # 创建子类对象
# s = Son()
# s.print1()
# s.dad_print1()
# s.mom_print1()
#
# # 创建孙类对象
# gs = Grandson()
# gs.print1()
# gs.dad_print1()
# gs.mom_print1()

# super() 可以省去在子类中写父类的名称
class Son1(Dad):
    def __init__(self):
        self.str1 = "子类"
    def print1(self):
        self.__init__()
        print(f"我是子类，我的属性是{self.str1}")
    def dad_print1(self):
        super().__init__()
        super().print1()

# s1 = Son1()
# s1.print1()
# s1.dad_print1()

# 私有属性、私有方法

class Son2(Dad):
    __money = 3000
    def __print_money(self):
        print(f"我是私有方法，我有{self.__money}块钱")
    def get_money(self):
        return self.__money
    def set_money(self,num):
        if num < 0:
            print("输入错误，请重新输入")
        else:
            self.__money = num

s2 = Son2()
# print(s2.__money)
# s2.__print_money()

print(s2.get_money())
s2.set_money(-1)
print(s2.get_money())
s2.set_money(500)
print(s2.get_money())
