# pre1.*pre2(target).*post1.*post2
import sys
sys.path.append('algos')
from improved_len_decision import glolbal_len_decision

NonGreedyStatus=False

def lhs_static_str(lhs):
		if len(lhs)>=2:
			pre1=glolbal_len_decision(lhs[-2])
			pre2=glolbal_len_decision(lhs[-1])
			return [pre1,pre2]
		elif len(lhs)==1:
			pre1=""
			pre2=glolbal_len_decision(lhs[0])
			return [pre1,pre2]

def rhs_static_str(rhs):
		if len(rhs)>=2:
			post1=glolbal_len_decision(rhs[0])
			post2=glolbal_len_decision(rhs[1])
			return [post1,post2]
		elif len(rhs)==1:
			post1=glolbal_len_decision(rhs[0])
			post2=""
			return [post1,post2]

def patt1_static_str(pyre,GreedyStatus,lhs,rhs,cooked_string,LINE_NUM,pre_has_space):
	global pyre_1_result,NonGreedyStatus
	NonGreedyStatus = GreedyStatus

	if NonGreedyStatus:
		quantifier = ".*?"
	else:
		 quantifier = ".*"
	if pre_has_space == True:
		p_space="\\s+"
	elif pre_has_space == False:
		p_space="\\s*"
	if len(lhs)!=0 and len(rhs)!=0:
		pre_res = lhs_static_str(lhs)
		post_res = rhs_static_str(rhs)
		pre1,pre2 = pre_res[0],pre_res[1]
		
		if pre1=="":
			pre1=""
		else:
			pre1=pre1+quantifier
		
		if pre_has_space==True:
			pre2=pre2+quantifier
		else:
			pre2=pre2

		post1,post2 = post_res[0],post_res[1]
		
		if pyre==True:
			res = f"re.search(\"{quantifier}{pre1}{pre2}{p_space}({cooked_string}).*{post1}.*{post2}\",TXT)"
			return res
		elif pyre==False:
			return f"sed -E -n '{LINE_NUM}s/.*"+pre1+pre2+"("+p_space+(cooked_string)+").*"+post1+".*"+post2+"/\\1/p'"
		
	elif len(lhs)==0 and len(rhs)!=0:
		post_res = rhs_static_str(rhs)
		post1,post2 = post_res[0],post_res[1]
		
		if pre_has_space==True:
			if NonGreedyStatus:
				init_with = ".*?"
			else:
				init_with = ".*"
		else:
			init_with = "^"
		
		if post1!="":
			post1=post1+".*"
		if post2!="":
			post2=post2+".*"
		
		if pyre==True:
			res = f"re.search(\"{init_with}{p_space}{(cooked_string)}.*{post1}{post2}\",TXT)"
			return res
		elif pyre==False:
			return f"sed -E -n '{LINE_NUM}s/{init_with}("+p_space+(cooked_string)+").*"+post1+post2+"/\\1/p'"
	
	elif len(lhs)!=0 and len(rhs)==0:
		pre_res = lhs_static_str(lhs)
		pre1,pre2 = pre_res[0],pre_res[1]
		
		if pre1=="":
			pre1=""
		else:
			pre1=pre1+quantifier

		if pre_has_space==True:
			pre2=pre2+"" #REF-psb-01
		else:
			pre2=pre2
		
		if pyre==True:
			res  = f"re.search(\"{quantifier}{pre1}{pre2}{p_space}({cooked_string}).*\",TXT)"
			return res
		return f"sed -E -n '{LINE_NUM}s/.*"+pre1+pre2+"("+p_space+(cooked_string)+").*/\\1/p'"


"""
- Adding unnecessary .* causing wrong output
- we carefully add .* to pre2 only if p_space is True
- Since we have \\s+ infront of target \\s+(target) , we will get it fine
- But if i include a wildcard .*\\s*(target), then we will not get expected
- In those cases we use no wildcards assuming target and custom-brd is a same word
- example -> process 117 is (dead) now
- exmaple -> process 186 is (alive) now
- we can choose ( and ) as custom-brd, it's clear that it's one single word
- We should NOT use any wildcards here
- Post can/cannot have wildcards (which may be fine)
- It was also not good, eventho pre1 doesnot exist, hardcoding .* wildcard was appearing always
- psb-01: we cannot add a wildcard .* since no Postb exist will not get expected as its goes till end
"""