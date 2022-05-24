# from typing import Counter
dict = {'a':50, 'b':58,'c': 56,'d':40,'e':100, 'f':20}
# k=[]
# k=Counter(dict)
# high=k.most_common(3)
# for i in high:
#     print(i[0])
max=0
max1=0
max2=0
d=[]
for i in dict:
    for j in dict:
        if dict[j]>max:
            max=dict[j]
            a=j
        if dict[j]>max1 and dict[j]!=max:
            max1=dict[j]
            b=j
        if dict[j]>max2 and dict[j]!=max and dict[j]!=max1:
            max2=dict[j]
            c=j
d.append(a)
d.append(b)
d.append(c)
print(d)

