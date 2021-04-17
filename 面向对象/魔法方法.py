# 初始化对象
class Washer():
    def __init__(self,width,height,name):
        self.width = width
        self.height = height
        self.name = name
    def print_info(self):
        print(f'{self.name}的宽度是{self.width}')
        print(f'{self.name}的高度是{self.height}')
    def __str__(self):
        return f'这是{self.name}洗衣机的说明书'
    def __del__(self):
        print(f"{self.name}被删除了")

haier1 = Washer(300,500,"haier1")
haier2 = Washer(100,400,"haier2")

print(haier2)

haier2.print_info()
# del haier1
del haier2
print(haier1)
haier1.print_info()