# 师傅
class Master(object):
    def __init__(self):
        self.kongfu = '五香煎饼果子配方'

    def make(self):
        print(f"运用Master{self.kongfu}制作煎饼果子")


# 学校类
class School(Master):
    def __init__(self):
        self.kongfu = '香辣煎饼果子配方'

    def make(self):
        print(f'运用School{self.kongfu}制作煎饼果子')
    def make_master(self):
        super().__init__()
        super().make()


class Prentice1(School):
    def __init__(self):
        self.kongfu = '独创煎饼果子配方'

    def make(self):
        print(f'运用Prentice{self.kongfu}制作煎饼果子')

    def make_old(self):
        super().__init__()
        super().make()
        super().make_master()

xiaoming = Prentice1()
xiaoming.make()
xiaoming.make_old()
