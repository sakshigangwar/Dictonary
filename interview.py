# a={"a":"my","b":"name","c":"is","d":"sakshi"}
# for i in a:
#     print(a[i],end=" ")


# a={"sum":{1:3,4:6,5:7,7:10}}
# key=int(input("enter the key:"))
# value=int(input("ente the value:"))
# for i,j in a.items():
#     for k in j:
#         if k==key:
#             j[k]+=value

# print(a)


# i=1
# k=1
# while i<=4:
#     s=1
#     while s<=4-i:
#         print(" ",end=" ")
#         s=s+1
#     j=1
#     while j<=k:
#         print("*",end=" ")
#         j=j+1
#     k=k+2
#     print()
#     i=i+1





# num=int(input("enter the number::"))
# a={}
# i=0
# while i<num:
#     key=input("enter the key:")
#     value=input("enter the value:") 
#     a.update({key:value})
#     i=i+1
# print(a)



# a={"num":2,"sun":4,"mum":6,"dum":8}
# sum=0
# for i in a:
#     sum=sum+a[i]
# print(sum)

# a={"num":2,"sun":4,"mum":6,"dum":8}
# for i,j in a.items():
#         print(i,":",j)

# a={"num":2,"sun":4,"mum":6,"dum":8}
# count=0
# print("k  v  c")
# for i in a:
#     count=count+1
#     print(i, a[i], count)

# user=int(input("Enter the max size: "))
# i=0
# b={}
# while i<user:
#     name=input("Enter name: ")
#     surname=input("Enter the surname: ")
#     age=int(input("Enter the age: "))
#     b.update({"name":name,"surname":surname,"age":age})
#     i+=1
# print([b])



d = {}
size = int(input("Enter the size of nested dictionary: "))
for i in range(size):
    dict_name = input("Enter the name of child dictionary: ")
    d[dict_name] = {}
    Name = input("Enter name: ")
    Age = input("Enter Age: ")
    d[dict_name]["Name"] = Name
    d[dict_name]["Age"] = Age
print(d)

 