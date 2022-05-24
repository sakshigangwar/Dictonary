dock=[{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
b=[]
for i in dock:
    for j in i.values():
        if j not in b:
            b.append(j)
print(b)



a={"a 001":"english","b 002":"hindi"}
b=a["a 001"]="a001"
print(b)
