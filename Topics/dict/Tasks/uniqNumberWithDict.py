# numList = list(map(int, input().split()))
# dictList = dict.fromkeys(numList)
# print(*dictList.keys())

lst = ['3 S', '5 N', '4 Е', '7 V', '5 U', '4 S']
dict_lst = {}
for item in lst:
    dict_lst.setdefault(item[0], []).append(item[2:])

for k, v in dict_lst.items():
    print(k + ":", ", ".join(v))
