lst_value = list(map(float, input().split()))
result_lst = [item for index, item in enumerate(lst_value) if index % 2 == 0 ]
print(result_lst)