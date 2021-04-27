class Dog():
    tooth = 10

xiaohei = Dog()
wangcai = Dog()

print(Dog.tooth)
print(xiaohei.tooth)
print(wangcai.tooth)

Dog.tooth = 12
print(Dog.tooth)
print(xiaohei.tooth)
print(wangcai.tooth)

xiaohei.tooth = 20
print(Dog.tooth)
print(xiaohei.tooth)
print(wangcai.tooth)
print("xiaohei")

xiaohei = Dog()
print(Dog.tooth)
print(xiaohei.tooth)
print(wangcai.tooth)