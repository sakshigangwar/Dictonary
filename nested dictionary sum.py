# d={"a":{"b":40},"c":50,"d":30,"f":4,"e":10}
# sum=0
# for i in d:
#     if type(d[i])==dict:
#         for j in d[i]:
#             sum=sum+d[i][j]
#     else:
#         sum=sum+d[i]
# print(sum)

# dic=[{"name":"sakshi","age":17},{"name":"anjali","age":18},{"name":"vashali","age":19},{"name":"rani","age":20}]
# a=[]
# for i in range(len(dic)):
#     for x,y in dic[i].items():
#         if x=="age":
#             a.append(y)
# print(a)


# a=str(input("enter the name"))
# d={}
# for i in range(len(a)):
#     d.update({a[i]:i})
# print(d)






# prime number key and not prime number Value dict m print karo
# num=int(input("enter the number"))
# i=1
# b=[]
# b1=[]
# # c={}
# while i<=num:
#     j=1
#     c=0
#     while j<=i:
#         if i%j==0:
#             c=c+1
#         j=j+1
#     if c==2:
#         b.append(i)
#     else:
#         b1.append(i)
#     i=i+1
# print(b)
# c={}
# l=0
# while l<len(b):
#     c.update({b[l]:b1[l]})
#     l+=1
# print(c) 
# # print(c) 

# for loop



num=int(input("enter the number::"))
i=0
a=[]
while i<=num:
    a.append(i)
    i=i+1
print(a)
i=0
b={}
while i<len(a):
        if a[i]==0:
            b.update({i:"true"})
        else:
            b.update({i:"false"})
        i=i+1
print(b)



# list question
# num=int(input("enter the number"))
# i=1
# while i<num:
#     j=0
#     c=0
#     while j<=i:
#         if i%2==0:
#             c=c+1
#         j=j+1
#     if c==2:
#         print(i,"prime")
#     else:
#         print(i,"not prime")
#     i=i+1

# without sum k sum
# dict={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36,}
# count=0
# for i in dict:
#     count=count+dict[i]
#     print(count)


# without value function
# dict={"s":9,"a":5,"d":7}
# for i in dict:
#     print(dict[i])

# without key function k key print
# dict={"a":6,"s":8,"t":5}
# l=[]
# for i in dict:
#     l.append(i)
# print(l)


# # value phle print ho key bad m
# data={"name":"sakshi","age":20,"brand":"ford"}
# a=[]
# for i in data:
#     a.append(i)
# b=[]
# for i in data.values():
#     b.append(i)
# d={}
# i=0
# while i<len(a):
#     c={b[i]:a[i]}
#     d.update(c)
#     i=i+1
# print(d)




# 3 list se nested dictionary create karna
# id=[1,2,3,4]
# n=["a","b","c","d"]
# a=[12,6,8,9]
# d={}
# for i in range(len(id)):
#     d1={}
#     for j in range(len(n)):
#         if i==j:

#             d1.update({n[j]:a[j]})
#     d.update({id[i]:d1})
# print(d)


# keys=["name","age","job"]
# values=["john","25","developer"]
# dict=dict(zip(keys,values))
# print(dict)