# 人类
class Member():
    # 属性：姓名、体重
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
    # 方法1：跑步（减0.5公斤）
    def run(self,n):
        for i in range(1,n+1):
            self.weight -= 0.5
        print(f"{self.name}跑了{n}次步，减了{0.5*n}公斤")
    # 方法2：吃东西（增加1公斤）
    def eat(self,n):
        for i in range(1,n+1):
            self.weight += 1
        print(f"{self.name}吃了{n}次东西，增加了{n}公斤")
    # 输出：××的体重是××公斤
    def __str__(self):
        return f"{self.name}的体重是{self.weight}公斤"

# 创建小明对象
xiaoming = Member('xiaoming',75)
print(xiaoming)
# 跑步减肥
xiaoming.run(3)
print(xiaoming)
# 吃饭增肥
xiaoming.eat(2)
print(xiaoming)

# 创建小美对象
xiaomei = Member('xiaomei',45)
print(xiaomei)
