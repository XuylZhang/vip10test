# 房屋类
class House():
    #属性：占地面积、家具列表、剩余面积
    def __init__(self,floorArea,furnitureList):
        self.floorArea = floorArea
        self.furnitureList = furnitureList
        self.residueArea = floorArea
    #方法：放家具
    def addFurniture(self,item):
        if self.residueArea >= item.floorArea:
            self.furnitureList.append(item.name)
            self.residueArea -= item.floorArea
        else:
            print(f"房屋面积不足以放下{item.name}")
    #显示房屋信息
    def __str__(self):
        return f"房屋总面积{self.floorArea}，房子中的家具{self.furnitureList}，房屋剩余面积{self.residueArea}"

# 家具类
class Furniture():
    #属性：名称、占地面积
    def __init__(self,name,floorArea):
        self.name = name
        self.floorArea = floorArea

#创建家具对象
fur1 = Furniture("床",4)
#创建房屋对象
house1 = House(80,[])
#房子里放家具
house1.addFurniture(fur1)
#输出房屋信息
print(house1)

#创建家具对象2
fur2 = Furniture("体育场",75)
#房子里放家具2
house1.addFurniture(fur2)
#输出房屋信息
print(house1)