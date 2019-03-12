from sys import exit


def gold_room():  # 黄金屋
    print("this room is full of gold. how much do you take?")
    next = input(">>")
    if next.isdigit():
        num = int(next)
    else:
        dead("man, learn to type a number")
    if num < 50:
        print("nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("you greedy bastard！")


def bear_room():  # 熊屋
    print("there is a bear here")
    print("the bear has a bunch of honey")
    print("the fat bear is in front of another door")
    print("how are you going to move the bear?")
    print("1. take money\n2. taunt bear\n3. open door")
    bear_moved = False
    while True:
        next = input(">>")
        if next == "1":
            dead("the bear looks at you then slaps your face off")
        elif next == "2" and not bear_moved:
            print("the bear has moved from the door. you can go through it now")
            bear_moved = True
        elif next == "2" and bear_moved:
            dead("the bear gets pissed off and chews your leg off")
        elif next == "3" and bear_moved:
            gold_room()
        else:
            print("i got no idea what that means")


def evil_room():  # 恶魔屋
    print("here you see the great evil")
    print("he, it, whatever stares at you and you go insane")
    print("do you flee for your life or eat your head?")
    print("1. flee life\n2. eat head")
    next = input(">>")
    if next == "1":
        start()
    elif next == "2":
        dead("well that was tasty!")
    else:
        evil_room()


def dead(why):  # 死亡原因
    print(why, "good job!")
    exit(0)


def start():
    print("you are in a dark room")
    print("there is a door to your right and left")
    print("which one do you take?")
    next = input(">>")
    if next == "left":
        bear_room()
    elif next == "right":
        evil_room()
    else:
        dead("you stumble around the room until you starve")


start()
