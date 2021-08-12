import random
def youhui(n):
    if n>=1 and n<=10:
        print("恭喜你获得了一张联想的优惠卷")
        return 1
    elif n>=11 and n<=35:
        print("恭喜你获得一张老干妈的优惠卷")
        return 2
    else:
        print("恭喜你获得一张华为的优惠卷")
        return 3

shop = [
    ["lenovo PC",5000],
    ["Mac pc",12000],
    ["HUAWEI  WATCH PRO 20",2000],
    ["机械革命",15000],
    ["老干妈",7.5],
    ["卫龙辣条",3],
    ["西瓜",2]
]
# 1.空的购物车
mycart = []
#  2.初始化您的余额
money = input("请输入您本月工资：")
money = int(money)
# 3.正常购物
i = 1
n = youhui(random.randint(1, 45))
while i <= 20:
    # 展示商品
    for key, value in enumerate(shop):
        print(key, value)
    chose = input("请输入您想要的商品：")
    if chose.isdigit():
        chose = int(chose)
        if chose > len(shop): # len
            print("没有改号商品！请重新输入！")
        else:
            # 钱够不够
            if money >= shop[chose][1]:
                mycart.append(shop[chose])
                j = 0
                if n == 0:
                    money = money - shop[chose][1]
                else:
                    if chose == 0 and n == 1 :
                        y = input("是否使用优惠卷（Y/N）：")
                        if  y == "Y" or y == "y":
                            money = money - 0.5 * shop[chose][1]
                            n = 0;
                        else:
                            money = money - shop[chose][1]
                    elif chose == 4 and n == 2 :
                        y = input("是否使用优惠卷（Y/N）：")
                        if y == "Y" or y == "y":
                            money = money - 0.1 * shop[chose][1]
                            n = 0;
                        else:
                            money = money - shop[chose][1]
                    elif chose == 2 and n == 3:
                        y = input("是否使用优惠卷（Y/N）：")
                        if y == "Y" or y == "y":
                            money = money - 0.6 * shop[chose][1]
                            n = 0;
                        else:
                            money = money - shop[chose][1]
                    else:
                        money = money - shop[chose][1]
                print("恭喜，添加成功！您的余额还剩",money)
            else:
                print("钱不够了，您的剩余金额",money,"买其他商品吧！")
    elif chose == "q" or chose == "Q":
        print("欢迎下次光临！")
        break  # 跳出循环
    else:
        print("对不起，输入错误！")
    i = i + 1

print("以下是您的购物小条，请拿好！")
num = []

print("---------------------------------------")
#统计商品出现的次数
for key,value  in enumerate(mycart):
    if value in mycart[:key]:
        continue
    else:
         num.append(mycart.count(mycart[key]))
mycart2 = []
for i in range(len(mycart)):
    if not mycart[i] in mycart2 :
        mycart2.append(mycart[i]);
print(mycart2)
for key,value  in enumerate(mycart2):
    print(key,"------",value[0],"价格：￥",value[1],"数量：",num[key])
print("---------------------------------------")
print("您的余额还剩：￥",money)




