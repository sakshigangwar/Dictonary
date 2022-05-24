from re import L


dict={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
a={}
for i in dict:
    k=len(dict[i])
    a.update({dict[i]:k})
print(a)


# i=0
# while i<len(dict):
#     j=0
#     while j<len(dict):
#         count=count+1
#         j=j+1
#     i=i+1
# print(count)








# # a=["sakshi"]
# count=0
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         count=count+1
#         j=j+1
#     i=i+1
# print(count)
    