"""
This script runs and tests the generated pattern and returns the executed result in a shell.
Since it runs in a shell, it must be carefully done and hence put in an alpha version as of: Jul 23 - 23
"""

from echo_escape import echo_escaper
import re

def run_pyre_shell(req,fullline):
	patt1 = req['pattern_1_result']
	patt2 = req['pattern_2_result']
	patt3 = req['pattern_3_result']
	patt4 = req['pattern_4_result']
	patt5 = req['pattern_5_result']
	patt6 = req['pattern_6_result']
	TXT=echo_escaper(fullline)

	try:
		patt1_shell_op=str(eval(patt1))
		if patt1_shell_op=="()":
			patt1_shell_op=str(eval(patt1).group())
	# except AttributeError:
	except Exception as e:
		patt1_shell_op=f"Run-Test bug,please report this: {e}"
	
	try:
		patt2_shell_op=str(eval(patt2))
		if patt2_shell_op=="()":
			patt2_shell_op=str(eval(patt2).group())
	except Exception as e:
		patt2_shell_op = f"Run-Test bug,please report this: {e}"
	
	if patt4!="long_result_ignored":
		try:
			patt4_shell_op=str(eval(patt4))
			if patt4_shell_op=="()":
				patt4_shell_op = str(eval(patt4).group())
		except Exception as e:
			patt4_shell_op = f"Something went wrong, please report this: {e}"
	else:
		patt4_shell_op="long_result_ignored"
	
	try:
		if patt5!="Works_better_with_complex_patterns":
			patt5_shell_op=str(eval(patt5))
			if patt5_shell_op=="()":
				patt5_shell_op = str(eval(patt5).group())
		else:
				patt5_shell_op = "Works_better_with_complex_patterns"
	except Exception as e:
		patt5_shell_op = f"Run-Test bug,please report this: {e}"
	
	try:
		patt6_shell_op=str(eval(patt6))
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


