# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)

# city_population = {
#   "NewYorkCity":8550405,
#   "LosAngeles":3971883, 
#   "Toronto":2731571, 
#   "Chicago":2720546, 
#   "Houston":2296224, 
#   "Montreal":1704694, 
#   "Calgary":1239220, 
#   "Vancouver":631486, 
#   "Boston":667137
# }
# print(city_population["NewYorkCity"])
# print(city_population)
# print(type(city_population))

# Dict = {
#   'ball' : 'green',
#   'Ball': 'red'
# }
# print(Dict['ball'])
# print(Dict['Ball'])
# print(Dict['bat'])

# dict={
#   "brand":"ford",
#   "model":"mustang",
#   "year":1964
# }
# print(dict["brand"])



# update Value

# dict={
#   "brand":"ford",
#   "model":"mustang",
#   "year":1964,
#   "year":2020
# }
# print(dict["year"])

# any type data

# dict={
#   "brand":"ford",
#   "electric":"false",
#   "year":1964,
#   "color":["red","white","blue"]
# }
# print(dict["color"])

# type of dict

# dict={
#   "brand":"ford",
#   "model":"mustang",
#   "year":1964
# }
# print(type(dict))

# get type print

## thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"]
# print(x)
# x = thisdict.get("model")
# print(x)

# key type()

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.keys()
# # print(x) 

# car["color"] = "white"
# print(x)

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary") 

# Get Items
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.items()
# print(x) #before the change
# x=car["year"] = 2020
# print(x) #after the change 


# remove item
# dict={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1964
# }
# dict.pop("model")
# print(dict)


# Change Values

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2018
# print(thisdict)

# Update Dictionary

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020}) 
# print(thisdict)

# Adding Items

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)

# Removing Items

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict) 

# last item delete

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict) 

# bich ka item delete karna

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict) 

# clear 
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict) 

# Copy a Dictionary

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)

# dict  function()

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisdict)
# print(mydict) 

# Nested Dictionaries

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# } 
# print(myfamily)

# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# } 
# print(myfamily)


# # interview qustion
#     # pop()
# dict={"name":"sakshi","college":"Navgurukul","class":12,"year":2022}
# dict.pop("class")
# print(dict)

# # clear ()
# dict={"name":"sakshi","college":"Navgurukul","class":12,"year":2022}
# dict.clear()
# print(dict)

# # get ()
# dict={"name":"sakshi","college":"Navgurukul","class":12,"year":2022}
# x=dict.get("name")
# print(x)

# # keys()
# dict={"name":"sakshi","college":"Navgurukul","class":12,"year":2022}
# x=dict.keys()
# print(x)

# # items()
# dict={"name":"sakshi","college":"Navgurukul","class":12,"year":2022}
# x=dict.items()
# print(x)


# # copy()
# dict={"name":"sakshi","college":"Navgurukul","class":12,"year":2022}
# x=dict.copy()
# print(x)

# # popitem()
# dict={"name":"sakshi","college":"Navgurukul","class":12,"year":2022}
# dict.popitem()
# print(dict)





# # Value()
# dict={"name":"sakshi","college":"Navgurukul","class":12,"year":2022}
# x=dict.values()
# print(x)




# # add newitem
# dict={"name":"sakshi","college":"Navgurukul","class":12,"year":2022}
# dict["sum"]=0
# print(dict)





# update()
dict={"name":"sakshi","college":"Navgurukul","class":12,"year":2022}