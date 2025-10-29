str_list = input().split()
lst = [item for item in str_list if len(item) > 5]
print(*lst)