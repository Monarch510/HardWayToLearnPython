ten_things = "apples Oranges Crows Telephone Light Sugar"
print("wait there's not 10 things in that list, let's fix that")
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("adding: ", next_one)
    stuff.append(next_one)
    print("there's %d items now." % len(stuff))
print("there we go: ", stuff)
print("let's do some things with stuff.")
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))  # 在stuff的各元素之间加入空格
print('#'.join(stuff[3:5]))  # 在stuff的第四个和第五个元素之间加入#
