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

	patt1_shell_op=str(eval(patt1).groups()),
	patt2_shell_op=str(eval(patt2).groups()),
	patt3_shell_op="___",
	if patt4!="long_result_ignored":
		patt4_shell_op=str(eval(patt4).groups()),
	else:
		patt4_shell_op="long_result_ignored"
	patt5_shell_op=str(eval(patt5).groups()),
	patt6_shell_op=str(eval(patt6).groups())
	
	final_res = {
	"patt1_shell_op":patt1_shell_op,
	"patt2_shell_op":patt2_shell_op,
	"patt3_shell_op":"___",
	"patt4_shell_op":patt4_shell_op,
	"patt5_shell_op":patt5_shell_op,
	"patt6_shell_op":patt6_shell_op
	}
	return final_res

