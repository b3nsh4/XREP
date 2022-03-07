# in tuple, adjacent values may repeat, so we have to remove it
#[(('\\w+', '\\w+'), 2), (('-', '[A-Z]'), 1)] <-- an example
from itertools import groupby
possible_alnum = ['[a-z]','[a-z]+','[A-Z]','[A-Z]+','[0-9]','[0-9]+',"\\w","\\w+"]
new=[]
x = ['[a-z]', '[A-Z]', '[0-9]', '[A-Z]', '[0-9]', '[A-Z]', '[a-z]', '[A-Z]', '-', '[A-Z]']

def alnum_algo(old,new): #old is the list for alnum filter, results to new ,both shoould be list
  for k in zip(old[::2],old[1::2]):
     temp = all(x in possible_alnum for x in k)
     if temp == True:
         new.append("\\w+")
     else:
        for i in k:
           new.append(i)
  if len(old)%2!=0:
     if len(new)>1:
        if old[-1] in possible_alnum and new[-1] == "\\w" or new[-1] == "\\w+":
           new[-1]="\\w+"
        else:
           new.append(old[-1])

alnum_algo(x,new)
res = [i[0] for i in groupby(new)]
print(res)