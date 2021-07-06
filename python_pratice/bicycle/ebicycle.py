# Author：DongXuewei
# Time  ：2021/7/6 19:40
# coding：utf-8

"""
父类：Bicycle
写一个自行车类Bicycle，有run（骑行）方法，调用时显示骑行里程km（）骑行里程为传入的数字
子类：Ebicycle
写一个电动车类Ebicycle继承Bicycle。添加电池电量battery_level实行通过参数传入，同时有两个方法：
1. fill_charge(vol)用来充电，vol为电量
2. run(km)用于骑行，每骑行10km小号电量1度当电量耗尽时调用Bicycle的run方法骑行
显示骑行结果：通过传入的里程数，显示骑行结果，及当电量耗尽，需要真正骑行的里程数
"""


class Bicycle():
    def run(self, km):
        print(f"健康环保，骑行里程数为：{km} km")


class Ebicycle(Bicycle):
    def __init__(self, battery_level):
        # 初始化电池电量
        self.battery_level = battery_level

    def fill_charge(self, vol):
        # 充电后电池电量
        self.battery_level = self.battery_level + vol

    def run(self, km):
        # 电量耗完后需要用脚骑行里程数
        miles = km - self.battery_level * 10
        if miles > 0:
            print(f"已用电行驶：{self.battery_level * 10} km\n剩余电量：0")
            super().run(miles)
        else:
            print(f"已用电行驶：{km} km\n剩余电量：{self.battery_level - km / 10}")

#入口函数
if __name__ == '__main__':
    eb = Ebicycle(10)
    eb.fill_charge(1)
    eb.run(120)
