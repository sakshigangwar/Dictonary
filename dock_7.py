dic1={1:10, 2:20}
dic2={3:30, 4:40}
# dic3={5:50, 6:60}
# b={}
# i=0
# while i<len(dic1):
#     b.update(dic1)
#     b.update(dic2)
#     b.update(dic3)
#     i=i+1
# print(b)
a={1:10, 2:20}
b={3:30, 4:40}
c={}
for i in a,b:
    c.update(i)
print(c)
