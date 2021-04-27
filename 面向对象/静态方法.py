# 静态方法可以减少不必要的内存占用和性能消耗
class Dog():
    @staticmethod
    def print():
        print('我是静态方法，不需要实例对象和类对象')

a = Dog()
a.print()
Dog.print()