def wrappit(req):
	SED_PRE = f"sed -E -n '" #starting ' included

	SED_POST = f"/\\1/p'" #ending ' included

	FIND_PRE = f"re.findall(\"" 

	FIND_POST = f"\",TXT)"  

	GREP_PRE = f"grep -E -o '"
	
	GREP_POST = f"'"
	
	if req == "sed":
		PRE_WRAP =  SED_PRE
		POST_WRAP = SED_POST
	elif req == "pyre":
		PRE_WRAP = FIND_PRE
		POST_WRAP = FIND_POST
	elif req == "grep":
		PRE_WRAP = GREP_PRE
		POST_WRAP = GREP_POST
	return [PRE_WRAP,POST_WRAP]
