from echo_escape import echo_escaper
import subprocess
def run_shell(req):
   patt1 = req['patt1']
   patt2 = req['patt2']
   patt3 = req['patt3']
   patt4 = req['patt4']
   patt5 = req['patt5']
   patt6 = req['patt6']
   full_line = req['full_line'][0]
   fresh_echo=echo_escaper(full_line)
   print("->",fresh_echo)
   patt1_op = subprocess.check_output('echo -e "'+fresh_echo+'" |'+patt1,shell=True).decode()
   patt2_op = subprocess.check_output('echo -e "'+fresh_echo+'" |'+patt2,shell=True).decode()
   patt3_op = subprocess.check_output('echo -e "'+fresh_echo+'" |'+patt3,shell=True).decode()
   patt4_op = subprocess.check_output('echo -e "'+fresh_echo+'" |'+patt4,shell=True).decode()
   if patt5!="Works_better_with_complex_patterns":
      patt5_op = subprocess.check_output('echo -e "'+fresh_echo+'" |'+patt5,shell=True).decode()
   else:
      patt5_op="Exit reason: ignored patt5"
   patt6_op = subprocess.check_output('echo -e "'+fresh_echo+'" |'+patt6,shell=True).decode()
   final_res = {
      "patt1_shell_op":patt1_op,
      "patt2_shell_op":patt2_op,
      "patt3_shell_op":patt3_op,
      "patt4_shell_op":patt4_op,
      "patt5_shell_op":patt5_op,
      "patt6_shell_op":patt6_op,
   }
   return final_res
