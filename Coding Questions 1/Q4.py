def func2(x,y):
    if x == 1:
        return x
    return (y + x + func2(x-1,0)) #y = 0 is passed as value of y is adding only one time

print(func2(5,10))
