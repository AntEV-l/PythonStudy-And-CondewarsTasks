def unification_two_dict(dicti_one, dicti_two):
    dicti_res = dicti_one.copy()
    dicti_res.update(dicti_two)
    return dicti_res

print(unification_two_dict({"apple":1, "orange":2}, {"banana":5}))

def delete_elem_with_even_value(dicti):
    return {k: v for k,v in dicti.items() if v % 2}

# Sample Input:
# +71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890
# Sample Output:
# ('+2', ['+21235777890', '+21234567110']) ('+5', ['+52134567890']) ('+6', ['+61234576890']) ('+7', ['+71234567890', '+71234567854', '+71232267890'])

numbers = input().split()  #we are creating a list
d = {}
for number in numbers:
    code = number[:2] # we take two first char from num
    if code not in d:
        d[code] = [] #create a new data in dicti key:code data:list
    d[code].append(number) #add value at list
print(*sorted(d.items()))