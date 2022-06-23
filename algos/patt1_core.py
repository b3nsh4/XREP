#### pre1.*pre2(target)post1.*post2 #A.K.A PATTERN-01
## pre1 is splitted[0] and pre2 is splitted[-1] post1, post2 accordingly
from escape_me import *
NonGreedyStatus=False

def glolbal_len_decision(string):
  if len(string)>4: #checking if string is gt4
    gt4 = True
    shorted_str = escape_me(string[:3])
    len_after_shorted = len(string[3:])
    return {"gt4":gt4,"shorted_str":shorted_str,"len_after_shorted":str(len_after_shorted)}
  else:
    return {"gt4":False,"string":string}

#lhs and rhs is the status of the checkbox, if checked we change it with []? else nothing

def cute_cut(h1,h2,splitted_stuff):
  if NonGreedyStatus:
    quantifier = ".*?"
  else:
    quantifier=".*"
  
  if len(splitted_stuff)>=2:
    if len(splitted_stuff[0])>4:
      global_res_1 = glolbal_len_decision(splitted_stuff[0])
      bd1 = h1+global_res_1["shorted_str"]+".{"+global_res_1["len_after_shorted"]+"}"+h2
    else:
      bd1 = h1+escape_me(splitted_stuff[0])+h2

    if len(splitted_stuff[-1])>4:
      global_res_2 = glolbal_len_decision(splitted_stuff[-1])
      bd2 = h1+global_res_2["shorted_str"]+".{"+global_res_2["len_after_shorted"]+"}"+h2
    else: #len is lt 4 
      bd2 = h1+escape_me(splitted_stuff[-1])+h2
    final_res = bd1+quantifier+bd2 #returns bd1.*bd2
    return final_res

  elif len(splitted_stuff)==1:
    if len(splitted_stuff[0])>4:
      global_res_1 = glolbal_len_decision(splitted_stuff[0])
      bd1 = h1+global_res_1["shorted_str"]+".{"+global_res_1["len_after_shorted"]+"}"+h2
    else: #if len is lt 4
      bd1 = h1+escape_me(splitted_stuff[0])+h2
    return bd1
  elif len(splitted_stuff)==0: #string is empty
    return ""

def pat_1_ready(pyre,GreedyStatus,lhss,rhss,LINE_NUM,splitted_pre,splitted_post,prebd,postbd,cooked_string_copy,pre_spc,post_spc):
  global NonGreedyStatus
  NonGreedyStatus = GreedyStatus
  h1 = "["
  h2 = "]?"
  no_h1 = ""
  no_h2= ""
  global pyre_1_result
  
  if lhss==True:
    bd1 = cute_cut(h1,h2,splitted_pre)
  elif lhss==False:
    bd1 = cute_cut(no_h1,no_h2,splitted_pre)
  
  
  if rhss==True:
    bd2 = cute_cut(h1,h2,splitted_post)#put escape_me(fo....) here
  elif rhss==False:
    bd2 = cute_cut(no_h1,no_h2,splitted_post)
  
  #checks if user needs POSIX or Pyre
  if pyre==True:
    res = f"re.findall(\"{bd1}{pre_spc}({cooked_string_copy}){post_spc}{bd2}.*\",TXT)"
    return res
  elif pyre==False:
    return (f"sed -E -n '{LINE_NUM}s/{bd1}{pre_spc}({cooked_string_copy}){post_spc}{bd2}.*/\\1/p'")


# this worked becasue both strings were >4
# so we can achieve below output for pattern1

#algorithm
# - check if i have bd1 and bd2 for a given splitted_stuff
# - if yes, take 1st one as splitted_stuff[0] and last one as splitted_stuff[-1]
# - if len(splitted_stuff[0]) > 4 the run glolbal_len_decision else return the same string
# - if splitted_stuff len eq 1, then we take 0th element since it is nearest to target
# i.e bd(target)

#For pattern-1, there is 2 pre1s and 2 pre2s - reason is above. therefore, if one select for
#LHS , it should be [pre-1]?.*pre2(cooked_string)[post-1]?.*post2