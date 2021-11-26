target =  ['[[:digit:]]+', '.', '[[:digit:]]', '.', '[[:digit:]]', '.', '[[:digit:]]', '/', '[[:digit:]]']

escape = ['.', '[', '{', '(', ')', '\\', '*', '+', '?', '|', '^', '$','/']
print(target)
k=0
for i in target:
    if i in escape:
        print("before insert",i)
        print("tar bfr dlt",target)
        del(target[k])
        print("tar aftr dlt",target)
        target.insert(k,"\\"+i)
        print("after insert",target[k])
        print("tar aftr insert",target)
    k+=1
    print(k)
print(target)
