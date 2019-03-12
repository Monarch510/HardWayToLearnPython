the_count = [1, 2, 3, 4, 5]
fruits = ["appless", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]
for number in the_count:
    print("this is count %d" % number)
for fruit in fruits:
    print("a fruit of type: %s" % fruit)
for i in change:
    print("i got %s" % i)
elements = []
for i in range(0, 6):  # range(start, end, step)三个参数，step步长
    print("adding %d to the list" % i)
    elements.append(i)
for i in elements:
    print("elements was: %d" % i)