escaper = ['.', '[',']', '{', '(', ')', '\\', '*', '+', '?', '|', '^', '$','/','"']

def escape_me(string):
  res = ""
  for i in string:
    if i in escaper:
      res+="\\"+i
    else:
      res+=i
  return res