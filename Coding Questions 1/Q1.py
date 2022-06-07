marks = {"Tom":[75,63,72],"Dick":[41,52,36],"Harry":[60,51,30]}

avg = {}
for key,values in marks.items():
    avg[key] = sum(values)/len(values)

print(avg)
