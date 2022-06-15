def pyre_escaper(string):
	res=""
	for i in string:
		if i == "'":
			res+="\\"+i
		else:
			res+=i
	return res

