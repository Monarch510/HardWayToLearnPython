# 文字游戏
import random
death = 0


def dead(reason):
    global death
    death += 1
    print(reason, "游戏失败！")
    print("输入1重新开始游戏！")
    restart = input(">>")
    if restart == "1":
        start()
    else:
        exit(0)


def choose_door():
    print("是时候该动起来了，周围有四扇门，你选择：")
    print("1. 东门\t2. 南门\n3. 西门\t4. 北门")


def start():
    print("你现在起点")
    print("你好奇地打量四周，看到中央有一块竖着的木牌，上面写道：")
    print("五行八卦奇门遁甲，开休生伤杜景惊死")
    choose_door()
    door = input(">>")
    if door == "1":
        shengDoor()
    elif door == "2":
        duDoor()
    elif door == "3":
        jinDoor()
    elif door == "4":
        kaiDoor()
    else:
        start()


def kaiDoor():  # 开门
    print("你现在在开门")
    print("你好奇地打量四周，看到中央有一块竖着的木牌，上面写道：")
    print("一言九鼎\n天上宫阙\n\t格物致知\n\t开门大吉")
    choose_door()
    door = input(">>")
    if door == "1":
        siDoor()
    elif door == "2":
        start()
    elif door == "3":
        shangmen()
    elif door == "4":
        print("无法打开")
        kaiDoor()
    else:
        kaiDoor()


def xiuDoor():  # 休门
    print("你现在在休门")
    game1()
    choose_door()
    door = input(">>")
    if door == "2" or door == "3":
        print("无法打开")
        xiuDoor()
    elif door == "1":
        duDoor()
    elif door == "4":
        jinDoor()
    else:
        xiuDoor()


def shengDoor():  # 生门
    print("你现在在生门")
    choose_door()
    print("走到真正的出口将无法回头，请谨慎选择！！！")
    door = input(">>")
    if door == "1":
        print("这里是真正的出口，然而这个门是数字密码门\n北京第三交通委提醒您：密码千万条，机会只一次，五号排第一，不要输入错")
        print("请输入密码：")
        password = input(">>")
        if password == "596123784":
            print("恭喜你，逃出密室！！！")
            print("游戏期间你一共死亡%d次" % death)
            exit(0)
        else:
            dead("密码错误！")
    elif door == "2":
        jingDoor()
    elif door == "3":
        start()
    elif door == "4":
        siDoor()
    else:
        shengDoor()


def shangmen():  # 伤门
    print("你现在在伤门")
    print("你好奇地打量四周，然而什么都没有")
    choose_door()
    door = input(">>")
    if door == "3" or door == "4":
        print("无法打开")
        shangmen()
    elif door == "1":
        kaiDoor()
    elif door == "2":
        jinDoor()
    else:
        shangmen()


def duDoor():  # 杜门
    print("你现在在杜门")
    print("你好奇地打量四周，看到中央有一块竖着的木牌，上面写道：")
    print("无中生有新章创，从始至终正道行")
    choose_door()
    door = input(">>")
    if door == "1":
        jingDoor()
    elif door == "2":
        print("无法打开")
        duDoor()
    elif door == "3":
        xiuDoor()
    elif door == "4":
        start()
    else:
        duDoor()


def jinDoor():  # 景门
    print("你现在在景门")
    game2()
    choose_door()
    door = input(">>")
    if door == "1":
        start()
    elif door == "2":
        xiuDoor()
    elif door == "3":
        print("无法打开")
        jinDoor()
    elif door == "4":
        shangmen()
    else:
        jinDoor()


def jingDoor():  # 惊门
    print("你现在在惊门")
    print("你发现墙壁上有人刻着‘0 + 0 = ？’")
    choose_door()
    door = input(">>")
    if door == "1" or door == "2":
        print("无法打开")
        jingDoor()
    elif door == "3":
        duDoor()
    elif door == "4":
        shengDoor()
    else:
        jingDoor()


def siDoor():  # 死门
    print("你现在在死门")
    print("耳边突然想起绕口令：")
    print("四是四，十是十，四十是四十，十四是十四")
    print("你心里一片慌张，心里想着赶快离开，你选择？")
    print("1. 赶快离开 2. 我不信邪，继续留下")
    choose = input(">>")
    if choose == "1":
        choose_door()
        door = input(">>")
        if door == "1" or door == "4":
            print("无法打开")
            dead("想离开却打不开门，就这样悲哀地死去了！")
        elif door == "2":
            shengDoor()
        elif door == "3":
            kaiDoor()
    else:
        dead("叫你不信邪，现在死了吧！")


def match(ran, variable):
    if ran % variable == 0 or ran // 10 == variable or ran % 10 == variable:
        return 1
    else:
        return 0


def game1():
    children = 6
    print("你遇到%d个小孩，他们想和你玩个报数游戏" % children)
    print("小孩报一个数，如果它是%d的倍数或者带有数字%d，你就输入1，其余输入0" % (children, children))
    print("你选择：1. 玩 2. 不玩")
    choose = input(">>")
    if choose == "1":
        i = 0
        correct = 0
        while i < children:
            i += 1
            ran = random.randint(1, 100)
            print(i, "号小孩说", ran)
            respon = int(input(">>"))
            if respon == match(ran, children):
                print("回答正确！")
                correct += 1
            else:
                print("回答错误！")

        if correct == children:
            print("小孩们告诉你有关离开密室的一条线索\n出口的密码就藏在每一个房间中")


def game2():
    print("你遇到凶恶的被镣铐锁住的老虎，老虎们对你虎视眈眈")
    print("这时，你发现只要向前走七步之后，老虎们就够不着你了，你会选择？")
    print("1. 缓慢地走过 2. 飞快地跑过 3. 掉头往回走")
    choose = input()
    if choose == "1":
        dead("你走的太慢了，被老虎一口吃掉！")
    elif choose == "2":
        dead("你在慌乱中摔倒了，被老虎一口吃掉！")
    elif choose == "3":
        print("恭喜你活下来了，有时后退才是成功的关键！你仍在原来的房间")
    else:
        dead("自取灭亡，被老虎一口吃掉！")


print("欢迎进入游戏\n这是一个密室逃生游戏，你需要找到真正的出口，然后输入密码打开它，逃出去！")
start()
