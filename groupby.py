from itertools import groupby
temp=[]
t=[]
a = ['a', ':', 'a', ':', 'b', 'a', 'b', 'a', 'b']
for k in zip(a[::2],a[1::2]):
	t.append(k)
if len(a)%2!=0:
	t.append(a[-1]) 

#grouping with numbering
for i,k in groupby(t):
	l=list(k)
	temp.append((i,len(l)))
#filtering from temp
final=""
for m in temp:
	t = ''.join(m[0])
	if m[1]>1:
		final+="("+t+")"+"{"+str(m[1])+"}"
	elif m[1]==1:
		final+=str(m[0])

print(temp)
print(final)

#algo to check adjacent same pair for alnum

# target = ['orange','mango','CAR','apple','pineapple','grapes','BUS']
# fruits = ['apple','orange','grapes','mango','pineapple']
# lis = []

# def alnum():
# 	for k in zip(target[::2],target[1::2]):
# 		temp = all(x in fruits for x in k)
# 		if temp == True:
# 		    lis.append("fruits")
# 		else:
# 			for i in k:
# 				lis.append(i)
# 	if len(target)%2!=0:
# 		if target[-1] in fruits and lis[-1] == "fruits" or lis[-1] == "fruit":
# 			lis[-1]="fruitZZ"
# 		else:
# 			lis.append(target[-1])
# 	return lis


# print(alnum())
# import itertools

# a = ["a", "a", "b", "b", "c", "c", "c", "c", "a", "a", "d"]

# pairs = zip(a[::2], a[1::2])
# groups = itertools.groupby(pairs)

# for pair, group in groups:
#     print(pair, list(group))