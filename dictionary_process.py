

class vocabulary:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
        self.trial = 0
        self.accepted = 0

    def print(self):
        print(self.word, " : ", self.meaning)
        print("You tried", self.trial, "times and accepted", self.accepted, "times.")

    def test(self):
        self.trial +=1
        meaning = input(self.word+": ")
        if meaning == self.meaning:
            self.accepted +=1
            return
        check_step = input("Does it same with "+ self.meaning +"? [press enter if right]")

        if check_step == '':
            self.accepted +=1
            self.print()
            print("\n")
            return
        
        self.print()
        print("\n")


    def study(self):
        self.print()
        temp=input()

class statics:
    def __init__(self):
        self.total_trial = 0
        self.total_accept = 0
        self.max_trial = 0
        self.max_accept_rate = 0
        self.min_accept_rate = 100
        self.word_need_to_memorize =[]

    def update(self, vocabulary_list):
        for vocab in vocabulary_list:
            self.total_trial += vocab.trial
            self.total_accept += vocab.accepted
            self.max_trial = max(self.max_trial,vocab.trial)
            if vocab.trial == 0:
                continue
            self.max_accept_rate = max(self.max_accept_rate, 100.0*vocab.accepted/vocab.trial)
            if self.min_accept_rate>100.0*vocab.accepted/vocab.trial:
                self.word_need_to_memorize = [vocab]
            elif  self.min_accept_rate==100.0*vocab.accepted/vocab.trial:
                self.word_need_to_memorize.append(vocab)

            self.min_accept_rate = min(self.min_accept_rate, 100.0*vocab.accepted/vocab.trial)

    def print(self):
        print("you have tried", self.total_trial, "times, accepted", self.total_accept)
        print("The worst accepted words")
        for vocab in self.word_need_to_memorize:
            vocab.print()

def find(
    vocabulary_list, word
):
    for vocab in vocabulary_list:
        if vocab.word ==word:
            return vocab
    
    return 'none'