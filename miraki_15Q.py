# a = {(1,2):1,(2,3):2}
# print(a[1,2])
# o/p=1

# a = {'a':1,'b':2,'c':3}
# print(a['a','b'])
# o/p=keyerror


# fruit = {}

# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
#         addone('Apple')
#         addone('Banana')
#         addone('apple')
#         addone('Apple')
# print(len(fruit))
# print(fruit)

# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age

# print(Student["name"]) 
# o/p=1

# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12

# sum = 0
# for k in my_dict:
#     sum += my_dict[k]

# print(sum)
# print(my_dict)
# o/p=30

# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates[box]))
# o/p=typeerror


# rec = {
# "Name" : "Python", 
# "Age":"20",
# "Addr" : "NJ", 
# "Country" :"USA"
# }
# id1 = id(rec)
# del rec

# rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
# id2 = id(rec)
# print(id1 == id2)
# o/p=true

# details={"name":"Shanti","age":12,"email":"shanti@navgurukul.org",}

# print(details["name"])
# print(details["lastname"])
# print(details[age])
# o/p=typeerror

# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1.values():
#     sum=sum+1
# print(sum)
# o/p=4


# dict={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:11,12:12,13:13,14:14,15:15}
# cdict={}
# for i in range(1,16):
#     c=i*i
#     print(c)


s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
a={'python':20,"gaurav":300,'dev':34,"karan":43}
c={}
for i in (s,a):
    c.update(i)
print(c)


