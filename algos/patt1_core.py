
#### pre1.*pre2(target)post1.*post2 #A.K.A PATTERN-01
#READY FOR BETA TEST !!!! CHECKOUT FOR SPACES IF OUTPUTS ARENOT WORKING

# string_1 = "ADYdd FOR BETA TES"
# string_2 = "ADY FOR BETA TES"
# splitted_pre = string_1.split()
# splitted_post = string_2.split()
#checking if pre1 pre2 and post1 post2 exist
#if both exist, we use patt1_bndry_gt2 else eq1

escape = ['.', '[', '{', '(', ')', '\\', '*', '+', '?', '|', '^', '$','/','"']

def escape_me(string):
  res = ""
  for i in string:
    if i in escape:
      res+="\\"+i
    else:
      res+=i
  return res

def spacer_finder(pre_or_post,stuff):  #pre2\s?(target)\s?post
  if pre_or_post=="pre":
    splitted_stuff = stuff.lstrip().split(" ")

    if splitted_stuff[-1] == "":
      space_before = True
    else:
      space_before = False
    return space_before
  
  elif pre_or_post=="post":
    
    splitted_stuff = stuff.rstrip().split(" ")
    if splitted_stuff[0] == "":
      space_after = True
    else:
      space_after = False
    return space_after

def glolbal_len_decision(string):
	if len(string)>4: #checking if string is gt4
		gt4 = True
		shorted_str = string[:3]
		len_after_shorted = len(string[3:])
		return {"gt4":gt4,"shorted_str":shorted_str,"len_after_shorted":str(len_after_shorted)}
	else:
		return {"gt4":False,"string":string}

def foo(what,splitted_stuff):
  if len(splitted_stuff)>=2:
    if len(splitted_stuff[0])>4:
      global_res_1 = glolbal_len_decision(splitted_stuff[0])
      bd1 = global_res_1["shorted_str"]+".{"+global_res_1["len_after_shorted"]+"}"
    else:
      bd1 = splitted_stuff[0]

    if len(splitted_stuff[-1])>4:
      global_res_2 = glolbal_len_decision(splitted_stuff[-1])
      bd2 = global_res_2["shorted_str"]+".{"+global_res_2["len_after_shorted"]+"}"
    else:
      bd2 = splitted_stuff[-1]
    final_res = bd1+".*"+bd2 #returns bd1.*bd2
    return final_res
  
  elif len(splitted_stuff)==1:
    if len(splitted_stuff[0])>4:
      global_res_1 = glolbal_len_decision(splitted_stuff[0])
      bd1 = global_res_1["shorted_str"]+".{"+global_res_1["len_after_shorted"]+"}"
    else:
      bd1 = splitted_stuff[0]
    return bd1
  elif len(splitted_stuff)==0: #string is empty
    if what=="pre": #if pre strng is empty, retrun something relevant. so i return ^ and $ for the post
      return ""
    elif what=="post":
      return ""


def pat_1_ready(splitted_pre,splitted_post,prebd,postbd,cooked_string_copy):
  bd1 = foo("pre",splitted_pre)
  bd2 = foo("post",splitted_post) #put escape_me(fo....) here

  #checking for spaces
  pre_has_space = spacer_finder("pre",prebd)
  post_has_space = spacer_finder("post",postbd)

  if pre_has_space ==True and post_has_space==True:
    return (f"sed -E -n 's/{bd1}\\s*({cooked_string_copy})\\s*{bd2}/\\1/p'")

  elif pre_has_space ==False and post_has_space==False:
    return (f"sed -E -n 's/{bd1}({cooked_string_copy}){bd2}/\\1/p'")

  elif pre_has_space == True and post_has_space== False:
    return (f"sed -E -n 's/{bd1}\\s*({cooked_string_copy}){bd2}/\\1/p'")

  elif pre_has_space == False and post_has_space ==True:
    return (f"sed -E -n 's/{bd1}({cooked_string_copy})\\s*{bd2}/\\1/p'")

# this worked becasue both strings were >4
# so we can achieve below output for pattern1

#algorithm
# - check if i have bd1 and bd2 for a given splitted_stuff
# - if yes, take 1st one as splitted_stuff[0] and last one as splitted_stuff[-1]
# - if len(splitted_stuff[0]) > 4 the run glolbal_len_decision else return the same string
# - if splitted_stuff len eq 1, then we take 0th element since it is nearest to target
# i.e bd(target)
