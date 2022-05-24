# a =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# i=0
# count=1
# while i<len(a):
#     j=0
#     while j<len(a):
#         count=count+1
#         j=j+1
#     i=i+1
# print(count)


a =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
count=0
for i in a:
    j=0
    while j<len(a[i]):
        count+=1
        j+=1
print(count)


