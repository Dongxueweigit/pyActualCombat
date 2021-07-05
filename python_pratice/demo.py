# Author：DongXuewei
# Time  ：2021/7/5 19:25

a=1
def func():
    global a
    a=2
    print(f"{a}")

func()
print(a)