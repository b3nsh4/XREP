# .*pre-2(.+).{N}
from wrapper import *
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

def pattern_6_beta(grep,
        pyre,
        GreedyStatus,
        lhs,
        rhs,
        LINE_NUM,
        preb,
        postb,
        pre_spc,
        post_spc
):
    if GreedyStatus:
        quantifier = ".*?"
    else:
        quantifier = ".*"
    
    res = preb.split()
    if lhs==True and rhs==True:
        return "non_useful_pattern"

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

    if len(res)>=1:
        pre_res = escape_me(res[-1])
        try:
            final_post = glolbal_decision_6(postb.split()[0])
        except IndexError:
            if pyre:
                res = f"re.findall(\"{quantifier}{lhs_1}{pre_res}{lhs_2}{pre_spc}([^ ]+)$\",TXT)"
                return res
            elif grep:
                res = f"{GREP_PRE}{pre_spc}[^ ]+${GREP_POST}"
                return res
            else:
                res = f"sed -E -n '{LINE_NUM}s/.*{lhs_1}{pre_res}{lhs_2}{pre_spc}([^ ]+)$/\\1/p'"
                return res
        if len(final_post)!=0:
            if pyre==True:
                res = f"re.findall(\"{quantifier}{lhs_1}{pre_res}{lhs_2}{pre_spc}([^ ]+){post_spc}{rhs_1}{str(final_post)}{rhs_2}.*\",TXT)"
                return res
            else:
                return f"sed -E -n '{LINE_NUM}s/.*{lhs_1}{pre_res}{lhs_2}{pre_spc}(.+){post_spc}{rhs_1}{str(final_post)}{rhs_2}.*/\\1/p'"
    
    elif len(postb.split())==0: #if len is zero for postb
        if pyre==True:
            res =  f"re.findall(\"^([^ ]+){post_spc}$\",TXT)"
            return res
        elif pyre==False:
            return f"sed -E -n '{LINE_NUM}s/^([^ ]+){post_spc}$/\\1/p'"
    else:
        final_post = glolbal_decision_6(postb.split()[0])
        
        if pyre==True:
            res = f"re.findall(\"^([^ ]+){post_spc}{rhs_1}{str(final_post)}{rhs_2}.*\",TXT)"
            return res
        elif pyre==False:
            return f"sed -E -n '{LINE_NUM}s/^([^ ]+){post_spc}{rhs_1}{str(final_post)+rhs_2}.*/\\1/p'"


"""
if needed, get text after target and set it as boundary from Js instead of using \\s+ 
- When RHS-vary, we use [^ ]+ since, no RHS
- We can't use (.+) as it goes till EOL since no RHS
- When LHS-vary, we use (.+) since RHS is present, it won't go EOL
- If LHS-vary and RHS-vary, return "Not useful pattern" 

"""
