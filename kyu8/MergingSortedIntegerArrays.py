def merge_arrays(first, second):
    return sorted(set(first + second))
print(merge_arrays([2, 4, 8], [2, 4, 6]))