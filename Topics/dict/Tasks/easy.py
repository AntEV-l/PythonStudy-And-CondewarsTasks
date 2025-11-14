def amount_char_in_string(some_string):
    dicti = {}
    for item in some_string:
        dicti.update({item:some_string.count(item)})
    return dicti
#task one
# value = input().split(" ")
lst_two = [item.split('=') for item in value]
for item in lst_two:
    for elem in item:
        item[1] = int(item[1])
d = dict(lst_two)
print(*sorted(d.items()))

# task two create dict without dict
d3 = {}
value_two = input().split(" ")
lst_three = [item.split('=') for item in value_two]
for item in lst_three:
    d3[int(item[0])] = item[1]
print(*sorted(d3.items()))


# task three
input_field = input().split(" ")
print(input_field)
dicti = dict(item.split("=") for item in input_field)
print("ДА") if "house" and "True" and "5"  in dicti else print("НЕТ")
