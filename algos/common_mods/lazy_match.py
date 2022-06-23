from itertools import groupby
from lookup import alphas,num_class,big_alphas

def lazy_pattern(di_2):
	res = [list(group) for key,group in groupby(di_2,lambda x:x not in alphas and x not in num_class and x not in big_alphas)]
	return group_all(res)


def group_all(lis):
	grouped=[]
	for i in lis:
		if len(i)>1:
			temp=[]
			for k in i:
				if k in alphas:
					temp.append('a-z')
				elif k in big_alphas:
					temp.append('A-Z')
				elif k in num_class:
					temp.append('0-9')
				else:
					grouped.append(''.join(k))
			if len(temp) !=0:
				temp = list(dict.fromkeys(temp,None)) # no dups
				grouped.append(f"[{''.join(temp)}]+")
		else:
			grouped.append(''.join(i))
	return grouped

