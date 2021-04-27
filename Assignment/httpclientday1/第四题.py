# 弹药不足异常类
class NotEnoughException(Exception):
    def __init__(self,f_name,num):
        self.f_name = f_name
        self.num = num
    def __str__(self):
        return f'{self.f_name}中弹药不足{self.num}发'

# 士兵类
class Man():
    #属性：士兵名字
    def __init__(self,name):
        self.name = name
    #方法1：开火
    def fire(self,item,num):
        # 弹药不足发射完所有子弹，弹药足够发射指定数目弹药
        try:
            if item.num-num <0:
                raise NotEnoughException(item.name,num)
        except NotEnoughException as result:
            print(result)
            print(f'士兵{self.name}用{item.name}开火，发射了{item.num}发子弹')
            item.fire_bullet(item.num)
        else:
            print(f'士兵{self.name}用{item.name}开火，发射了{num}发子弹')
            item.fire_bullet(num)
        print(item)
    #方法2：给枪填子弹
    def add(self,item,num):
        item.add_bullet(num)
        print(f'士兵{self.name}给{item.name}填装了{num}发子弹')
        print(item)
# 枪类：
class Gun():
    #属性：枪名字、子弹数量
    def __init__(self,name,num):
        self.name = name
        self.num = num
    #方法1：发射子弹
    def fire_bullet(self,a):

            self.num -= a
    # 方法2：填装子弹
    def add_bullet(self,b):
        self.num += b
    def __str__(self):
        return f'{self.name}中还有{self.num}发子弹'

# 实例化枪
ak47 = Gun('AK47',30)
M16 = Gun('M16',40)
# 实例化士兵
xiaoming = Man('xiaoming')
#士兵开枪
xiaoming.fire(M16,50)
xiaoming.fire(ak47,10)
#士兵给枪填子弹
xiaoming.add(ak47,20)

