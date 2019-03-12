from sys import argv

script, input_file = argv


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)  # file.seek(off,whence), len正表示向后移动，负表示向前移动;whence: 0表示从头开始， 1当前位置， 2尾位置；


def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(input_file)
print("frist let's print the whole file:\n")
print_all(current_file)
print("now let's rewind, kind of like a tape.")
rewind(current_file)
print("let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
