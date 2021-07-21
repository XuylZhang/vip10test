import os


c = os.path.getctime(__file__)
m = os.path.getmtime(__file__)
print(c)
print(m)