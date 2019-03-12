import re

animals = ["bear", "python", "peacock", "kangaroo", "whale", "platypus"]
print("please input a sentence, such as 'the animal at 1' or 'the 1st animal")
sentence = input(">>")
words = sentence.split(" ")
if words.__len__() == 3:
    index = int(re.findall(r"\d+", words[1])[0])  # 提取序数中的基数
    print("the %dst animal is at %d and is a %s" % (index, index - 1, animals[index - 1]))
elif words.__len__() == 4:
    index = int(words[3])
    print("the animal at %d is the %dst animal and is a %s" % (index, index + 1, animals[index]))
