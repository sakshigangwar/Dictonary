a=["one","two","three","four","five"]
b=[1,2,3,4,5]
d={}
i=0
while i<len(a):
    d.update({a[i]:b[i]})
    i=i+1
print(d)

