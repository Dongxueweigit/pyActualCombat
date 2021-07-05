# Author：DongXuewei
# Time  ：2021/7/5 22:46
# coding：utf-8

#form import相当于复制了一份内容到本地地址，不能够通过调用者改变原有的值，import引用的是模块的地址，可以通过调用者修改原有内容
#from giftFlag import *
import giftFlag
#发礼物方法
def send():
    print("发礼物啦")
    #global have_gift
    #have_gift = True
    giftFlag.have_gift = True