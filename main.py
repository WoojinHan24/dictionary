import dictionary_process as dct
import pickle
import fileinput
import random


flag = 0
del1 = "한"
del2 = ":"
del3 = "-"
update_string ="______________\n"

while(True):
    try:
        with open('vocabulary_list.pickle', 'rb') as f:
            vocabulary_list = pickle.load(f)
    except FileNotFoundError:
        print("There are no files.")
        vocabulary_list =[]
        flag=1
        check_step = 'y'

    if flag == 0:
        check_step=input("Will you change the vocabulary list? [y/n]")


    if check_step == 'n' or check_step =='N' or check_step =='':
        break


    if check_step == 'y' or check_step =='Y':
        print("Paste down your list back in vocabulary_list.txt")
        temp = input("[press any key to continue]")
        read_start = False

        with fileinput.input(files=("vocabulary_list.txt"), encoding = "utf-8") as f:
            for line in f:
                if line == update_string:
                    read_start = True
                    continue

                if read_start == False:
                    continue
                
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

                if dct.find(vocabulary_list,word)=='none':
                    vocabulary_list.append(dct.vocabulary(word,meaning))
                else:
                    print("overlapped.")
                    dct.fine(vocabulary_list,word).print()
        

        with open("./vocabulary_list.txt", "r") as f:
            lines = f.readlines()
        with open("./vocabulary_list.txt", "w") as f:
            for line in lines:
                if line != update_string:
                    f.write(line)
            f.write(update_string)

        with open('vocabulary_list.pickle', 'wb') as f:
            pickle.dump(vocabulary_list, f, pickle.HIGHEST_PROTOCOL)
        break


# for vocab in vocabulary_list:
#     vocab.print()

# raise KeyError



try:
    num_question = int(input("How many vocabulary want to test?: "))
    num_question = min((num_question, len(vocabulary_list)))
except ValueError:
    num_question = len(vocabulary_list)


question_list = random.sample(range(len(vocabulary_list)), num_question)
print(num_question,"vocabulary ready.")
check_step = input("Will you check the question list? [press enter to check]")


if check_step == '':
    for idx in question_list:
        vocabulary_list[idx].study()

for idx in question_list:
    vocabulary_list[idx].test()

with open('word_list.pickle', 'wb') as f:
    pickle.dump(vocabulary_list, f, pickle.HIGHEST_PROTOCOL)

