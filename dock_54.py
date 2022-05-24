from itertools import count


dict={1: ['anjali singh'], 2: ['vashali singh'], 3: ['nirdosh gangwar'], 4: ['neraj gangwar'], 5: ['payal sharma']}
l=[]
for i in dict:
    l.append(dict[i])
b=[]
for i in range(len(l)):
    for j in range(len(l[i])):
        b.append(l[i][j])

d={}
count=0
for x in range(len(b)):
    count+=1
    for j in range(len(b[x])):
        d.update({count:b[x]})
print([d])