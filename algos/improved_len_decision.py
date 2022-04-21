from escape_me import *

def glolbal_len_decision(string):
   if len(string)>4: #checking if string is gt4
      # escaped_string = escape_me(string) escaping in prior
      gt4 = True
      shorted_str = string[:3] #uses escaped string
      len_after_shorted = str(len(string[3:])) #uses non escaped string for count
      return escape_me(shorted_str)+".{"+len_after_shorted+"}" #escaping after shorted
   elif len(string)==0:
      return "" #if whatever is empty
   else:
      return escape_me(string) 


'''
in essence escaping after shorting is better to avoid edge cases like below
   for abc/123
   will give -> abc\.{4} instead of abc.{4}   
'''