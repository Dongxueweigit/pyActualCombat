## python实战

## 第一个小功能：发礼物

### 路径：

python_pratice/sendGifts

### 需求：

1. 拥有礼物的标识
2. 定义一个发礼物的方法
3. 定义一个战士礼物的方法
4. 启动方法

## 课后作业

### 题目要求：原有存款1000元，发工资后变为2000元

### 定义模块：

1. 定义存款标识模块money.py，存款标识saved_money=1000
2. 定义发工资模块send_money，用来增加收入计算
3. 定义工资查询模块selecte_money，用来展示工资数额
4. 定义一个启动模块start，启动展示最终存款金额

## python实战1-骑电动车

### 父类：Bicycle

写一个自行车类Bicycle，有run（骑行）方法，调用时显示骑行里程km（）骑行里程为传入的数字

### 子类：Ebicycle

写一个电动车类Ebicycle继承Bicycle。添加电池电量battery_level实行通过参数传入，同时有两个方法：

1. fill_charge(vol)用来充电，vol为电量
2. run(km)用于骑行，每骑行10km小号电量1度当电量耗尽时调用Bicycle的run方法骑行

### 显示骑行结果

通过传入的里程数，显示骑行结果，及当电量耗尽，需要真正骑行的里程数

## python实战2-回合制格斗游戏

### 需求：

一个回合制游戏，每一个角色都有hp和power，hp代表血量，power代表共计力，hp的初始值为1000，power的初始值为200。两个hp进行对比，血量剩余多的人获胜。

### 定义一个fight方法：

1. my_hp = hp -enemy_power
2. enemy_final_hp = enemy_hp - my_power 
