# 面积不足异常类练习
class NotEnoughError(Exception):
    # 属性：家具、家具面积、房屋剩余面积
    def __init__(self,f_name,f_area,r_area):
        self.f_name = f_name
        self.f_area = f_area
        self.r_area = r_area
    # 返回：剩余面积不足以放下家具面积的家具
    def __str__(self):
        return f'房屋剩余{self.r_area}平米,不足以放下{self.f_area}平米的{self.f_name}'

# 房子类
class House():
    # 属性：户型、总面积、家具列表、剩余面积
    def __init__(self,type,area):
        self.type = type
        self.c_area = area
        self.furnitrue = []
        self.r_area = area
    # 方法：放家具
    def addFurniture(self,item):
        try:
            if self.r_area-item.area < 0 :
                raise NotEnoughError(item.name,item.area,self.r_area)
        except NotEnoughError as result:
            print(result)
        else:
            self.r_area -= item.area
            self.furnitrue.append(item.name)
    # 输出：户型、总面积、剩余面积、家具名称列表
    def __str__(self):
        return f'户型{self.type}，总面积{self.c_area}平米，剩余面积{self.r_area}平米，家具列表{self.furnitrue}'
# 家具类：
class Furnitrue():
    # 属性：名称、占地面积
    def __init__(self,name,area):
        self.name = name
        self.area = area

# 创建房子对象
house1 = House('两室一厅',80)
print(house1)
# 创建家具对象：床、衣柜、餐桌
bed = Furnitrue('床',4)
closet = Furnitrue('衣柜',2)
table = Furnitrue('餐桌',1.5)
#放家具
house1.addFurniture(bed)
print(house1)
house1.addFurniture(closet)
print(house1)
house1.addFurniture(table)
print(house1)

# 异常类
a = Furnitrue("浴缸",80)
house1.addFurniture(a)
print(house1)

