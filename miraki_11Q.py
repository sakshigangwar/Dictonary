
# from typing import Counter


dict={'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
# k=[]
# k=Counter(dict)
# high=k.most_common(3)
# for i in high:
#     print(i[1])

# max=0
# max1=0
# max2=0
# for i in dict:
#     for j in dict:
#         if dict[j]>max:
#             max=dict[j]
#         if dict[j]>max1 and dict[j]!=max:
#             max1=dict[j]
#         if dict[j]>max2 and dict[j]!=max and dict[j]!=max1:
#             max2=dict[j]
# print(max,max1,max2)

l=[]
for i in dict:
    l.append(dict[i])
max=0
min=l[0]
i=0
while i<len(l):
    if l[i]>max:
        max=l[i]
    if l[i]<min:
        min=l[i]
    i=i+1
print(max,min)