import random

someWords = '''apple banana mango strawberry
orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split()
word = random.choice(someWords)

class Hangman:
    start = "---------welcome to my hangman game---------"
    print(start)


    def __init__(self,word):
        self.word = word


    def random_choice_word(self):
        print(f"Selected word is a fruit with {len(self.word)} letters.")
        print(f"you have {len(self.word)+2} chances to find it")

    def loops(self):
        for i in self.word:
            print("_", end="") 

        print()
        a = len(self.word) + 2
        b = 0
        letterGuessed = ''

        while  b<a:
            c = str(input("Guess the word.:\n"))
            if c == self.word:
                print("you win")
                break

            if c in self.word:
                k = self.word.count(c)
                for _ in range(k):
                    letterGuessed += c

            for char in self.word:
                if char in letterGuessed:
                    print(char,end="")
                else:
                    print("_",end="")

            if c == self.word:
                print("YOU WİN")
                break
            b+=1

        else:
            print(f"you lost {self.word}")


a = Hangman(word)
a.fonk()
a.loops()
