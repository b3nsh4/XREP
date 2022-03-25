from flask import Flask,render_template,request,jsonify,make_response
from itertools import groupby
import json
import uuid
from github import Github
import sys
sys.path.append('algos')
from patt1_core import pat_1_ready,escape_brakt
from patt2_core import pat_2_ready
from pattern_6_beta import pattern_6_beta
from simple_cooker import simple_chef,final_cooker
app = Flask(__name__)
g = Github('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')
repo = g.get_repo("b3nsh4/XREP_BUG_REPORTS")

@app.route('/')
def getstarted():
   return render_template('index.html')

@app.route("/entry", methods=["POST","GET"])
def stratg():
   req = request.get_json() #getting text and line from frontend
   global string_selected
   string_selected=req['TEXTSELECTED']
   global whole
   whole=req['WHOLE_STUFF']
   line_num = req['LINENUMBER']
   word_index = req['word_index']
   full_line = req['full_line']
   
   print(full_line[word_index[0]:word_index[1]])

   #introductory to [LR]HS can be found at docs.xrep.in/boundaries
   # CHECKING IF LHS AND RHS HAS CHECKED

   # below global vars keeps output of checkboxes!
   global LINE_NUM
   global is_lhs_enabled
   global is_rhs_enabled
   # above global vars keeps output of checkboxes!

   is_lhs_enabled = req['TheLHSNumStat']
   is_rhs_enabled = req['TheRHSNumStat']

   lhs = is_lhs_enabled
   rhs = is_rhs_enabled
   if lhs==True:
      lhs_1 = "["
      lhs_2 = "]?"
      prd = "."  #for pattern-5
      wild = ".*" #for pattern-5
   else:
      lhs_1 = ""
      lhs_2 = ""
      prd=""  #for pattern-5
      wild="" #for pattern-5

   if rhs==True:
      rhs_1 = "["
      rhs_2 = "]?"
   else:
      rhs_1 = ""
      rhs_2 = ""

   LSTATUS = req['TheLineNumStat']
   if LSTATUS == True:
      LINE_NUM = line_num
   elif LSTATUS == False:
      LINE_NUM = ""

   this_full_text = whole[line_num-1] #gets the entire text in selected line for strcit_mode
   #getting index number of selected word
   start_index=req['start_index']
   end_index=req['end_index']

   if string_selected == '':
      return jsonify("empty string")
   j=len(string_selected)

   len_str = len(string_selected)

   pre_boundary = this_full_text[:start_index]

   post_boundary = this_full_text[end_index:] 

   len_for_pre_boundary = len(this_full_text[:start_index])

   len_for_post_boundary = len(this_full_text[end_index:]) 

   splitted_pre = pre_boundary.split()

   splitted_post = post_boundary.split()

   splitted_pre_len = len(splitted_pre) #len of splitted PRE array

   splitted_post_len = len(splitted_post) #len of splitted POST array

   if len_for_pre_boundary==0 and len_for_post_boundary==0:
      cooked_pre_boundary=""
      cooked_post_boundary=""
      print("zero")

   elif len_for_pre_boundary>6 and len_for_pre_boundary>6:
      cooked_pre_boundary = pre_boundary[:3]
      len_after_pre_boundary = len_for_pre_boundary-4

      cooked_post_boundary = escape_brakt(post_boundary[:3])
      len_after_post_boundary = len_for_post_boundary-4

   elif len_for_pre_boundary<6 and len_for_post_boundary<6:
      cooked_pre_boundary = pre_boundary
      cooked_post_boundary = escape_brakt(post_boundary)

   elif len_for_pre_boundary<6:
      cooked_pre_boundary = pre_boundary
      cooked_post_boundary = escape_brakt(post_boundary[:3])
      len_after_post_boundary = len_for_post_boundary-4

   elif len_for_post_boundary<6:
      cooked_post_boundary = escape_brakt(post_boundary)

      cooked_pre_boundary = pre_boundary[:3]
      len_after_pre_boundary = len_for_pre_boundary-4

   #limiting long selection outputs.. THIS DECIDES OVERALL OUTPUT!
   if len(string_selected) > 50:
      return  {
      "pattern_4_result":"Non-useful pattern!",
      "pattern_3_result":"Non-useful pattern!", 
      "pattern_1_result":"Non-useful pattern!",
      "pattern_5_result":"Non-useful pattern!",
      "pattern_2_result":"Non-useful pattern!"
       }
   

   abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

   ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

   nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

   space = [' ']

   escape = ['.', '[', '{', '(', ')', '\\', '*', '+', '?', '|', '^', '$','/','"',']']

   possible_alnum = ['[a-z]','[a-z]+','[A-Z]','[A-Z]+','[0-9]','[0-9]+',"\\w","\\w+"]

   #global variables for this function#
   global number_of_repeats #used to know whether we have (1(2)) while substituting
   number_of_repeats = 0 
   global cooked_string_copy
   cooked_string_copy=""
   prefetch = "sed -E "+'"'+str(LINE_NUM)+"{}s/(".format(LINE_NUM)
   # not using +str(line_num)+ AS OF NOW!!
   if len_for_pre_boundary!=0:
      prefetch_for_pat5 = f"sed -E -n "+'"'+str(LINE_NUM)+"s/."+lhs_1+"{"+str(len_for_pre_boundary)+"}"+lhs_2+wild+"("+prd
   else:
      prefetch_for_pat5 = f"sed -E -n "+'"'+str(LINE_NUM)+"s/\\s*("

   i=0

   di = [] #used to loop through string and saves here eg: in abc or ABC or nums ..etc

   di_2 = [] #simplified di with + for repetative values

   di_3 = [] #alnum 

   di_4 = [] #2nd stage alnum filtering

   di_5 = [] #3rd stage(in some case, NOt using NOW)

   while (i<len(string_selected)):
      if string_selected[i] in abc:
        di.append("[a-z]") #replaced [a-z] with w
        i+=1
      elif string_selected[i] in ABC:
        di.append("[A-Z]") #replaced [A-Z] with w
        i+=1
      elif string_selected[i] in nums:
        di.append("[0-9]")
        i+=1
      elif string_selected[i] in space:
        di.append("\\s+")
        i+=1
      elif string_selected[i] in escape:
         di.append("\\"+string_selected[i])
         i+=1
      else:
        di.append(string_selected[i])
        i+=1

   #below is implementation of groupby (refer groupby.py)
   for i,k in groupby(di):
      l=list(k)
      if len(l) != 1:
         di_2.append(i+"+")
      else:
         di_2.append(i)


   def spacer_finder(pre_or_post,stuff):  #pre2\s?(target)\s?post
      if pre_or_post=="pre":
         splitted_stuff = stuff.lstrip().split(" ")

         if splitted_stuff[-1] == "":
            space_before = True
         else:
            space_before = False
         return space_before
      
      elif pre_or_post=="post":
         
         splitted_stuff = stuff.rstrip().split(" ")
         if splitted_stuff[0] == "":
            space_after = True
         else:
            space_after = False
         return space_after

   def glolbal_decision_for_pattern3(string):
      if len(string)>4: #checking if string is gt4
         gt4 = True
         shorted_str = string[:3]
         len_after_shorted = str(len(string[3:]))
         return shorted_str+".{"+len_after_shorted+"}"
      elif len(string)==0:
         return "" #if whatever is empty
      else:
         return string

   def glolbal_len_decision(string):
      if len(string)>4: #checking if string is gt4 if yes, take 4chars, rest as .{N}
         gt4 = True
         shorted_str = string[:3]
         len_after_shorted = len(string[3:])
         return {"gt4":gt4,"shorted_str":shorted_str,"len_after_shorted":str(len_after_shorted)}
      else:
         return {"gt4":False,"string":string}

   #fn for alnum (refer alnum.py)
   def alnum_algo(old,new): #old is the list for alnum filter, results to new ,both shoould be list
      for k in zip(old[::2],old[1::2]):
         temp = all(x in possible_alnum for x in k)
         if temp == True:
             new.append("\\w+")
         else:
            for i in k:
               new.append(i)
      if len(old)%2!=0:
         if len(new)>1:
            if old[-1] in possible_alnum and new[-1] == "\\w+":
               new[-1]="\\w+"
            else:
               new.append(old[-1])

   def repeating_stuff(list_to_filter): #to fix repeat (refer rept.py in termux)
      t=[] #stores result of N number repeats [('foo','bar')N]
      temp = []
      global cooked_string_copy
      global number_of_repeats
      for k in zip(list_to_filter[::2],list_to_filter[1::2]):
         t.append(k)
      if len(list_to_filter)%2!=0:
         t.append(list_to_filter[-1]) 
#grouping with numbering
      for i,k in groupby(t):
         l=list(k)
         temp.append((i,len(l)))
      #filtering from temp
      cooked_string=""
      for m in temp:
         t = ''.join(m[0])
         if m[1]>1:
            number_of_repeats+=1
            cooked_string+="("+t+")"+"{"+str(m[1])+"}"
         elif m[1]==1:
            for n in m[0]:
               cooked_string+=n
      cooked_string_copy+=cooked_string
      return cooked_string

   

   def pattern_2():
      ##lhs and rhs is the status of the checkbox, if checked we change it with []? else nothing 
      
      nonlocal di_3
      alnum_algo(di_2,di_3) #1st stage alnum filter
      
      di_3 = [i[0] for i in groupby(di_3)]
      preb = pat_2_ready(pre_boundary.lstrip().split(" "))
      postb = pat_2_ready(post_boundary.lstrip().split(" "))
      if len(di_2) < 4:  #changing value may affect filtering steps
         res = repeating_stuff(di_2)
         # print("kondeee",preb)
         return "sed -E -n '{}s/{}\\s*({})\\s*{}.*/\\1/p'".format(LINE_NUM,lhs_1+preb+lhs_2,res,rhs_1+postb+rhs_2)
      else:
         res = repeating_stuff(di_3)
         return "sed -E -n '{}s/{}\\s*({})\\s*{}.*/\\1/p'".format(LINE_NUM,lhs_1+preb+lhs_2,res,rhs_1+postb+rhs_2)

   def pattern_5(): #mostly have \\w+ than [[:class:]]
      nonlocal di_4
      if len(di_3) > 15:
         alnum_algo(di_3,di_4)

         di_4 = [i[0] for i in groupby(di_4)]

         res = repeating_stuff(di_4)
         final = prefetch_for_pat5+res+').*/\\1/p"'
         return final
      else:
         if len(di_3)!=0:
            res = repeating_stuff(di_3)
            final = prefetch_for_pat5+res+').*/\\1/p"'
            return final
         else:
            return "𝘞𝘰𝘳𝘬𝘴 𝘣𝘦𝘵𝘵𝘦𝘳 𝘸𝘪𝘵𝘩 𝘮𝘰𝘳𝘦 𝘤𝘮𝘱𝘭𝘹 𝘰𝘯𝘦𝘴!"

   def filter_the_escape(filterthis): #filtering escape chars
      some_escapes = ["<",">"]
      res = ""
      for i in filterthis:
         if i in escape:
            res+="\\"+i
         else:
            res+=i
      return res

   #refer algos/patt6_boundaries.py for BELOW

   def cooked_pattern_1(splitted_stuff):
      if len(splitted_stuff)>=2:
         if len(splitted_stuff[0])>4:
            global_res_1 = glolbal_len_decision(splitted_stuff[0])
            bd1 = global_res_1["shorted_str"]+".{"+global_res_1["len_after_shorted"]+"}"
         else:
            bd1 = splitted_stuff[0]

         if len(splitted_stuff[-1])>4:
            global_res_2 = glolbal_len_decision(splitted_stuff[-1])
            bd2 = global_res_2["shorted_str"]+".{"+global_res_2["len_after_shorted"]+"}"
         else:
            bd2 = splitted_stuff[-1]
       
         return [bd1,bd2]
     
      elif len(splitted_stuff)==1:
         if len(splitted_stuff[0])>4:
            global_res_1 = glolbal_len_decision(splitted_stuff[0])
            bd1 = global_res_1["shorted_str"]+".{"+global_res_1["len_after_shorted"]+"}"
            return [bd1]
         else:
            bd1 = splitted_stuff[0]
            return [bd1]

   def escape_from_list(list):
      temp = []
      for i in list:
         temp.append(escape_brakt(i))
      return temp

   def pattern_1():
      patt1_res = pat_1_ready(lhs,rhs,LINE_NUM,splitted_pre,splitted_post,pre_boundary,post_boundary,cooked_string_copy)
      return patt1_res


   def pattern_3(): #using boundaries in pattern_2 for
      #settlement for pre_boundary
      splitting_pre_on_space = pre_boundary.split(" ")
      if len(pre_boundary.split())==0:
         pre_bndry_patt3="\\s*^"
      else:
         splitting_for_global_fn = pre_boundary.split()[-1]
         pre_bndry_patt3 = glolbal_decision_for_pattern3(escape_brakt(splitting_for_global_fn))
      #settlement for pre_boundary
      
      prefetch_complex_subsitit = "sed -E -n "+'"'+str(LINE_NUM)+"s/("
      if len_for_pre_boundary==0 and len_for_post_boundary==0:
         return (f"sed -E '{LINE_NUM}s/(.+)?({cooked_string_copy})$(.*)/XXX/'")
      elif len_for_pre_boundary==0: #preboundary missing
         if number_of_repeats==0:
            return (f"sed -E '{LINE_NUM}s/(.+)?({cooked_string_copy})\\s*?({cooked_post_boundary})\\s*?(.*)/XXX \\3 \\4/'")
         else:
            return (f"sed -E '{LINE_NUM}s/(.+)?({cooked_string_copy})\\s*?({cooked_post_boundary})\\s*?(.*)/XXX \\4 \\5/'")
      elif len_for_post_boundary==0: #postboundry missing
         return (f"sed -E '{LINE_NUM}s/(.+)?({pre_bndry_patt3})\\s*?({cooked_string_copy})$/\\1 \\2 XXX/'")
      else:
         if number_of_repeats ==0:
            return (f"sed -E '{LINE_NUM}s/(.+)?({pre_bndry_patt3})\\s*?({cooked_string_copy})\\s*?({cooked_post_boundary})(.*)/\\1 \\2 XXX \\4 \\5/'")
         else:
            return (f"sed -E '{LINE_NUM}s/(.+)?({pre_bndry_patt3})\\s*?({cooked_string_copy})\\s*?({cooked_post_boundary})(.*)/\\1 \\2 XXX \\5 \\6/'")


      
   def count_this_repeats(list_to_filter): #can be used in di_1 if needed
      t=[] #stores result of N number repeats [('foo','bar')N]
      temp = []
      for k in zip(list_to_filter[::2],list_to_filter[1::2]):
         t.append(k)
      if len(list_to_filter)%2!=0:
         t.append(list_to_filter[-1]) 
#grouping with numbering
      for i,k in groupby(t):
         l=list(k)
         temp.append((i,len(l)))
      #filtering from temp
      fixed_repeats=""
      for m in temp:
         t = ''.join(m[0])
         if m[1]>1:
            fixed_repeats+="("+t+")"+"{"+str(m[1])+"}"
         elif m[1]==1:
            for n in m[0]:
               fixed_repeats+=n
      return fixed_repeats


   def sub_with_specific_numbering(basic_duplicate_list): #make numbers of repats (smtg){N}
      final_cooked_string = ""
      sub_it = "sed -E '{}s/".format(LINE_NUM)
      temp = []
      l = []
      for j,k in groupby(basic_duplicate_list):
         l=list(k)
         temp.append((j,len(l)))
      for i in temp:
         if i[1]>1:
            stuff= str(i[0])
            count = str(i[1])
            final_cooked_string+="("+stuff+")"+"{"+count+"}"
         elif i[1]==1:
            stuff=str(i[0])
            final_cooked_string+=stuff
      return sub_it+final_cooked_string+"/XXX/'"


   def pattern_4(basic_duplicate_list): #make numbers of repats (smtg){N}
      nonlocal cooked_pre_boundary
      escaped_pre_boundary = escape_brakt(cooked_pre_boundary)
      final_cooked_string = ""
      short_cook = ".*"
      sub_it = "sed -E -n '{}s/.*(".format(LINE_NUM)
      temp = []
      l = []

      for j,k in groupby(basic_duplicate_list):
         l=list(k)
         temp.append((j,len(l)))
      for i in temp:
         if i[1]>1:
            stuff= str(i[0])
            count = str(i[1])
            final_cooked_string+="("+stuff+")"+"{"+count+"}"
         elif i[1]==1:
            stuff=str(i[0])
            final_cooked_string+=stuff

      if escaped_pre_boundary=="": 
         closest_pre_boundary=pre_boundary[-1:-4]
         # line_num varibale is not using AS OF NOW!!
         return  "sed -E -n '{}s/.*{}.*({})\\s*{}.*/\\1/p'".format(LINE_NUM,lhs_1+closest_pre_boundary+lhs_2,final_cooked_string,rhs_1+cooked_post_boundary+rhs_2)
      else:
         return  "sed -E -n '{}s/.*{}.*({})\\s*{}.*/\\1/p'".format(LINE_NUM,lhs_1+escaped_pre_boundary+lhs_2,final_cooked_string,rhs_1+cooked_post_boundary+rhs_2)             

   def pattern_6():
      res = pattern_6_beta(lhs,rhs,LINE_NUM,pre_boundary,post_boundary)
      return res
   #some global vars
   global sub_with_spec_nums
   global pattern_4_result
   global pattern_2_result #speicif filter
   global pattern_3_result
   global pattern_1_result
   global pattern_5_result #not_pattern_2
   global patt6_result #NEW CHANGE !! FEB 23-22

   #global var ends
   # pattern_1_v2()
   sub_with_spec_nums = sub_with_specific_numbering(di)
   pattern_4_result = pattern_4(di)
   pattern_2_result = pattern_2()
   patt6_result = pattern_6()
   if len(di_3) > 15:
      pattern_5_result = pattern_5()
      pattern_3_result = pattern_3()
      pattern_1_result = pattern_1()

      final_return = {
      # "sub_with_spec_nums":sub_with_spec_nums,
      "pattern_1_result":pattern_1_result,
      "pattern_4_result":pattern_4_result,
      "pattern_3_result":pattern_3_result, 
      "pattern_5_result":pattern_5_result,
      "pattern_6_result":patt6_result
      }
      return final_return

   else:

      pattern_3_result = pattern_3()
      pattern_1_result = pattern_1()
      pattern_5_result = pattern_5()
      final_return = {
      # "sub_with_spec_nums":sub_with_spec_nums,
      "pattern_1_result":pattern_1_result,
      "pattern_2_result":pattern_2_result,
      "pattern_3_result":pattern_3_result,
      "pattern_4_result":pattern_4_result,
      "pattern_5_result":pattern_5_result,
      "pattern_6_result":patt6_result
      }
      return final_return


@app.route('/bug')
def bug_report():
   global whole
   global string_selected
   global sub_with_spec_nums
   global pattern_4_result
   global pattern_2_result #speicif filter
   global pattern_3_result
   global pattern_1_result
   global pattern_5_result #pattern_5
   global patt6_result
   try:

      collect = {
      "entire_line":whole,
      "selected_text":string_selected,
      "pattern_1_result":pattern_1_result,
      "pattern_2_result":pattern_2_result,
      "pattern_3_result":pattern_3_result,
      "pattern_4_result":pattern_4_result,
      "pattern_5_result":pattern_5_result,
      "pattern_6_result":patt6_result
      }
   except Exception as e:
      print("EXCEPR->",e)
      return {"status":"You have'nt started yet!","notes":"Start by selecting what you need!"}
   if string_selected!="":
      #creating bug_report at gh

      x=uuid.uuid1()
      rand_uuid = x.hex
      pre_beautify = json.dumps(collect, indent=2)
      #creating new report file
      report_status = "Report Sent"
      notes = "Thank you very much for submitting this report, this will help to improve 𝙓𝙍𝙀𝙋 RefID for this report is:  {}".format(rand_uuid)
      repo.create_file(rand_uuid, "NEW REPORT",pre_beautify, branch="main") #file creates
      return { "status":report_status,"notes":notes,"Ref:ID":rand_uuid}
   else:
      report_status = "Report NOT sent"
      notes = "You have not choose anything!"
      print("report NOT sent")
      return { "status":report_status,"notes":notes}



@app.route('/donate')
def donate_xrep():
   return render_template('donate.html')

if __name__ == '__main__':
   app.run(debug=True)

#BEFORE DEPLOY, BEBUG, GIT_REPO UNCOMMENT (LINE-8)
