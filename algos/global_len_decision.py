def glolbal_len_decision(string):
	if len(string)>4:
		gt4 = True
		shorted_str = string[:3]
		len_after_shorted = len(string[3:])
		return {"gt4":gt4,"shorted_str":shorted_str,"len_after_shorted":len_after_shorted}
	else:
		return {"gt4":False,"string":string}

res = glolbal_len_decision("thisiss")
if res["gt4"]==True:
	print (res["shorted_str"]+".{"+str(res["len_after_shorted"])+"}")
else:
	print("ngt4",res["string"])