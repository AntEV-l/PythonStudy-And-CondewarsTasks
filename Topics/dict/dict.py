# d = {"key":"value", "key2":"value2", "key3":"value3"}
# value = d["key"]
# print(value)
# d2 = dict(one=1, two=2, three=3)
# print(d2)
# lst = [[1,2],[4,5],[7,8]]
# res = dict(lst)
# print(res)
#
# #del
# del d["key"]
# k = "abc" in d  # key in dict. Return true or false



#
# values = input().split()
# res = {item.split('=',1)[0]: item.split('=',1)[1] for item in values}
# d = {key:value for key,value in res.items() if key not in ["False", "3"]}
# print(*sorted(d.items()))


# for i in range(0, len(lst_in), 2):
#     phone = lst_in[i]
#     name = lst_in[i + 1]
#     result.append(f"{phone} {name}")
# print(result)

lst_in = input().split(" ")
result =[f"{lst_in[i]} {lst_in[i + 1].rstrip()}" for i in range(0, len(lst_in), 2)]
d = {}
for items in result:
    val,key = items.split() # value and key from the first elem of list
    if key not in d:
        d[key] = []
    d[key].append(val)
print(*sorted(d.items()))



# +71234567890 Serg +71234567810 Serg +51234567890 Miha +72134567890 Nikola