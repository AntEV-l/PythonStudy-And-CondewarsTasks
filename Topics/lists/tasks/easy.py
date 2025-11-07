def sum_list(lst):
    return sum(lst)

def max_in_list(lst): # without using max
    max_value = 0
    for value in lst:
        if value > max_value:
            max_value = value
    return max_value

def delete_duplicates(lst):
    return list(set(lst))

def reverse_without_revers(lst):
    return lst[::-1]

def amount_of_even(lst):
    return sum([1 for value in lst if value % 2 == 0 ])


def celsium_to_farengheit(arg):
    return [x * 9/5 + 32 for x in arg]
