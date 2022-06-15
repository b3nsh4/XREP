from echo_escape import echo_escaper

import re

def run_pyre_shell(req):
	patt1 = req['patt1']
	patt2 = req['patt2']
	patt3 = req['patt3']
	patt4 = req['patt4']
	patt5 = req['patt5']
	patt6 = req['patt6']
	full_line = req['full_line'][0]
	TXT=echo_escaper(full_line)

	try:
		patt1_shell_op=str(eval(patt1).groups())
		if patt1_shell_op=="()":
			patt1_shell_op=str(eval(patt1).group())
	# except AttributeError:
	except Exception as e:
		patt1_shell_op=f"Run-Test bug,please report this: {e}"
	
	try:
		patt2_shell_op=str(eval(patt2).groups())
		if patt2_shell_op=="()":
			patt2_shell_op=str(eval(patt2).group())
	except Exception as e:
		patt2_shell_op = f"Run-Test bug,please report this: {e}"
	
	if patt4!="long_result_ignored":
		try:
			patt4_shell_op=str(eval(patt4).groups())
			if patt4_shell_op=="()":
				patt4_shell_op = str(eval(patt4).group())
		except Exception as e:
			patt4_shell_op = f"Something went wrong, please report this: {e}"
	else:
		patt4_shell_op="long_result_ignored"
	
	try:
		if patt5!="Works_better_with_complex_patterns":
			patt5_shell_op=str(eval(patt5).groups())
			if patt5_shell_op=="()":
				patt5_shell_op = str(eval(patt5).group())
		else:
				patt5_shell_op = "Works_better_with_complex_patterns"
	except Exception as e:
		patt5_shell_op = f"Run-Test bug,please report this: {e}"
	
	try:
		patt6_shell_op=str(eval(patt6).groups())
		if patt6_shell_op=="()":
			patt6_shell_op=str(eval(patt6).group())
	except Exception as e:
		patt6_shell_op = f"Run-Test bug,please report this: {e}"
	try:
		patt3_shell_op = str(eval(patt3))
	except Exception as e:
		patt3_shell_op = f"Run-Test bug,please report this: {e}"
	
	final_res = {
	"patt1_shell_op":patt1_shell_op,
	"patt2_shell_op":patt2_shell_op,
	"patt3_shell_op":patt3_shell_op,
	"patt4_shell_op":patt4_shell_op,
	"patt5_shell_op":patt5_shell_op,
	"patt6_shell_op":patt6_shell_op
	}
	return final_res

def conv_to_group(res):
	for key,val in res.items():
		if res[key]=="()":
			res[key]="Exact Match: use re.group()"
	return res


