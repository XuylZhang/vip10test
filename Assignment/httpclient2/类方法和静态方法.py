# 类方法
class Dog():
    age = 10
    @classmethod
    def get_age(cls):
        return cls.age

a = Dog()
result = a.get_age()
print(result)

# 静态方法
class Dog1():
    @staticmethod
    def get_a():
        print("我是静态方法")
b = Dog1()
b.get_a()
Dog1.get_a()