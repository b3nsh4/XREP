from flask import Flask,render_template,request,jsonify,make_response
app = Flask(__name__)

@app.route('/')
def hello_name():
   return render_template('index.html')


@app.route("/entry", methods=["POST"])
def stratg():
	req = request.get_json()
	i=0
	string=req['TEXTSELECTED']
	if string == '':
		return jsonify("empty string")
	line_num = req['LINENUMBER']
	prefetch = "sed -E '"+str(line_num)+"s/("
	j=len(string)
	len_str = len(string)
	di={} 

	abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', ' p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

	nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

	space = [' ']

	escape = ['.', '[', '{', '(', ')', '\\', '*', '+', '?', '|', '^', '$','/']

	while (i<len(string)):
	    if string[i] in abc:
	        di[i]="\\w" #replaced [a-z] with w
	        i+=1
	    elif string[i] in ABC:
	        di[i]="\\w" #replaced [A-Z] with w
	        i+=1
	    elif string[i] in nums:
	        di[i]="[[:digit:]]"
	        i+=1
	    elif string[i] in space:
	        di[i]="\\s"
	        i+=1
	    else:
	        di[i]=string[i]
	        i+=1
	y=None
	x=[]

	#cool trick which replaces prev index if duplicate with +

	for i in di.values():
	    if(y!=i):
	        y=i
	        x.append(y)
	    elif (y==i):
	        x[-1]=i+"+"

	# possible = ['[[:alnum:]]+','[[:alnum:]]','[a-z]','[0-9]','[0-9]+','[a-z]+','[A-Z]','[A-Z]+']
	possible = ['\\w+','\\w','\\w','[[:digit:]]','[[:digit:]]+','\\w+','\\w','\\w+']
	z=0
	new_list =[]
	new_list_2 = []
	#FIX FOR ALNUM 1
	while (z<len(x)):
	  if (x[z] in possible) and (z+1<len(x)) and (x[z+1] in possible):
	    new_list.append("\\w+") #replaces alnum with w
	    z+=1
	  else:
	    new_list.append(x[z])
	  z+=1

	#FIX FOR ALNUM 2
	v=0
	escape_catch = 0
	while (v<len(new_list)):
	  if (new_list[v] in possible) and (v+1<len(new_list)) and (new_list[v+1] in possible):
	    new_list_2.append("\\w+") #replaces alnum with w
	    v+=1

	  else:
	  	new_list_2.append(new_list[v])
	  v+=1

	#fix3 for previous while loop stops without going to last index; so, add another cond
	try:
		if new_list_2[-1] and new_list_2[-2] in possible:
			del new_list_2[-2:]
			new_list_2.append("\\w+") #replaces alnum with w
	except IndexError:
		print("fk")
	#char escapes with \
	v=0
	for escaper in new_list_2:
		try:
			if escaper in escape:
				del(new_list_2[v])
				new_list_2.insert(v,"\\"+escaper)
			v+=1
		except IndexError:
			print("escaperloop missin")
			continue
	#print("\n",new_list_2)

	#from 01-01-2021


	trace_1=0
	new=[]
	while trace_1<len(new_list_2):
	  new.append(new_list_2[trace_1:trace_1+2])
	  trace_1+=2
	optimized_arra_1=[]
	trace_2=0
	k=None
	#print(new)
	trace_4=0
	trace_3=0
	prev=None
	optimized_arra_2=[]
	while(trace_2<len(new)):
		if (k!=new[trace_2]):
			k=new[trace_2]
			optimized_arra_1.append(new[trace_2])
			print("d1",optimized_arra_1)
			trace_3=0
		else:
			trace_3+=1
			optimized_arra_1.insert(trace_4,trace_3)
			print("d2",optimized_arra_1)
		trace_4+=1
		trace_2+=1

	#optimization part-2 where optimized_arra_1 1,2 is added into 3
	wait=[]
	trace_5=0
	#ISSUE ON THIS LOOP //TODO
	print("flag",optimized_arra_1)
	while(trace_5<len(optimized_arra_1)):
		if (isinstance(optimized_arra_1[trace_5],int) and isinstance(optimized_arra_1[trace_5+1],int)):
			print("tr 5 5+1",optimized_arra_1[trace_5],optimized_arra_1[trace_5+1])
			pre_1_test_lis=(optimized_arra_1[trace_5]+optimized_arra_1[trace_5+1])
			wait.append(optimized_arra_1[trace_5])
			wait.append(optimized_arra_1[trace_5+1])
			pre_1_test_lis_str=str(wait[-1]+1)
			#ABOVE line is adding 1 more to {} because, it works now! (lil hack!)
			optimized_arra_2.append("{"+pre_1_test_lis_str+"}")


			#algorithm for (paraths) (bla){n}
			#1 take x = optimized_arra_2[trace_5-1]
			#2 create empty str 
			#3 for loop on x and append to empty str
			#4 use str concat to add paraths
			#5 del(optimized_arra_2[trace_5-1])
			#6 insert(trace_5-1,final_string)

			paranths_do_str = ""
			for i in optimized_arra_2[trace_5-1]:
				paranths_do_str=paranths_do_str+i
			paranths_do_str="("+paranths_do_str+")"
			del(optimized_arra_2[trace_5-1])
			optimized_arra_2.insert(trace_5-1,paranths_do_str)

			

			trace_5+=2
		elif (optimized_arra_1[trace_5]) ==1:
			optimized_arra_2.append("{"+str(1)+"}")
			paranths_do_str = ""
			for i in optimized_arra_2[trace_5-1]:
				paranths_do_str=paranths_do_str+i
			paranths_do_str="("+paranths_do_str+")"
			del(optimized_arra_2[trace_5-1])
			optimized_arra_2.insert(trace_5-1,paranths_do_str)
			trace_5+=1

		else:
			optimized_arra_2.append(optimized_arra_1[trace_5])
			trace_5+=1
	print("\n",optimized_arra_2)
	#making it a nice readable string
	optimized_string=""
	for i in range(len(optimized_arra_2)):
		for j in range(len(optimized_arra_2[i])):
			optimized_string = optimized_string+optimized_arra_2[i][j]

	print(optimized_string)
	return jsonify(prefetch+optimized_string+")/XXX/'")

	#print("waited",wait)
	print(string)

if __name__ == '__main__':
   app.run(debug=True)