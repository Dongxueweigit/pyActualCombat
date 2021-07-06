# Author：DongXuewei
# Time  ：2021/7/6 22:56
# coding：utf-8

class Game:
    my_hp = 1000
    my_power = 200
    enemy_hp = 900
    enemy_power = 199

    def __init__(self, my_hp, enemy_hp):
        self.my_hp = my_hp
        self.enemy_hp = enemy_hp

    def figth(self):
        while True:
            self.my_hp = self.my_hp + self.defense - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power

            print(f"my_hp:{self.my_hp}")
            print(f"enemy_hp:{self.enemy_hp}")
            if self.my_hp <= 0:
                print("我输了！")
                break
            if self.enemy_hp <= 0:
                print("我赢了！")
                break

    def back_kome(self):
        print("回城")

class HouYi(Game):
    def __init__(self, defense,my_hp,enemy_hp):
        self.defense = defense
        super().__init__(my_hp,enemy_hp)

    def figth(self):
        while True:
            self.my_hp = self.my_hp + self.defense - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power

            print(f"my_hp:{self.my_hp}")
            print(f"enemy_hp:{self.enemy_hp}")
            if self.my_hp <= 0:
                print("我输了！")
                break
            if self.enemy_hp <= 0:
                print("我赢了！")
                break


# game = Game(1000, 1100)
# game.figth()

houyi=HouYi(200,1000,1500)
houyi.figth()
houyi.back_kome()