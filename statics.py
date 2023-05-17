import dictionary_process as dct
import pickle

try:
    with open('vocabulary_list.pickle', 'rb') as f:
        vocabulary_list = pickle.load(f)
except FileNotFoundError:
    print("There are no files")


statics = dct.statics()

statics.update(vocabulary_list)
statics.print()
