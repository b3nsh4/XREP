# pre1.*pre2(target).*post1.*post2
import sys
sys.path.append('algos')
from improved_len_decision import glolbal_len_decision

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

def patt1_static_str(lhs,rhs,cooked_string,LINE_NUM,pre_has_space):
	if pre_has_space == True:
		p_space="\\s+"
	elif pre_has_space == False:
		p_space="\\s*"
	if len(lhs)!=0 and len(rhs)!=0:
		pre_res = lhs_static_str(lhs)
		post_res = rhs_static_str(rhs)
		pre1,pre2 = pre_res[0],pre_res[1]
		post1,post2 = post_res[0],post_res[1]
		return f"sed -E -n '{LINE_NUM}s/.*"+pre1+".*"+pre2+".*"+"("+p_space+(cooked_string)+").*"+post1+".*"+post2+"/\\1/p'"
		
	elif len(lhs)==0 and len(rhs)!=0:
		post_res = rhs_static_str(rhs)
		post1,post2 = post_res[0],post_res[1]
		return f"sed -E -n '{LINE_NUM}s/.*("+p_space+(cooked_string)+").*"+post1+".*"+post2+".*/\\1/p'"
	
	elif len(lhs)!=0 and len(rhs)==0:
		pre_res = lhs_static_str(lhs)
		pre1,pre2 = pre_res[0],pre_res[1]
		return f"sed -E -n '{LINE_NUM}s/.*"+pre1+".*"+pre2+".*("+p_space+(cooked_string)+").*/\\1/p'"
