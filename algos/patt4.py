# pattern-4 or name whatever
#      .*pre-2(.+).{N}

# if pre-2 doesnot exist, use pre-1 

pre = "thisismy movu haha"
post = "perfect movie is feelgood"
pre_len = len(pre.split())
post_len = len(post)

def glolbal_len_decision(string):
	if len(string)>4: #checking if string is gt4
		gt4 = True
		shorted_str = string[:3]
		len_after_shorted = len(string[3:])
		return {"gt4":gt4,"shorted_str":shorted_str,"len_after_shorted":len_after_shorted}
	else:
		return {"gt4":False,"string":string}


def patt3():
	if pre_len!=0 and post_len!=0:
		if pre_len>=2:
			pre_2 = glolbal_len_decision(pre.split()[-1])
		else:
			pre_2 = pre.split()[0]
		print("len of post",".{",post_len,"}")

	elif pre_len==0 and post_len==0:
		print("no pre post")

	elif pre_len==0 and post_len!=0:
		print("no pre but post")

	elif pre_len!=0 and post_len==0:
		if pre_len>=2:
			pre_2 = glolbal_len_decision(pre.split()[1])
		else:
			pre_2= glolbal_len_decision(pre.split()[0])
		print("no post")

patt3()