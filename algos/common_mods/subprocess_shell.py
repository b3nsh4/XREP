from echo_escape import echo_escaper
import subprocess
def run_shell(req,full_line):
   patt1 = req['pattern_1_result']
   patt2 = req['pattern_2_result']
   patt3 = req['pattern_3_result']
   patt4 = req['pattern_4_result']
   patt5 = req['pattern_5_result']
   patt6 = req['pattern_6_result']
   fresh_echo=echo_escaper(full_line)
   print("->",fresh_echo)
   patt1_op = subprocess.check_output('echo -e "'+fresh_echo+'" |'+patt1,shell=True).decode()
   if patt2!="non_useful_pattern":
      patt2_op = subprocess.check_output('echo -e "'+fresh_echo+'" |'+patt2,shell=True).decode()
   else:
      patt2_op = "non_useful_pattern"
   patt3_op = subprocess.check_output('echo -e "'+fresh_echo+'" |'+patt3,shell=True).decode()
   if patt4!="long_result_ignored":
      patt4_op = subprocess.check_output('echo -e "'+fresh_echo+'" |'+patt4,shell=True).decode()
   else:
      patt4_op = "long_result_ignored"
   if patt5!="Works_better_with_complex_patterns":
      patt5_op = subprocess.check_output('echo -e "'+fresh_echo+'" |'+patt5,shell=True).decode()
   else:
      patt5_op="Exit reason: ignored patt5"
   if patt6!="non_useful_pattern":
      patt6_op = subprocess.check_output('echo -e "'+fresh_echo+'" |'+patt6,shell=True).decode()
   else:
      patt6_op = "non_useful_pattern"
   final_res = {
      "patt1_shell_op":patt1_op,
      "patt2_shell_op":patt2_op,
      "patt3_shell_op":patt3_op,
      "patt4_shell_op":patt4_op,
      "patt5_shell_op":patt5_op,
      "patt6_shell_op":patt6_op,
   }
   return final_res
