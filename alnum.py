#algo to check adjacent same pair for alnum

target = ['orange','mango','CAR','apple','pineapple','grapes','BUS']
fruits = ['apple','orange','grapes','mango','pineapple']
lis = []

def alnum():
	for k in zip(target[::2],target[1::2]):
		temp = all(x in fruits for x in k)
		if temp == True:
		    lis.append("fruits")
		else:
			for i in k:
				lis.append(i)
	if len(target)%2!=0:
		if target[-1] in fruits and lis[-1] == "fruits" or lis[-1] == "fruit":
			lis[-1]="fruitZZ"
		else:
			lis.append(target[-1])
	return lis


print(alnum())