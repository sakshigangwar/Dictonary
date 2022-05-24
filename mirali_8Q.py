name=int(input("enter the element::"))
dict={}
for i in range(name):
    keys=input("enter the keys")
    value=input("enter the value")
    dict.update({keys:value})
print(dict)
