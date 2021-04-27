# 类方法一般用来访问类属性
class Dog():
    # 私有类属性
    __tooth = 10

    # 类方法
    @classmethod
    def get_tooth(cls):
        return cls.__tooth

# 访问类方法
xiaohei = Dog()
result = xiaohei.get_tooth()
print(result)