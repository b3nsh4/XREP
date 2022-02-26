
#READY FOR BETA TEST !!!! CHECKOUT FOR SPACES IF OUTPUTS ARENOT WORKING

# pattern-3 or name whatever
#      .*pre-2\s*([^ ]+.+)\s*post-1.*

# if pre-2 doesnot exist, use pre-1 

pre = "2 packets transmitted, 1 received,"
post = "packet loss, time 1001ms"
pre_len = len(pre.split())
post_len = len(post.split())

def glolbal_len_decision(string):
	if len(string)>4: 
		gt4 = True
		shorted_str = string[:3]
		len_after_shorted = len(string[3:])
		return shorted_str+".{"+str(len_after_shorted)+"}"
	else:
		return string


def func(pre_or_post,whatever):
	if pre_or_post=="pre":
		if pre_len>=1:
			res = glolbal_len_decision(whatever.split()[-1])
			return ".*"+res
		else:
			return "no pre"
	elif pre_or_post=="post":
		if post_len>=1:
			res = glolbal_len_decision(whatever.split()[0])
			return res+".*"
		else:
			return "no post"

result1 = func("pre",pre)
result2 = func("post",post)
print(result1,"\n",result2)