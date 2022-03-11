#READY FOR BETA TEST !!!! CHECKOUT FOR SPACES IF OUTPUTS ARENOT WORKING

# pattern-2: pre1.{N}(cookedsrsring)post1.{N}
from simple_cooker import final_cooker

escape = ['.', '[',']', '{', '(', ')', '\\', '*', '+', '?', '|', '^', '$','/','"']

def escape_me(string):
  res = ""
  for i in string:
    if i in escape:
      res+="\\"+i
    else:
      res+=i
  return res

def does_pre_post_exist(whatever):
	splitted = whatever.split()

	if len(splitted)>=1:
		exist = True
	else:
		exist= False
	return exist

def glolbal_len_decision(string):
	if len(string)>4: #checking if string is gt4
		escaped_string = escape_me(string) 
		gt4 = True
		shorted_str = escaped_string[:3] #uses escaped string
		# print("shorted_str",shorted_str)
		len_after_shorted = str(len(string[3:])) #uses non escaped string for count
		return shorted_str+".{"+len_after_shorted+"}"
	elif len(string)==0:
		return "" #if whatever is empty
	else:
		return escape_me(string) 

def pat_2_ready(whatever):
	if len(whatever)>=2:
		res = glolbal_len_decision(whatever[0])
		len_after_that = str(len(" ".join(whatever[1:]))+1)
		return res+".{"+len_after_that+"}" #put escape_me(res) if needed
	elif len(whatever)==1:
		res = glolbal_len_decision(whatever[0])
		return res #put escape_me(res) if needed
	else:
		return "" #if whatever is empty
# one = pat_2_ready(pre_split_on)
# two = pat_2_ready(post_split_on)
# print(one)
# print(two)

# REF:01 
# we take ['this', 'movie', 'is', 'feelgood'] 
# in this list, when we do 1: , it never counts the space b/w this and movie
# there we miss one space. we are sure that there will be space since we split()
# str(len(" ".join(pre_strip_split[1:]))+1) #reason why we added +1 read #ref:01


