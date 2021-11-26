a=[(('a', ':'), 2), (('b', 'a'), 2), (('b','d'), 1)]

temp=""
for i in a:
	t = ''.join(i[0])
	if i[1]>1:
		temp+="("+t+")"+"{"+str(i[1])+"}"
	elif i[1]==1:
		for n in i[0]:
			temp+=n

print(temp)