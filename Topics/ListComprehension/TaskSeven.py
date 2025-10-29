lst_one = input().split()
lst_odd = [x for ind, x in enumerate(lst_one) if ind % 2 == 0]
lst_even = [x for ind, x in enumerate(lst_one) if ind % 2 != 0]
lst_result = [[lst_odd[i], int(lst_even[i])] for i in range(len(lst_odd))]
print(lst_result)