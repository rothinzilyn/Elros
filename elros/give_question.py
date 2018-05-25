import random
import word_question


def give():
    index = random.randint
    while word_question.en_list.__len__:
        print("index : ", index, " - ", word_question.en_list[index])
        index = index + 1
        return