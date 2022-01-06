# pattern-4 or name whatever
# .*pre-2(.+).{N}

# if pre-2 doesnot exist, use pre-1 


#TODO -- ESCAPE /

pre = "manife"
post = "this movie is feelgood"
pre_len = len(pre.split())
post_len = len(post)

def pattern_6_beta(whatever):
	res = whatever.split()
	if len(res)>=1:
		pre_res = res[-1]
		if post_len!=0:
			return "sed -E -n 's/.*"+pre_res+"(.+).{"+str(post_len)+"}/\\1/p'"
		else:
			return "sed -E -n 's/.*"+pre_res+"(.+)$/\\1/p'".format(cooked_string)
	else:
		return "sed -E -n 's/.*^(.+).{"+str(post_len)+"}/\\1/p'".format(cooked_string)
# foo(pre)

