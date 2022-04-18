# takes static strings from front and does follwing
# - seperate 'lhs' and 'rhs' in seperate lists from list of dicts
# - sorts in acordance with index within those lists

lhs_str = []
rhs_str = []

def static_arranger(arr):
	if len(arr)>1:
		for i in arr:
			if 'lhs' in i.values():
				lhs_str.append(i)
			elif 'rhs' in i.values():
				rhs_str.append(i)
			else:
				return "Something went wrong (static_arranger)"
	else:
		return arr

def sort_final(arr):
	arr=sorted(arr,key=lambda x: x['index'])

#manually clearing the list is needed since we only call the function and not entire script file
def clear_lis():
	lhs_str.clear()
	rhs_str.clear()

def static_res(arr):
	clear_lis()
	static_arranger(arr)
	if len(lhs_str)!=0:
		sort_final(lhs_str)
	if len(rhs_str)!=0: 
		sort_final(rhs_str)
	return {"lhs_arr_sorted":lhs_str,"rhs_arr_sorted":rhs_str}