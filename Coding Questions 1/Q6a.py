def octal(n): 
    res = ''
    s = bin(n)
    s = s[2:]
    if len(s)<9:
        x = [0 for x in range(9-len(s))]
        x = map(str,x)
        s = (''.join(x)) + s
        
    for x in range(0,len(s),3):
        res += str(int(s[x:x+3],2))
    return res

print(octal(150))   
