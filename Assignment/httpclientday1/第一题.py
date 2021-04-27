# 动物类
class Zoo():
    #属性：种类
    def __init__(self,name):
        self.name = name
    #方法：爱吃鱼，要喝水
    def interest(self,inter):
        print(f'{self.name}爱{inter}')
    def need(self,n):
        print(f'{self.name}要{n}')

cat1 = Zoo('小猫')
cat1.interest('吃鱼')
cat1.need('喝水')
