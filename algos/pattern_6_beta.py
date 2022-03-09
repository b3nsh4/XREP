# pattern-4 or name whatever
# .*pre-2(.+).{N}

# if pre-2 doesnot exist, use pre-1 


#TODO -- ESCAPE /
def escape_brakt(this):
	bkts = ['[',']', '{', '(', ')', '\\', '*', '+', '?', '|', '^', '$','/','"']
	res = ""
	for i in this:
		if i in bkts:
			res+="\\"+i
		else:
			res+=i
	return res

def glolbal_decision_6(string):
	if len(string)>4: #checking if string is gt4
		 gt4 = True
		 shorted_str = escape_brakt(string[:3])
		 len_after_shorted = str(len(string[3:]))
		 return shorted_str+".{"+len_after_shorted+"}"
	elif len(string)==0:
		 return "" #if whatever is empty
	else:
		 return escape_brakt(string)

def pattern_6_beta(LINE_NUM,preb,postb):
	res = preb.split()
	# print("postb",postb.split())
	if len(res)>=1:
		pre_res = escape_brakt(res[-1])
		try:
			final_post = glolbal_decision_6(postb.split()[0])
		except IndexError:
			return "sed -E -n '{}s/.*"+pre_res+"(.+)$/\\1/p'".format(LINE_NUM)

		if len(final_post)!=0:
			return f"sed -E -n '{LINE_NUM}s/.*"+pre_res+"(.+)\\s*"+str(final_post)+".*/\\1/p'".format(LINE_NUM)
	elif len(postb.split())==0: #if len is zero for postb
		return f"sed -E -n '{LINE_NUM}s/.*^(.+).*$.*/\\1/p'".format(LINE_NUM)
	else:
		final_post = glolbal_decision_6(postb.split()[0])
		return f"sed -E -n '{LINE_NUM}s/.*^(.+).*"+str(final_post)+".*/\\1/p'"
# foo(pre)

