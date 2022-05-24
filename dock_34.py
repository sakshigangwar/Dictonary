dict=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
a={}
sum=0
for i in dict:
        sum=sum+dict[i]
        a.update(dict)
print(a)

