

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
            return
        
        self.print()

    def study(self):
        self.print()
        temp=input()