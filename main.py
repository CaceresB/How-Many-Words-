#Game to guess all of the words in another word

#See what percentage you get
#import os
#os.system("pip install pyenchant")
#os.system("pip install PyDictionary")
import enchant
from random import randint
from itertools import permutations
from better_profanity import profanity
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)



#import PyDictionary

#Dictionary setup
#dictionary=PyDictionary

#Enchant Setup
d = enchant.Dict("en_US")


#Finds all letter combinations
def words(letters):
  wList = []
  for n in range(3, len(letters) + 1):
    for i in set(permutations(letters, n)):
      temp = ''.join(i)
      if d.check(temp) and temp not in wList and not profanity.contains_profanity(temp):
        wList += [temp]
  if wList[-1]==letters: wList.pop()
  return wList


with open('words_alpha.txt') as f:
	my_list = [x.rstrip() for x in f if len(x) > 5 and len(x)<11]

#dictionary.meaning(word)


NewGame=True

while NewGame:
  word = my_list[randint(1, len(my_list))]
  #dictionary.meaning(word)
  print(word)
  answers = words(word)
  tWords = len(answers)
  wGuessed = 0
  guesses = []
  Continue=True
  while Continue:
    print("\033[H",end="")
    print(word)
    print("You have guessed {0} out of {2} words! \n{1}% there ".format(wGuessed, wGuessed*100 / tWords, tWords)) 
    print("Enter 0 to quit")

    guess = input("Enter a word you can make from this word (min length 3): ")
    if guess in guesses:
      print("You tried this already!")
    elif guess in answers:
      guesses += [guess]
      wGuessed += 1
    else:
      if guess=="0":
        print(answers)
        Continue= False
        NG = input("Try a new word?").capitalize()
        if NG== "N" or NG== "NO":
          NewGame=False

      else:
        print("Not quite!")
      print("      ","")
  clearConsole()
