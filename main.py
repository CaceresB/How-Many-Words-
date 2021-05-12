#Game to guess all of the words in another word

#See what percentage you get
import os
#os.system("pip install pyenchant")
#os.system("pip install PyDictionary")
import enchant
from random import randint
from itertools import permutations
from better_profanity import profanity
#import os
from time import sleep
from math import ceil
from tabulate import tabulate

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)



#import PyDictionary
#from PyDictionary import PyDictionary
#dictionary=PyDictionary()


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
    if twList != []:
      wList+=[twList]
      gList+=[tgList]
  if len(wList[-1])>0:
    if letters in wList[-1]: 
      wList[-1].remove(letters)
      gList[-1].pop()
      numWords-=1
      if [] in wList:
        wList.remove([])
        gList.remove([])
  return wList,gList, numWords

def mTable(oList):
  mLetters = len(max(oList,key=len))
  if mLetters<20:
    nTable=[[] for i in range(mLetters)]
  else:
    nTable=[[] for i in range(20)]
  r = len(nTable)
  for i in oList:
    numC = ceil(len(i)/20)
    for j in range(numC):
      for k in range(r):
        if (j*r+k)<len(i):
          nTable[k]+= [i[j*20+k]]
        else:
          nTable[k] +=[""]
  return nTable

with open('words_alpha.txt') as f:
	my_list = [x.rstrip() for x in f if len(x) > 5 and len(x)<10]

#dictionary.meaning(word)


NewGame=True

while NewGame:
  word = my_list[randint(1, len(my_list))]
  while d.check(word)!= True and profanity.contains_profanity(word)!=True:
    word = my_list[randint(1, len(my_list))]

  print(word)
  
  answers, guesses, tWords = words(word)
  wGuessed = 0
  tGuessed = [0]*len(answers)
  Continue=True
  hints = 3
  while Continue and wGuessed!=tWords:
    print("\033[H\033[J",end="")
    print(word)
    pGuess = mTable(guesses)
    
    print(tabulate(pGuess))

    #print(guesses)
    print("\nYou have guessed {0} out of {2} words! \n{1:.2f}% there ".format(wGuessed, wGuessed*100 / tWords, tWords)) 
    print("Enter 0 to quit")
    print("Enter 1 for a hint ({0} left)".format(hints))

    guess = input("Enter a word you can make from this word (min length 3):\n")
    if guess == "1":
      if hints>0:
        i = randint(0,len(answers)-1)
        j = randint(0, len(answers[i])-1)
        while answers[i][j] in guesses[i]:
          i = randint(0,len(answers)-1)
          j = randint(0, len(answers[i])-1)
        guesses[i][tGuessed[i]] = answers[i][j]
        tGuessed[i]+= 1
        wGuessed+=1
        hints-=1
      else:
        print("Out of hints")
    elif guess=="0":
        pAnswers = mTable(answers)
        print(tabulate(pAnswers))
        Continue= False
    elif guess in guesses[len(guess)-3]:
      print("You guessed this already!")
    elif guess in answers[len(guess)-3]:
      guesses[len(guess)-3][tGuessed[len(guess)-3]] = guess
      wGuessed += 1
      tGuessed[len(guess)-3]+=1

      print("Good job!")
    
        

    else:
      print("Not quite!")
    
    sleep(.25)

  
  if wGuessed==tWords:
    pAnswers = mTable(answers)
    print(tabulate(pAnswers))
    print("Congrats you guesed them all!")
    sleep(.5)
  
  NG = input("Try a new word?").capitalize()
  if NG== "N" or NG== "NO":
    NewGame=False
  clearConsole()

  