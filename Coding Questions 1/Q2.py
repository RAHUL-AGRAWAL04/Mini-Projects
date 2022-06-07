def rfunc1(n):
    if n == 1:
        return n
    else:
        return (n-1)*rfunc1(n-1)

print(rfunc1(6)) #120
