import give_question

en_list = []
kr_list = []


def en_question():
    input_en_question = input('영어 스펠링을 써주세요. 끝내고 싶으시면 q를 누르세요: ')
    en_list.append(input_en_question)


def kr_question():
    input_kr_question = input('한국어 뜻을 써주세요:')
    kr_list.append(input_kr_question)


def en_kr_question():
    while 1:
        en_question()
        if en_list.__len__() > 0 and en_list[en_list.__len__()-1] == 'q':
            break
        else:
            kr_question()
