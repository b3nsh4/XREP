
SED_PRE = f"sed -E -n '" #starting ' included

SED_POST = f"/\\1/p'" #ending ' included

FIND_PRE = f"re.findall(\"" 

FIND_POST = f"\",TXT)"  

GREP_PRE = f"grep -E -o '"

GREP_POST = f"'"