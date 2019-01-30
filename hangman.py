import os
from random import randint

WORDS_PATH = "words"
ENG_ALPHABETS = [chr(65+i) for i in range(25)] + [chr(97+i) for i in range(25)]

def getCategory():
    categories = []
    for filename in os.listdir(WORDS_PATH):
        categories += [{
            "title": ".".join(filename.split(".")[:-1]),
            "file": filename
        }]

    return categories

def showMenu(categories):
    index = 1

    print("Select Category:")
    for category in categories:
        print("{:d}: {:s}".format(index, category["title"]))
        index += 1
    print()

    while True:
        select = input("> ")

        if not select.isdigit():
            print("Please input only number.")
        else:
            select = int(select)
            if select > len(categories) or select < 1:
                print("Please input number in range 1 - {:d}".format(len(categories)))
                continue
            break

    return categories[select-1]

def randomWord(file):
    filepath = os.path.join(WORDS_PATH, file)
    totalWords = sum(1 for line in open(filepath))

    if totalWords <= 0:
        print("File '{:s}' is empty.".format(file))
        exit()

    randIndex = randint(0, totalWords-1)

    if randIndex % 2 != 0:
        randIndex -= 1
    
    result = {}

    lineIndex = 0
    for line in open(filepath):
        if lineIndex == randIndex:
            result["word"] = line
        if lineIndex == randIndex+1:
            result["hint"] = line
            break
        lineIndex += 1

    return result

class GuessWord:
    def __init__(self, word, hint):
        self.word = word.strip()
        self.score = 0
        self.remaining = 10
        self.rightScore = 1
        self.wrongGuess = ""
        self.rightGuess = ""
        self.fullScore = self._fullScore()
        self.hint = hint.strip()
    
    def _fullScore(self):
        onlyAlpha = list(filter(lambda x: x.isalpha(), self.word))
        return len(onlyAlpha) * self.rightScore

    def show(self):
        for charecter in self.word:
            if charecter.lower() in self.rightGuess.lower():
                print(charecter, end=" ")
            elif charecter.isalpha():
                print("_", end=" ")
            else:
                print(charecter, end=" ")
        
        strWrong = ", ".join(self.wrongGuess)

        print("  score: {:d}, remaining wrong guess {:d}, wrong guessed: {:s}".format(
            self.score, self.remaining, strWrong
        ))
    
    def _guess(self):
        while True:
            charecter = input("> ")
            if len(charecter) > 1:
                print("You can input only 1 charecter at the time")
                continue
            elif not charecter.isalpha() or charecter not in ENG_ALPHABETS:
                print("Please input charecter between a - z")
                continue
            elif charecter.lower() in self.rightGuess.lower() + self.wrongGuess.lower():
                print("You have already guess this character. try another character.")
                continue
            break
        
        return charecter
    
    def _calculate(self, charecter):
        wordLower = self.word.lower()
        charecterLower = charecter.lower()

        if charecterLower in wordLower:
            self.rightGuess += charecter
            self.score += self.rightScore * wordLower.count(charecterLower)
            return 1
        else:
            self.wrongGuess += charecter
            self.remaining -= 1
            return -1

    def play(self):
        print("Hint: \"{:s}\"".format(self.hint.replace("##", "")))
        while True:
            self.show()
            if self.remaining != 0 and self.score != self.fullScore:
                self._calculate(self._guess())
            elif self.score == self.fullScore:
                msg = "You win!!! | The answer is '{:s}'".format(self.word)
                print()
                print("="*(len(msg)+4))
                print("* {:s} *".format(msg))
                print("="*(len(msg)+4))
                break
            else:
                print()
                print("====================")
                print("| End! You lost... |")
                print("====================")
                break

if __name__ == "__main__":
    categories = getCategory()
    select = showMenu(categories)
    randWord = randomWord(select["file"])

    guessWord = GuessWord(**randWord)
    guessWord.play()