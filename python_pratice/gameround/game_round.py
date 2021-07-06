# Author：DongXuewei
# Time  ：2021/7/6 22:40
# coding：utf-8

"""
需求：
一个回合制游戏，每一个角色都有hp和power，hp代表血量，power代表共计力，hp的初始值为1000，power的初始值为200。
两个hp进行对比，血量剩余多的人获胜。
定义一个fight方法：
1. my_hp = hp -enemy_power
2. enemy_final_hp = enemy_hp - my_power
"""


def game():
    my_hp = 1000
    my_power = 200
    enemy_hp = 900
    enemy_power = 199

    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        print(f"my_hp:{my_hp}")
        print(f"enemy_hp:{enemy_hp}")
        if my_hp <= 0:
            print("我输了！")
            break
        if enemy_hp <= 0:
            print("我赢了！")
            break
        # 三目表达式，功能同上if-else语句
        # print("我赢了！") if my_final_hp > enemy_final_hp else print("我输了！")


if __name__ == "__main__":
    game()
