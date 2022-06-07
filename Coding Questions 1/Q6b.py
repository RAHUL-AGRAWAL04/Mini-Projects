
def binary(n):
    s = ''
    n = list(str(n))
    n = map(int,n)
    for x in n:
        if x == 0:s+='000'
        elif x == 1:s+='001'
        elif x == 2:s+='010'
        elif x == 3:s+='011'
        elif x == 4:s+='100'
        elif x == 5:s+='101'
        elif x == 6:s+='110'
        elif x == 7:s+='111'
        
    return s
print(binary(250))

