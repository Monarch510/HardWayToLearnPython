def add(a, b):
    print("adding %d + %d" % (a, b))
    return a + b


def substract(a, b):
    print("substracting %d - %d" % (a, b))
    return a - b


def multiply(a, b):
    print("multiplying %d * %d" % (a, b))
    return a * b


def divide(a, b):
    print("dividing %d / %d" % (a, b))
    return a / b


print("let's do some math with just functions!")
age = add(20, 1)
height = substract(178, 10)
weight = multiply(35, 2)
iq = divide(160, 2)
print("age: %d, height: %d, weight: %d, iq: %d" % (age, height, weight, iq))
print("here is a puzzle")
what = add(age, substract(height, multiply(weight, divide(iq, 2))))
print("that becomes: ", int(what), "can you do it by hand?")
