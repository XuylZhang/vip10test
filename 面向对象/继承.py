# 师傅
class Master(object):
    def __init__(self):
        self.kongfu = '五香煎饼果子配方'

    def make(self):
        print(f"运用Master{self.kongfu}制作煎饼果子")


# 学校类
class School(object):
    def __init__(self):
        self.kongfu = '香辣煎饼果子配方'

    def make(self):
        print(f'运用School{self.kongfu}制作煎饼果子')


# #徒弟
# class Prentice(School,Master):
#     pass
# xiaoming = Prentice()
# print(xiaoming.kongfu)
# xiaoming.make()

# 徒弟独创配方
class Prentice1(School, Master):
    def __init__(self):
        self.kongfu = '独创煎饼果子配方'
        # 私有属性
        self.__money = 2000

    # 私有方法
    def __print(self):
        print('我是私有方法')
        print(self.__money)
        print(self.kongfu)
        print('私有方法结束')

    def siyou(self):
        print(f'我是私有属性{self.__money}')
        self.__print()
    def get_money(self):
        return self.__money
    def set_money(self,num):
        if num > 0:
            self.__money = num
        else:
            return '输入错误'
    def make(self):
        self.__init__()
        print(f'运用Prentice{self.kongfu}制作煎饼果子')

    def master_make(self):
        Master.__init__(self)
        Master.make(self)

    def school_make(self):
        School.__init__(self)
        School.make(self)


# xiaoming1 = Prentice1()
# print(xiaoming1.kongfu)
# xiaoming1.make()
# xiaoming1.school_make()
# xiaoming1.master_make()

# 徒孙
class Tusun(Prentice1):
    pass
xiaodan = Tusun()
xiaodan.make()
xiaodan.school_make()
xiaodan.master_make()

#私有属性调用
xiaomim = Prentice1()
# print(xiaomim.__money) 报错
# xiaomim.__print() 报错
# xiaomim.siyou()
print(xiaomim.get_money())
xiaomim.set_money(300)
print(xiaomim.get_money())
print(xiaomim.set_money(-1))
# print(xiaodan.__money) 报错

print(xiaodan.get_money())
