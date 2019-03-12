def break_words(stuff):  # 将句子按空格分开
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words


def sort_words(words):  # 将句子中的字符按照ASCII中的顺序从小到大排序
    """Sorts the words."""
    return sorted(words)


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print("first:", word)


def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print("last:", word)


def sort_sentence(sentence):  # 将句子中的词语按照词语中第一个字符在ASCII中的顺序从小到大排列
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


# my_words = "My name is wwj， 520！"
# print(break_words(my_words))
# print(sort_words(my_words))
# print(sort_sentence(my_words))
# print_first_and_last(my_words)
# print_first_and_last_sorted(my_words)

print(False and None)  # False
print(False or None)  # None
print(True and None)  # None
print(True or None)  # True
