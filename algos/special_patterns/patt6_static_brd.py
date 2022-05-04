# .*pre2-static(.+).{N}

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


def patt6_static_brd(LINE_NUM,preb,postb,pre_spc,post_spc,lhs_static_str):
    pre_str = glolbal_decision_6(lhs_static_str[-1])
    res = preb.split()
    if len(res)>=1:
        pre_res = escape_me(res[-1])
        try:
            final_post = glolbal_decision_6(postb.split()[0])
        except IndexError:
            return f"sed -E -n '{LINE_NUM}s/.*"+pre_str+"([^ ]+)$/\\1/p'"

        if len(final_post)!=0:
            return f"sed -E -n '{LINE_NUM}s/.*"+pre_str+pre_spc+"(.+)"+post_spc+str(final_post)+".*/\\1/p'".format(LINE_NUM)
    elif len(postb.split())==0: #if len is zero for postb
        return f"sed -E -n '{LINE_NUM}s/^([^ ]+){post_spc}.*$.*/\\1/p'".format(LINE_NUM)
    else:
        final_post = glolbal_decision_6(postb.split()[0])
        return f"sed -E -n '{LINE_NUM}s/^([^ ]+){post_spc}.*"+str(final_post)+".*/\\1/p'"


"""
if needed, get text after target and set it as boundary from Js instead of using \\s+ 
"""