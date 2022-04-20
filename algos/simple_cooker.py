
#designed for PATTERN-2 boundaries

from lookup import *

di_2 = []

def alnum_algo(old,new): #old is the list for alnum filter, results to new ,both shoould be list
  for k in zip(old[::2],old[1::2]):
     temp = all(x in possible_alnum for x in k)
     if temp == True:
         new.append("\\w+")
     else:
        for i in k:
          new.append(i)
  if len(old)%2!=0:
    if len(new)>=1:
      if old[-1] in possible_alnum and new[-1] == "\\w+":
        new[-1]="\\w+"
      elif old[-1] in possible_alnum and new[-1] in possible_alnum:
        new[-1]="\\w+"
      else:
        new.append(old[-1])
  return new

def simple_chef(string):


  #global variables for this function#
  i=0

  di = [] #used to loop through string and saves here eg: in abc or ABC or nums ..etc

 #simplified di with + for repetative values

  di_3 = [] #alnum 

  di_4 = [] #2nd stage alnum filtering

  di_5 = [] #3rd stage(in some case, NOt using NOW)

  while (i<len(string)):
    if string[i] in abc:
      di.append("\\w") #replaced [a-z] with w
      i+=1
    elif string[i] in ABC:
      di.append("\\w") #replaced [A-Z] with w
      i+=1
    elif string[i] in nums:
      di.append("\\w")
      i+=1
    elif string[i] in space:
      di.append("\\s+")
      i+=1
    elif string[i] in escape:
       di.append("\\"+string[i])
       i+=1
    else:
      di.append(string[i])
      i+=1

  # if len(di)==2:
  #   if di[0] == di[1]:
  #     temp_val = di[0]
  #     di.clear()
  #     di.append(str(temp_val+"+")) #adding + to same
  #   elif di[0] in possible_alnum and di[1] in possible_alnum:
  #     di.clear()
  #     di.append("\\w+") #ignored using [[:alnum:]]
    
  # fn = ""
  # for k in di:
  #   fn+=k
  # return fn #final as string!
  return di

def final_cooker(string):
  if len(string)==1:
    x=""
    fnl = simple_chef(string)
    for i in fnl: #because simple_chef returns list, we need to convert to str
      x+=str(i)
    return x
  else:
    x=""
    fnl = alnum_algo(simple_chef(string),di_2)
    for i in fnl:
      x+=str(i)
    return x

# print(final_cooker("s:")) <-- can be used for debugging

#this seems to be working well, it'll pair adjacent  duplicates with +
#if it's like [':','\w','\w'] it'll match the len(lis)%2!=0 condition
#then compares again to makeupwith it
#problem [':','\w','\w']
#expected [':','\w+']
#fixed