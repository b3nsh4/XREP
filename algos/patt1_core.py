#### pre1.*pre2(target)post1.*post2 #A.K.A PATTERN-01
from escape_me import *

def glolbal_len_decision(string):
  if len(string)>4: #checking if string is gt4
    gt4 = True
    shorted_str = escape_me(string[:3])
    len_after_shorted = len(string[3:])
    return {"gt4":gt4,"shorted_str":shorted_str,"len_after_shorted":str(len_after_shorted)}
  else:
    return {"gt4":False,"string":string}

#lhs and rhs is the status of the checkbox, if checked we change it with []? else nothing

def foo(lhs,rhs,what,splitted_stuff):
  if lhs==True:
    lhs_1 = "["
    lhs_2 = "]?"
  else:
    lhs_1 = ""
    lhs_2 = ""

  if rhs==True:
    rhs_1 = "["
    rhs_2 = "]?"
  else:
    rhs_1 = ""
    rhs_2 = "" 
  if len(splitted_stuff)>=2:
    if len(splitted_stuff[0])>4:
      global_res_1 = glolbal_len_decision(splitted_stuff[0])
      bd1 = lhs_1+global_res_1["shorted_str"]+".{"+global_res_1["len_after_shorted"]+"}"+lhs_2
    else:
      bd1 = lhs_1+escape_me(splitted_stuff[0])+lhs_2

    if len(splitted_stuff[-1])>4:
      global_res_2 = glolbal_len_decision(splitted_stuff[-1])
      bd2 = rhs_1+global_res_2["shorted_str"]+".{"+global_res_2["len_after_shorted"]+"}"+rhs_2
    else: #len is lt 4 
      bd2 = rhs_1+escape_me(splitted_stuff[-1])+rhs_2
    final_res = bd1+".*"+bd2 #returns bd1.*bd2
    return final_res

  elif len(splitted_stuff)==1:
    if len(splitted_stuff[0])>4:
      global_res_1 = glolbal_len_decision(splitted_stuff[0])
      bd1 = lhs_1+global_res_1["shorted_str"]+".{"+global_res_1["len_after_shorted"]+"}"+lhs_2
    else: #if len is lt 4
      bd1 = lhs_1+escape_me(splitted_stuff[0])+lhs_2
    return bd1
  elif len(splitted_stuff)==0: #string is empty
    if what=="pre": #if pre strng is empty, retrun something relevant. so i return ^ and $ for the post
      return ""
    elif what=="post":
      return ""

def pat_1_ready(lhss,rhss,LINE_NUM,splitted_pre,splitted_post,prebd,postbd,cooked_string_copy,pre_h_space,post_h_space):

  bd1 =  foo(lhss,rhss,"pre",splitted_pre)
  bd2 = foo(lhss,rhss,"post",splitted_post)#put escape_me(fo....) here
  #checking for spaces
  if pre_h_space==True:
    pre_spc = "\\s+"
  elif pre_h_space==False:
    pre_spc = "\\s*"

  if post_h_space==True:
    post_spc="\\s+"
  elif post_h_space==False:
    post_spc="\\s*"

  return (f"sed -E -n '{LINE_NUM}s/{bd1}{pre_spc}({cooked_string_copy}){post_spc}{bd2}/\\1/p'")


# this worked becasue both strings were >4
# so we can achieve below output for pattern1

#algorithm
# - check if i have bd1 and bd2 for a given splitted_stuff
# - if yes, take 1st one as splitted_stuff[0] and last one as splitted_stuff[-1]
# - if len(splitted_stuff[0]) > 4 the run glolbal_len_decision else return the same string
# - if splitted_stuff len eq 1, then we take 0th element since it is nearest to target
# i.e bd(target)



#READY FOR BETA TEST !!!! CHECKOUT FOR SPACES IF OUTPUTS ARENOT WORKING

#For pattern-1, there is 2 pre1s and 2 pre2s - reason is above. therefore, if one select for
#LHS , it should be [pre-1]?.*pre2(cooked_string)[post-1]?.*post2