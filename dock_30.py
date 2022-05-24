a={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
d={}
for i in a:
    for x in i:
        k=i.replace(' ','',)
        for i,x in a.items():
            d.update({k:x})
print(d)




# c=a["s 001"]="s001"
# b=a["s 002"]="s002"
# d.append(c)
# d.append(b)
# print(d)

































