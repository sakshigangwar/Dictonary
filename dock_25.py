num=int(input("enter the number"))
dict={}
for i in range(num):
    a=input("enter str")
    for i in a:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
print(dict)
