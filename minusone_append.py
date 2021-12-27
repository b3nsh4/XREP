a=['[a-z]+', '[A-Z]', '[0-9]', '[A-Z]', '[0-9]', '[A-Z]', '[a-z]', '[A-Z]', '-', '[A-Z]+', '[a-z]+', '[A-Z]', '[0-9]', '[A-Z]+', '[a-z]+', '[A-Z]']

possible_alnum = ['[a-z]','[a-z]+','[A-Z]','[A-Z]+','[0-9]','[0-9]+',"\\w","\\w+"]

res= []

def alnum_algo(old,new): #old is the list for alnum filter, results to new ,both shoould be list
  for k in zip(old[::2],old[1::2]):
    temp = all(x in possible_alnum for x in k)
    print(k)
    if temp == True:
    	if len(new)==0:
    		new.append("\\w+")
    	elif new[-1]=="\\w+":
    		continue
    else:
    	for i in k:
        	new.append(i)
  
  if len(old)%2!=0:
  	print("odd")
		
		# if len(new)>1:
		# 	if old[-1] in possible_alnum and new[-1] == "\\w+":
		# 		new[-1]="\\w+"
		# 	else:
		# 		new.append(old[-1])
  

alnum_algo(a,res)
print("\nres",res)
