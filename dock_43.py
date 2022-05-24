# a=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# dict={}
# for x,y in a:
#     dict.setdefault(x,[]).append(y)
# print(dict)


a=[2,3,4,1]
b={}
for i in a:
    b.update({a:i})
print(b)