dict={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
a={}
for i,y in dict.items():
    b=[]
    for j in y:
        if j%2==0:
            b.append(j)
            a.update({i:b})
print(a)

