# .*pre-2(.+).{N}

# if pre-2 doesnot exist, use pre-1 
from escape_me import *

def glolbal_decision_6(string):
    if len(string)>4: #checking if string is gt4
        gt4 = True
        shorted_str = escape_me(string[:3])
        len_after_shorted = str(len(string[3:]))
        return shorted_str+".{"+len_after_shorted+"}"
    elif len(string)==0:
        return "" #if whatever is empty
    else:
        return escape_me(string)

def pattern_6_beta(lhs,rhs,LINE_NUM,preb,postb,pre_spc,post_spc):
    res = preb.split()

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
	    # print("pre a",preb,postb)
	    # print("postb",postb.split())
    if len(res)>=1:
        pre_res = escape_me(res[-1])
        try:
            final_post = glolbal_decision_6(postb.split()[0])
        except IndexError:
            return f"sed -E -n '{LINE_NUM}s/.*"+lhs_1+pre_res+lhs_2+"(.+)$/\\1/p'"

        if len(final_post)!=0:
            return f"sed -E -n '{LINE_NUM}s/.*"+lhs_1+pre_res+lhs_2+pre_spc+"(.+)"+post_spc+rhs_1+str(final_post)+rhs_2+".*/\\1/p'".format(LINE_NUM)
    elif len(postb.split())==0: #if len is zero for postb
        return f"sed -E -n '{LINE_NUM}s/.*^(.+).*$.*/\\1/p'".format(LINE_NUM)
    else:
        final_post = glolbal_decision_6(postb.split()[0])
        return f"sed -E -n '{LINE_NUM}s/.*^(.+).*"+rhs_1+str(final_post)+rhs_2+".*/\\1/p'"
# foo(pre)

"""
if needed, get text after target and set it as boundary from Js instead of using \\s+ 
"""