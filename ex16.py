from sys import argv

script, filename = argv
print("we are going to erase %r." % filename)
print("if you don't want that, hit CTRL-C(^C).")
print("if you do want that, hit RETURN.")
input("?")
print("opening the file...")
target = open(filename, 'w')
print("truncating the file.  Goodbye!")
# target.truncate()  # 清空文件
print("now i'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
print("i'm going to write these to the file.")
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
print("and finally, we close it.")
target.close()


