#READY FOR BETA TEST !!!! CHECKOUT FOR SPACES IF OUTPUTS ARENOT WORKING

# pattern-2: pre1.{N}(cookedsrsring)post1.{N}

pre = "sds sdkds sduj"
post = "dddddd konf stroy"
pre_len = len(pre.split())
post_len = len(post.split())

pre_split_on = pre.lstrip().split(" ")
post_split_on = post.lstrip().split(" ")

def does_pre_post_exist(whatever):
	splitted = whatever.split()

	if len(splitted)>=1:
		exist = True
	else:
		exist= False
	return exist

def glolbal_len_decision(string):
	if len(string)>4: #checking if string is gt4
		gt4 = True
		shorted_str = string[:3]
		len_after_shorted = str(len(string[3:]))
		return shorted_str+".{"+len_after_shorted+"}"
	elif len(string)==0:
		return "empty"
	else:
		return string

def foo(whatever):
	if len(whatever)>=2:
		res = glolbal_len_decision(whatever[0])
		len_after_that = str(len(" ".join(whatever[1:]))+1)
		return res+".{"+len_after_that+"}"
	elif len(whatever)==1:
		res = glolbal_len_decision(whatever[0])
		return res
	else:
		return "empty"
one = foo(pre_split_on)
two = foo(post_split_on)
print(one)
print(two)

# REF:01 
# we take ['this', 'movie', 'is', 'feelgood'] 
# in this list, when we do 1: , it never counts the space b/w this and movie
# there we miss one space. we are sure that there will be space since we split()
# str(len(" ".join(pre_strip_split[1:]))+1) #reason why we added +1 read #ref:01


