# ---desinding--
dict={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
a=[]
for i in dict:
    a.append(dict[i])
i=0
while i<len(dict):
    j=0
    while j<len(a):
        if a[i]>a[j]:
            c=a[i]
            a[i]=a[j]
            a[j]=c
        j+=1
    i+=1
# print(l)
dict1={}
for k in range(len(a)):
    for i,j in dict.items():
        if j==a[k]:
            dict1.update({i:a[k]})
print(dict1) 


# ---asinding---
dict={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
a=[]
for i in dict:
    a.append(dict[i])
i=0
while i<len(dict):
    j=0
    while j<len(a):
        if a[i]<a[j]:
            c=a[i]
            a[i]=a[j]
            a[j]=c
        j+=1
    i+=1
dict2=[]
for k in range(len(a)):
    for i,j in dict.items():
        if j==a[k]:
            dict2.append((i,a[k]))
print(dict2) 



