# 创建类
class Washer():
    def wash(self):
        print("我会洗衣服")
        print(self)


# 创建（实例化）对象
haier1 = Washer()
print(haier1)
haier1.wash()

# 类的外面添加和获取属性
haier1.width = 500
haier1.height = 800
print(f'haier1的宽度是{haier1.width}')
print(f'haier1的高度是{haier1.height}')

# 类的里面获取属性
class Washer1():
    def print_info(self):
        print(f'{self.name}的宽度是{self.width}')
        print(f'{self.name}的高度是{self.height}')

haier2 = Washer1()
haier2.width = 500
haier2.height = 800
haier2.name = 'haier2'

haier3 = Washer1()

haier2.print_info()
# haier3.print_info()