# pattern-2: pre1.{N}(cookedsrsring)post1.{N}

from improved_len_decision import glolbal_len_decision
from simple_cooker import final_cooker
from escape_me import *

def count_by_spc(preb): #[^ ]\s+{N}
	init_count = 0
	for i in preb:
		if i == " ":
			init_count+=1
	split_preb = preb.split(" ")
	if split_preb[-1]==" ":
		return '.{'+str(init_count)+'}'
	elif split_preb[-1]!=" ":
		return '{'+str(init_count)+'}'+'.{'+str(len(split_preb[-1]))+'}'

def pat_2_ready(whatever,pre_boundary):
	if len(whatever)>=2:
		res = "([^ ]+\\s+)"
		return res+count_by_spc(pre_boundary)
	elif len(whatever)==1:
		res = glolbal_len_decision(whatever[0])
		return res #put escape_me(res) if needed
	else:
		return "" #if whatever is empty

# REF:01 
# we take ['this', 'movie', 'is', 'feelgood'] 
# in this list, when we do 1: , it never counts the space b/w this and movie
# there we miss one space. we are sure that there will be space since we split()
# str(len(" ".join(pre_strip_split[1:]))+1) #reason why we added +1 read #ref:01


