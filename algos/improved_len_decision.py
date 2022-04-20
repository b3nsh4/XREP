from escape_me import *

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