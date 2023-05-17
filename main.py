import dictionary_process as dct
import pickle
import fileinput
import random



flag = 0
del1 = "한"
del2 = ":"
del3 = "-"

while(True):
    if flag == 0:
        check_step=input("Will you change the vocabulary list? [y/n]")

    if check_step == 'y' or 'Y':
        vocabulary_list = []
        print("Paste down your list in vocabulary_list.txt")
        temp = input("[press any key to continue]")

        with fileinput.input(files=("vocabulary_list.txt"), encoding = "utf-8") as f:
            for line in f:
                if line == '\n':
                    continue
                if line[0] == del1:
                    continue
                if line[0] == del2:
                    continue
                word, meaning=line.split(del3)
                if word[-1] == ' ':
                    word = word[:-1]
                if meaning[0] == ' ':
                    meaning = meaning[1:]
                meaning = meaning[:-1]

                vocabulary_list.append(dct.vocabulary(word,meaning))
                

        with open('word_list.pickle', 'wb') as f:
            pickle.dump(vocabulary_list, f, pickle.HIGHEST_PROTOCOL)
        break

    if check_step == 'n' or 'N':
        try:
            with open('vocabulary_list.pickle', 'rb') as f:
                vocabulary_list = pickle.load(f)
        except FileNotFoundError:
            print("There are no files.")
            flag=1
            continue
        break

num_question = int(input("How many vocabulary want to test?: "))
try:
    num_question = min((num_question, len(vocabulary_list)))
except ValueError:
    num_question = len(vocabulary_list)

question_list = random.sample(vocabulary_list, num_question)

check_step = input("Will you check the question list? [press enter to check]")
if check_step == '':
    for vocab in question_list:
        vocab.study()

for vocab in question_list:
    vocab.test()

with open('word_list.pickle', 'wb') as f:
    pickle.dump(vocabulary_list, f, pickle.HIGHEST_PROTOCOL)

