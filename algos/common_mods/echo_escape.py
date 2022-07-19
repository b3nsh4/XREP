def echo_escaper(string):
    res=""
    for i in string:
        if i == '"':
            i = '\\'+i
        res+=i
    return res

