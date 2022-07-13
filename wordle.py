import random

class dicti:
    def __init__(self,d):
        self.dictionary=d
        self.dictionary.sort()
        self.secret_word=self.dictionary[random.randrange(len(self.dictionary))]

    def search(self,g):
        start = 0
        end = len(self.dictionary) - 1
        while start <= end:
            mid = (start + end) // 2
            if g == self.dictionary[mid]:
                return True
            elif g > self.dictionary[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return False


with open('words.txt') as f:
    d = f.readlines()
    dictionary=dicti(d)

print(dictionary.secret_word)


class gs:

    def __init__(self,secret,g):
        self.secret=secret
        self.guess_word=g
        self.correct_letter_wrong_place = []
        self.out = [0, 0, 0, 0, 0]
        self.s_elements = list(secret)
        for l in range(len(self.secret)-1):
              if self.guess_word[l] == self.secret[l]:
                    self.out[l] = 2
                    self.s_elements.remove(self.secret[l])
        for l in range(len(self.secret)-1):
             if self.guess_word[l] != self.secret[l]:
                if self.guess_word[l] in self.s_elements:
                    self.out[l] = 1
                    self.correct_letter_wrong_place += [self.guess_word[l]]
                    self.s_elements.remove(self.guess_word[l])
        self.output=''
        for l in self.out:
            self.output+=str(l)


guesses=[]
i=0
while(i<5):
    print('GUESS-'+str(i+1))
    g=input()+'\n'
    guess=gs(dictionary.secret_word,g)
    if dictionary.search(g):
        if g == dictionary.secret_word:
            print("YOU WIN")
            break
        else:
            if i == 0:
                print(guess.output)
                guesses += [guess]

            else:
                er = 0
                new_guess=list(guess.guess_word)
                for k in range(len(dictionary.secret_word)-1):
                    if guesses[i-1].output[k] == 2:
                        if guess.output[k] != 2:
                            er = 1
                            print("Not a valid input")
                            break
                        else:
                            del new_guess[k]

                if er == 1:
                    continue
                for k in guesses[i-1].correct_letter_wrong_place:
                    if k not in new_guess:
                        er=1
                        print("Not a valid input")
                        break
                if er == 1:
                    continue
                else:
                    print(guess.output)
                    guesses += [guess]

        i += 1
    else:
        print("Not a valid attempt!")

if i == 5:
    print("YOU LOSE\n")
    print("The word was-"+dictionary.secret_word)


