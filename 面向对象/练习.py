# 定义一个老师类，老师有姓名、性别和教的课程，可以教学，实现：××老师，性别是××，教××课
class Teacher():
    # 属性：姓名、性别、课程
    def __init__(self,name,gender,course):
        self.name = name
        self.gender = gender
        self.course = course
    # 方法：教学
    def teaching(self):
        print(f"{self.name}老师，性别是{self.gender}，教{self.course}课")

techer1 = Teacher("徐艳良","男","代码基础")
techer1.teaching()

