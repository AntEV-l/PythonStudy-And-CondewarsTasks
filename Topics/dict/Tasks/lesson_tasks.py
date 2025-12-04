#firts
#input one=1 two=2 three=3
# output  ('one', 1) ('three', 3) ('two', 2)
# input_list = input().split(" ")
# res = [item.split("=") for item in input_list]
# dict_r = dict(res)
# d = {key:int(value) for key, value in dict_r.items()}
# print(*sorted(d.items()))


#second without dict
# input 5=nice 4=good 3=so-so
# output (5, "nice") (4, "good") (3, "so-so")
lst_in_second = input().split(" ")
res_list = [item.split("=") for item in lst_in_second]
d = {}
for item in res_list:
    key, value = item[0], item[1]
    d[int(key)] = value
print(*sorted(d.items()))