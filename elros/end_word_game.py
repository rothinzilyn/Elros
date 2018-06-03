true_word = []
false_word = []
total = 0

def score():
    print('true_word :', true_word)
    print('false_word :',false_word)
    total_score = ((true_word.__len__()/2)/total)*100
    print(total_score,'점')


def set_total(num):
    global total
    total = num