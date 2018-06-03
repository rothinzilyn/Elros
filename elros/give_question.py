import random
import word_question
import end_word_game


def give():
    while word_question.en_list.__len__():
        kr_or_en = random.randrange(1,3)
        if kr_or_en == 1:
            index = random.randint(0, word_question.en_list.__len__()-1)
            en_quest = word_question.en_list.pop(index)
            kr_quest = word_question.kr_list.pop(index)
            print('question:',en_quest)
            answer = input()
            if answer == kr_quest:
                print('good job!')
                index = 0
                kr_or_en = 0
                end_word_game.true_word.append(en_quest)
                end_word_game.true_word.append(kr_quest)
            else:
                print('bad....')
                index = 0
                kr_or_en = 0
                end_word_game.false_word.append(en_quest)
                end_word_game.false_word.append(kr_quest)
        if kr_or_en == 2:
            index = random.randint(0,word_question.kr_list.__len__()-1)
            en_quest = word_question.en_list.pop(index)
            kr_quest = word_question.kr_list.pop(index)
            print('question:',kr_quest)
            answer = input()
            if answer == en_quest:
                print('good job!')
                index = 0
                kr_or_en = 0
                end_word_game.true_word.append(en_quest)
                end_word_game.true_word.append(kr_quest)
            else:
                print('bad....')
                index = 0
                kr_or_en = 0
                end_word_game.true_word.append(en_quest)
                end_word_game.true_word.append(kr_quest)
    return
