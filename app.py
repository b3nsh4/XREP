from flask import Flask,render_template,request,jsonify,make_response
from itertools import groupby
import json
import uuid
from github import Github
app = Flask(__name__)
g = Github('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')
repo = g.get_repo("b3nsh4/EXrep_BUG_REPORT")

@app.route('/')
def hello_name():
   return render_template('index.html')

@app.route("/entry", methods=["POST"])
def stratg():
   req = request.get_json() #getting text and line from frontend
   global string
   string=req['TEXTSELECTED']
   global whole
   whole=req['WHOLE_STUFF']
   line_num = req['LINENUMBER']
   this_full_text = whole[line_num-1] #gets the entire text in selected line for strcit_mode

   #getting index number of selected word
   start_index=req['start_index']
   end_index=req['end_index']

   if string == '':
      return jsonify("empty string")
   line_num = req['LINENUMBER']
   j=len(string)
   len_str = len(string)
   
   abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

   ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

   nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

   space = [' ']

   escape = ['.', '[', '{', '(', ')', '\\', '*', '+', '?', '|', '^', '$','/','"']

   possible_alnum = ['[a-z]','[a-z]+','[A-Z]','[A-Z]+','[0-9]','[0-9]+',"\\w","\\w+"]

   #global variables for this function#
   global number_of_repeats #used to know whether we have (1(2)) while substituting
   number_of_repeats = 0 
   global cooked_string_copy
   cooked_string_copy=""
   prefetch = "sed -E "+'"'+str(line_num)+"s/("

   prefetch_for_pat5 = "sed -E -n "+'"'+str(line_num)+"s/.*\\ ("
   i=0

   di = [] #used to loop through string and saves here eg: in abc or ABC or nums ..etc

   di_2 = [] #simplified di with + for repetative values

   di_3 = [] #alnum 

   di_4 = [] #2nd stage alnum filtering

   di_5 = [] #3rd stage(in some case, NOt using NOW)

   while (i<len(string)):
      if string[i] in abc:
        di.append("[a-z]") #replaced [a-z] with w
        i+=1
      elif string[i] in ABC:
        di.append("[A-Z]") #replaced [A-Z] with w
        i+=1
      elif string[i] in nums:
        di.append("[0-9]")
        i+=1
      elif string[i] in space:
        di.append("\\s+")
        i+=1
      elif string[i] in escape:
         di.append("\\"+string[i])
         i+=1
      else:
        di.append(string[i])
        i+=1

   #below is implementation of groupby (refer groupby.py)
   for i,k in groupby(di):
      l=list(k)
      if len(l) != 1:
         di_2.append(i+"+")
      else:
         di_2.append(i)


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
            if old[-1] in possible_alnum and new[-1] == "\\w" or new[-1] == "\\w+":
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

   

   def specific_filtering(): #THIS SHOULD BE SIMPLE SUBSTITUTION
      alnum_algo(di_2,di_3) #1st stage alnum filter
      if len(di_2) < 4:  #changing value may affect filtering steps
         res = repeating_stuff(di_2)
         final = prefetch+res+')/XXX/"'
         return final
      else:
         res = repeating_stuff(di_3)
         final = prefetch+res+')/XXX/"'
         return final

   def not_specific_filtering(): #mostly have \\w+ than [[:class:]]
      if len(di_3) > 15:
         alnum_algo(di_3,di_4)
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


   #some global variables#

   txt_before_target = this_full_text[:start_index].split( )
   txt_after_target = this_full_text[end_index:].split( )

   if len(txt_before_target)!=0: #preboundary check
      pre_boundary = filter_the_escape(txt_before_target[-1])
      cooked_pre_boundary = pre_boundary
   if len(txt_after_target)!=0: #postboundry check
      post_boundary= filter_the_escape(txt_after_target[0])
      cooked_post_boundary = post_boundary
   #below fn is important since target structure may vary
   #BLOCK ewb
   def easy_wrd_boundary(): #a.k.a strict_extract
   # the *? zero or more (greedy) also +? (greedy)

      if len(txt_before_target)==0 and len(txt_after_target)==0:
         return (f"sed -E -n '{line_num}s/\\s*?({cooked_string_copy})$/\\1/p'")
      elif len(txt_before_target)==0: #preboundary missing
         return (f"sed -E -n '{line_num}s/.*({cooked_string_copy})\\s*?{cooked_post_boundary}.*/\\1/p'")
      elif len(txt_after_target)==0: #postboundry missing
         return (f"sed -E -n '{line_num}s/.*{cooked_pre_boundary}\\s*?({cooked_string_copy})$/\\1/p'")
      else:
         pre = (f"sed -E -n '{line_num}s/.*{cooked_pre_boundary}\\s*?({cooked_string_copy})\\s*?{cooked_post_boundary}.*/\\1/p'")
         return pre

   def complex_substitution(): #using boundaries in specific_filtering for
      prefetch_complex_subsitit = "sed -E -n "+'"'+str(line_num)+"s/("
      if len(txt_before_target)==0 and len(txt_after_target)==0:
         return (f"sed -E '{line_num}s/(.+)?({cooked_string_copy})$(.*)/XXX/'")
      elif len(txt_before_target)==0: #preboundary missing
         if number_of_repeats==0:
            return (f"sed -E '{line_num}s/(.+)?({cooked_string_copy})\\s*?({cooked_post_boundary})\\s*?(.*)/XXX \\3 \\4/'")
         else:
            return (f"sed -E '{line_num}s/(.+)?({cooked_string_copy})\\s*?({cooked_post_boundary})\\s*?(.*)/XXX \\4 \\5/'")
      elif len(txt_after_target)==0: #postboundry missing
         return (f"sed -E '{line_num}s/(.+)?({cooked_pre_boundary})\\s*?({cooked_string_copy})$/\\1 \\2 XXX/'")
      else:
         if number_of_repeats ==0:
            return (f"sed -E '{line_num}s/(.+)?({cooked_pre_boundary})\\s*?({cooked_string_copy})\\s*?({cooked_post_boundary})(.*)/\\1 \\2 XXX \\4 \\5/'")
         else:
            return (f"sed -E '{line_num}s/(.+)?({cooked_pre_boundary})\\s*?({cooked_string_copy})\\s*?({cooked_post_boundary})(.*)/\\1 \\2 XXX \\5 \\6/'")


      
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
      sub_it = "sed -E '{}s/".format(line_num)
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


   def extract_with_specific_numbering(basic_duplicate_list): #make numbers of repats (smtg){N}
      final_cooked_string = ""
      sub_it = "sed -E -n '{}s/.+(".format(line_num)
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
      return sub_it+final_cooked_string+").*/\\1/p'"
   #some global vars
   global sub_with_spec_nums
   global extract_with_spec_nums
   global temp_spec #speicif filter
   global strict_sub
   global strict_extract
   global not_specific #not_specific_filtering

   #global var ends
   sub_with_spec_nums = sub_with_specific_numbering(di)
   extract_with_spec_nums = extract_with_specific_numbering(di)
   temp_spec = specific_filtering()
   if len(di_3) > 15:
      not_specific = not_specific_filtering()
      strict_sub = complex_substitution()
      print("\number_of_repeats: ",number_of_repeats)
      strict_extract = easy_wrd_boundary()
      final_return = {
      # "sub_with_spec_nums":sub_with_spec_nums,
      "extract_with_spec_nums":extract_with_spec_nums,
      "strict_sub":strict_sub, 
      "strict_extrct":strict_extract,
      "not_specific_filtering":not_specific
      }
      return final_return

   else:

      strict_sub = complex_substitution()
      print("\n number_of_repeats: ",number_of_repeats)
      strict_extract = easy_wrd_boundary()
      not_specific = not_specific_filtering()
      final_return = {
      # "sub_with_spec_nums":sub_with_spec_nums,
      "extract_with_spec_nums":extract_with_spec_nums,
      "strict_sub":strict_sub,
      "strict_extrct":strict_extract,
      "specific_filtering":temp_spec,
      "not_specific_filtering":not_specific
      }
      return final_return

@app.route('/bug')
def bug_report():
   global whole
   global string
   global sub_with_spec_nums
   global extract_with_spec_nums
   global temp_spec #speicif filter
   global strict_sub
   global strict_extract
   global not_specific #not_specific_filtering
   try:

      collect = {
      "entire_line":whole,
      "selected_text":string,
      "extract_with_spec_nums":extract_with_spec_nums,
      "strict_sub":strict_sub,
      "strict_extrct":strict_extract,
      "specific_filtering":temp_spec,
      "not_specific_filtering":not_specific
      }
   except NameError:
      return {"status":"You have'nt started yet!","notes":"Start by selecting what you need!"}
   if string!="":
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
   # pewerful_wrd_boundary(cooked_string)
   # return not_specific_filtering() #CANNOT be used for simple stuff (1000)  
   #not speicif only works with NON-simple stuff. with 1000 input, it gives nothing
   # print(sub_with_specific_numbering(di))
   # print(extract_with_specific_numbering(di))
   # temp_spec = specific_filtering()
   # if len(di_3) > 15:
   #    print("\nsubstit",complex_substitution())
   #    print("\nextract",easy_wrd_boundary())
   #    print not_specific_filtering()
   # else:
   #    print("\nsubstit",complex_substitution())
   #    print("\nextract",easy_wrd_boundary())
   #    print temp_spec


if __name__ == '__main__':
   app.run(debug=True,host='0.0.0.0')


      ## TODO - 27
      ##TODO: long sub 
      #TODO: long extraction
      #simple substitution
      #below is eg of complex substitution
      #sed -E "11s/(\<permaddr\s*)(\w+:[a-z][[:digit:]]:\w+:[a-z][[:digit:]]:[a-z]+)(:fd)/\1xxx\3/"
      #return cooked string only and add prefetch on diff fns on need
      #




      #FUTURE REFERENCE FOR FINAL RETURNS!
      # print("\ndi3",di_3)
      # if len(di_3) >1:
      #    alnum_algo(di_3,di_4) #2nd stage alnum filter

      #    if len(di_4) >1: #because if len is one, there is no more filtering needed
      #       alnum_algo(di_4,di_5)
      #       return(jsonify(repeating_stuff(di_5)))
      #    else:
      #       return(jsonify(repeating_stuff(di_4)))

      # if len(di_3) ==1: #if di_3 has onely 1, [[:alnum:]] for eg: we no need di_4
      #    sample = ""
      #    for i in di_3:
      #       sample+=i
      #    return(jsonify(repeating_stuff(sample)))  #most general case - only one eg: [[:alnum:]]+
      # return(jsonify(repeating_stuff(di_5)))


      #other notes
      #its better to always use \s* (zero or more) while playing with \s
      #change len(di_3) and return may affect the output
      #print(len(di2 or di3) then decide how to proceed)




   #rexg THE STARTER

   # #cool trick which replaces prev index if duplicate with +

   # for i in di.values():
   #     if(y!=i):
   #         y=i
   #         x.append(y)
   #     elif (y==i):
   #         x[-1]=i+"+"
   # #FIX FOR ALNUM 1
   # while (z<len(x)):
   #   if (x[z] in possible) and (z+1<len(x)) and (x[z+1] in possible):
   #     new_list.append("\\w+") #replaces alnum with w
   #     z+=1
   #   else:
   #     new_list.append(x[z])
   #   z+=1

   # #FIX FOR ALNUM 2
   # v=0
   # escape_catch = 0
   # while (v<len(new_list)):
   #   if (new_list[v] in possible) and (v+1<len(new_list)) and (new_list[v+1] in possible):
   #     new_list_2.append("\\w+") #replaces alnum with w
   #     v+=1

   #   else:
   #    new_list_2.append(new_list[v])
   #   v+=1

   # #fix3 for previous while loop stops without going to last index; so, add another cond
   # try:
   #    if new_list_2[-1] and new_list_2[-2] in possible:
   #       del new_list_2[-2:]
   #       new_list_2.append("\\w+") #replaces alnum with w
   # except IndexError:
   #    print("fk")
   # #char escapes with \
   # v=0
   # for escaper in new_list_2:
   #    try:
   #       if escaper in escape:
   #          del(new_list_2[v])
   #          new_list_2.insert(v,"\\"+escaper)
   #       v+=1
   #    except IndexError:
   #       print("escaperloop missin")
   #       continue
   # #print("\n",new_list_2)

   # #from 01-01-2021


   # trace_1=0
   # new=[]
   # while trace_1<len(new_list_2):
   #   new.append(new_list_2[trace_1:trace_1+2])
   #   trace_1+=2
   # optimized_arra_1=[]
   # trace_2=0
   # k=None
   # #print(new)
   # trace_4=0
   # trace_3=0
   # prev=None
   # optimized_arra_2=[]
   # while(trace_2<len(new)):
   #    if (k!=new[trace_2]):
   #       k=new[trace_2]
   #       optimized_arra_1.append(new[trace_2])
   #       print("d1",optimized_arra_1)
   #       trace_3=0
   #    else:
   #       trace_3+=1
   #       optimized_arra_1.insert(trace_4,trace_3)
   #       print("d2",optimized_arra_1)
   #    trace_4+=1
   #    trace_2+=1

   # #optimization part-2 where optimized_arra_1 1,2 is added into 3
   # wait=[]
   # trace_5=0
   # #ISSUE ON THIS LOOP //TODO
   # print("flag",optimized_arra_1)
   # while(trace_5<len(optimized_arra_1)):
   #    if (isinstance(optimized_arra_1[trace_5],int) and isinstance(optimized_arra_1[trace_5+1],int)):
   #       print("tr 5 5+1",optimized_arra_1[trace_5],optimized_arra_1[trace_5+1])
   #       pre_1_test_lis=(optimized_arra_1[trace_5]+optimized_arra_1[trace_5+1])
   #       wait.append(optimized_arra_1[trace_5])
   #       wait.append(optimized_arra_1[trace_5+1])
   #       pre_1_test_lis_str=str(wait[-1]+1)
   #       #ABOVE line is adding 1 more to {} because, it works now! (lil hack!)
   #       optimized_arra_2.append("{"+pre_1_test_lis_str+"}")


   #       #algorithm for (paraths) (bla){n}
   #       #1 take x = optimized_arra_2[trace_5-1]
   #       #2 create empty str 
   #       #3 for loop on x and append to empty str
   #       #4 use str concat to add paraths
   #       #5 del(optimized_arra_2[trace_5-1])
   #       #6 insert(trace_5-1,final_string)

   #       paranths_do_str = ""
   #       for i in optimized_arra_2[trace_5-1]:
   #          paranths_do_str=paranths_do_str+i
   #       paranths_do_str="("+paranths_do_str+")"
   #       del(optimized_arra_2[trace_5-1])
   #       optimized_arra_2.insert(trace_5-1,paranths_do_str)

         

   #       trace_5+=2
   #    elif (optimized_arra_1[trace_5]) ==1:
   #       optimized_arra_2.append("{"+str(1)+"}")
   #       paranths_do_str = ""
   #       for i in optimized_arra_2[trace_5-1]:
   #          paranths_do_str=paranths_do_str+i
   #       paranths_do_str="("+paranths_do_str+")"
   #       del(optimized_arra_2[trace_5-1])
   #       optimized_arra_2.insert(trace_5-1,paranths_do_str)
   #       trace_5+=1

   #    else:
   #       optimized_arra_2.append(optimized_arra_1[trace_5])
   #       trace_5+=1
   # print("\n",optimized_arra_2)
   # #making it a nice readable string
   # optimized_string=""
   # for i in range(len(optimized_arra_2)):
   #    for j in range(len(optimized_arra_2[i])):
   #       optimized_string = optimized_string+optimized_arra_2[i][j]

   # print(optimized_string)
   # return jsonify(prefetch+optimized_string+")/XXX/'")