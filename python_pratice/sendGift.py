# Author：DongXuewei
# Time  ：2021/7/5 22:31
# coding：utf-8
"""
1.拥有礼物的标识
2.定义一个发礼物的方法
3.定义一个战士礼物的方法
4.启动方法
"""
#拥有礼物的标识
have_gift = False

#发礼物方法
def send():
    print("发礼物啦")
    global have_gift
    #have_gift = True
    have_gift = True

#收礼物方法
def show():
    global have_gift
    if have_gift == True:
        print("收到礼物啦，好开心~")
    else:
        print("没有礼物")

print(f"name变量的值为{__name__}")
print(locals())
if __name__ == "__main__":
    send()
    show()





