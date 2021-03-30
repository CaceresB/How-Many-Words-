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
from time import sleep

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)



#import PyDictionary

#Dictionary setup


#Enchant Setup
d = enchant.Dict("en_US")


#Finds all letter combinations
def words(letters):
  wList = []
  gList = []
  numWords = 0
  for n in range(3, len(letters) + 1):
    twList = []
    tgList = []
    for i in set(permutations(letters, n)):
      temp = ''.join(i)
      if d.check(temp) and temp not in wList and not profanity.contains_profanity(temp):
        twList += [temp]
        tgList += ["_"*n]
        numWords+=1
    wList+=[twList]
    gList+=[tgList]
  if len(wList[-1])>0:
    if wList[-1][-1]==letters: 
      wList[-1].pop()
      gList[-1].pop()
      numWords-=1
  return wList,gList, numWords


with open('words_alpha.txt') as f:
	my_list = [x.rstrip() for x in f if len(x) > 5 and len(x)<10]

#dictionary.meaning(word)


NewGame=True

while NewGame:
  word = my_list[randint(1, len(my_list))]
  while d.check(word)!= True and profanity.contains_profanity(word)!=True:
    word = my_list[randint(1, len(my_list))]
  #dictionary.meaning(word)
  print(word)
  answers, guesses, tWords = words(word)
  wGuessed = 0
  tGuessed = [0]*len(answers)
  Continue=True
  while Continue and wGuessed!=tWords:
    print("\033[H\033[J",end="")
    print(word)
    for i in range(len(max(answers,key=len))):
      pGuess = ""
      for j in guesses:
        if i<len(j):
          pGuess+=j[i]+"\t\t"
      print(pGuess)

    #print(guesses)
    print("\nYou have guessed {0} out of {2} words! \n{1:.2f}% there ".format(wGuessed, wGuessed*100 / tWords, tWords)) 
    print("Enter 0 to quit")

    guess = input("Enter a word you can make from this word (min length 3):\n")
    if guess in guesses[len(guess)-3]:
      print("You tried this already!")
    elif guess in answers[len(guess)-3]:
      guesses[len(guess)-3][tGuessed[len(guess)-3]] = guess
      wGuessed += 1
      tGuessed[len(guess)-3]+=1

      print("Good job!")
    else:
      if guess=="0":
        for i in range(len(max(answers,key=len))):
          pAnswers = ""
          for j in range(len(answers)):
            if i<len(answers[j]):
              if answers[j][i] not in guesses[j]:
                pAnswers+=answers[j][i]+"\t\t"
              else:
                pAnswers+="\t\t"
          print(pAnswers)
        Continue= False
        

      else:
        print("Not quite!")
    
    sleep(.25)

  
  if wGuessed==tWords:
    print("Congrats you guesed them all!")
    sleep(.5)
  
  NG = input("Try a new word?").capitalize()
  if NG== "N" or NG== "NO":
    NewGame=False
  clearConsole()