import random

someWords = '''apple banana mango strawberry
orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split()
word = random.choice(someWords)

class Hangman:
    giriş = "---------adam asmaca oynuma hosgeldiniz---------"
    print(giriş)


    def __init__(self,word):
        self.word = word


    def fonk(self):
        print(f"seçilen kelime {len(self.word)} harfli meyve ")
        print(f"{len(self.word)+2} hakkın var")

    def loops(self):
        for i in self.word:
            print("_", end="") #kelime sayısı kadar çizgiler

        print()
        a = len(self.word) + 2
        b = 0
        letterGuessed = ''

        while  b<a:
            c = str(input(" kelime tahmin et:\n"))
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
                print(" you win")
                break

            b+=1

        else:
            print(f"you lost {self.word}")


a = Hangman(word)
a.fonk()
a.loops()
