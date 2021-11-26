from flask import Flask,render_template,request,jsonify,make_response
from itertools import groupby
app = Flask(__name__)

@app.route('/')
def hello_name():
   return render_template('index.html')

@app.route("/entry", methods=["POST"])
def stratg():
   req = request.get_json() #getting text and line from frontend
   string=req['TEXTSELECTED']
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

   possible_alnum = ['[a-z]','[a-z]+','[A-Z]','[A-Z]+','[[:digit:]]','[[:digit:]]+',"\\w","\\w+"]

   #global variables for this function#
   
   prefetch = "sed -E "+'"'+str(line_num)+"s/("
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
        di.append("[[:digit:]]")
        i+=1
      elif string[i] in space:
        di.append("\\s")
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
         print("\nnew",new)
         if len(new)>1:
            if old[-1] in possible_alnum and new[-1] == "\\w" or new[-1] == "\\w+":
               new[-1]="\\w+"
            else:
               new.append(old[-1])
            

   def repeating_stuff(list_to_filter): #to fix repeat (refer rept.py in termux)
      t=[] #stores result of N number repeats [('foo','bar')N]
      temp = []
      # print("\nlist_to_filter",list_to_filter)
      # for k in zip(list_to_filter[::2],list_to_filter[1::2]):
      #    d[k] = d.get(k,0)+1
      # print("\ndbefore",d)
      # z = [f'({"".join(k)}){ {v} }' if v > 1 else f'{"".join(k)}' for k,v in d.items()]
      # print("\nz",z)
      for k in zip(list_to_filter[::2],list_to_filter[1::2]):
         t.append(k)
      if len(list_to_filter)%2!=0:
         t.append(list_to_filter[-1]) 
      print("\nt",t)
#grouping with numbering
      for i,k in groupby(t):
         l=list(k)
         temp.append((i,len(l)))
      #filtering from temp
      print("\ntemp",temp)
      cooked_string=""
      for m in temp:
         t = ''.join(m[0])
         if m[1]>1:
            cooked_string+="("+t+")"+"{"+str(m[1])+"}"
         elif m[1]==1:
            for n in m[0]:
               cooked_string+=n
      #print("\ncooked_string",cooked_string)

      #fixing the odd bug
      # if len(list_to_filter)%2!=0:
      #    print("list_to_filter-1",list_to_filter[-1])
      #    z.append(list_to_filter[-1])
      #this is to remove ('foo','bar')N and make it to ['(foobar){N}']
      # final_res=""  #string for 
      # for b in z:
      #    final_res+=b
      return (prefetch+cooked_string+')/XXX/"') #RETURNS TUPLE ALSO NEED FIXES WITH (somehting){}

   

   def specific_filtering():
      alnum_algo(di_2,di_3) #1st stage alnum filter
      if len(di_2) < 4:  #changing value may affect filtering steps
         return (jsonify(repeating_stuff(di_2)))
      else:
         return(jsonify(repeating_stuff(di_3)))

   def not_specific_filtering(): #mostly have \\w+ than [[:class:]]
      alnum_algo(di_2,di_3) #1st stage alnum filter
      if len(di_3) > 4:
         alnum_algo(di_3,di_4)
         return (jsonify(repeating_stuff(di_4)))
      else:
         return (jsonify(repeating_stuff(di_3)))

   #below fn is important since target structure may vary
   #BLOCK ewb
   def easy_wrd_boundary(): #used to find without line numbers <wrd bndry>([^ ]<wrd bndry>)
      try:
         txt_before_target = this_full_text[:start_index].split( )
         txt_after_target = this_full_text[end_index:].split( )
         pre_boundary = txt_before_target[-1]
         post_boundary= txt_after_target[0]
      except IndexError:
         print("Couldn't run BLOCK-#ewb, index error")
         console.log("Couldn't run BLOCK-#ewb")
      # TODO: pre_boundary or post_bndry need escape eg: link\/ether
      pre = (f"sed -E -n '{line_num}s/.*\\<{pre_boundary}?([^ ]+)?{post_boundary}.*/\\1/p'")
      return pre

   #def very_specific():
   # print("indexed",this_full_text[start_index:end_index])
   # print("d2",di_2)
   # print("d3",di_3)
   print(easy_wrd_boundary())
   # pewerful_wrd_boundary(cooked_string)
   # return not_specific_filtering() #CANNOT be used for simple stuff (1000)  
   #not speicif only works with NON-simple stuff. with 1000 input, it gives nothing
   return specific_filtering()





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


if __name__ == '__main__':
   app.run(debug=True)








