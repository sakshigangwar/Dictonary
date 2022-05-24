# dict={"m":1,"I":1,"S":1,"S":2,"I":2,"S":3,"S":4,"I":2,"P":1,"P":2,"I":3}
# dict="w3resource"
# d={}
# for i in dict:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)

# nested dic

size=int(input("enter the size"))
i=0
d={}
di={}
while i<size:
    key=(input("enter the key"))
    value=(input("enter the value"))
    d.update({key:value})
    i=i+1
d.update(di)
print(d)