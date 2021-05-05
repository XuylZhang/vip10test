class Dog():
    age = 10

a = Dog()
b = Dog()
print(Dog.age)
print(a.age)
print(b.age)

# 修改类属性
Dog.age = 12
print(Dog.age)
print(a.age)
print(b.age)


# 修改对象的类属性
a.age = 14
print(Dog.age)
print(a.age)
print(b.age)