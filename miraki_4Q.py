# dic={
#     1:"NAVGURUKUL",
#     2:"in",
#     3:{
#         "A": "WELCOME",
#         "B": "to",
#         "C": "DHARAMASALA"
#     }
# }
# for i in dic:
#     if type(dic[i])==type(dic):
#         for j in dic[i]:
#             del dic[i][j]
#             break
# print(dic)

dict={1:"NAVGURUKUL",2:"IN",3:{"A":"WELCOME","B":"TO","C":"DHARAMSALA"}}
for i in dict:
    if type(dict[i])==type(dict):
        for j in dict[i]:
            del dict [i][j]
            break
print(dict)

# dict={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1964
# }
# dict.pop("model")
# print(dict)

