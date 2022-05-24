a1={1:2,2:3,3:4,4:5}
a2={5:6,3:4,9:6,8:3}
for i in a2:
    if i in a1:
        a1[i]=+a2[i]
    else:
        a1[i]=a2[i]
print(a1)

