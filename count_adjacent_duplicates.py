from itertools import groupby
a=['[a-z]', '[a-z]', '[a-z]', '[a-z]', 'bus', 'apple','bus','bus']
string = ""
temp = []
l = []

for j,k in groupby(a):
    l=list(k)
    temp.append((j,len(l)))
for i in temp:
    if i[1]>1:
        stuff= str(i[0])
        count = str(i[1])
        print(stuff,count)
        string+="("+stuff+")"+"{"+count+"}"
    elif i[1]==1:
        stuff=str(i[0])
        string+=stuff

print(string)