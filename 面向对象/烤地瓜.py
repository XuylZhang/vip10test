# 地瓜类
class Sweet():
    # 属性：熟的状态、烤的时间、添加的调料
    def __init__(self):
        self.stu = "生的"
        self.time = 0
        self.seasonings = []
    # 方法：被烤
    def bake(self,time,sea):
        if 0 <= time <= 3:
            pass
        elif 3 < time <= 5 :
            self.stu = "半生不熟"
        elif 5 < time <= 8 :
            self.stu = "熟的"
        elif time > 8 :
            self.stu = "烤糊了"
        else:
            print("输入有误")
        self.time = time
        self.seasonings.append(sea)
    # 输出：地瓜加了什么调料，烤了多久，现在的状态
    def __str__(self):
        return f'烤地瓜中加了{self.seasonings}，烤了{self.time}分钟，现在是{self.stu}'
# 创建对象
s1 = Sweet()
# 烤地瓜
s1.bake(9,'胡椒粉')
print(s1)
