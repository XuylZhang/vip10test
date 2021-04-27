# 父类
class Dog():
    def work(self):
        print('指哪打哪。。。')
# 子类1
class ArmyDog(Dog):
    def work(self):
        print('追击敌人。。。')
# 子类2
class DrugDog(Dog):
    def work(self):
        print('找出毒品。。。')
# 使用子类
class Person():
    def work_with_dog(self,dog):
        dog.work()
m = Dog()
a = ArmyDog()
b = DrugDog()
c = Person()
c.work_with_dog(a)
c.work_with_dog(b)
c.work_with_dog(m)