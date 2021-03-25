#Game to guess all of the words in another word

#See what percentage you get

import enchant
d = enchant.Dict("en_US")
#d.check("Hello")

#d.check("Helo")

#d.suggest("Helo")
#['He lo', 'He-lo', 'Hello', 'Helot', 'Help', 'Halo', 'Hell', 'Held', 'Helm', 'Hero', "He'll"]

#file1 = open("words_alpha.txt","r")
from random import randint

from itertools import permutations

def words(letters):
    for n in range(1, len(letters)+1):
        yield from map(''.join, permutations(letters, n))

with open('words_alpha.txt') as f:
    my_list = [x.rstrip() for x in f if len(x)>5]

print(len(my_list))
x=my_list[randint(1,len(my_list))]
print(x)
wSet = set(words(x))
#answers = []
for word in wSet:
  if len(word)>2 and d.check(word):
    print(word)