def test(length, add):
    i = 0
    numbers = []
    while i < length:
        print("at the top i is %d" % i)
        numbers.append(i)
        i += add
        print("numbers now:", numbers)
        print("at the bottom i is %d" % i)
    print("the numbers: ")
    for num in numbers:
        print(num)


print("please input a number:")
length = int(input(">>"))
add = 2
test(length, add)
