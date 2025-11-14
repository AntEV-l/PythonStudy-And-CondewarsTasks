# https://www.codewars.com/kata/52705ed65de62b733f000064/train/python
val = [
  {"a": 1, "b": 3},
  {"a": 3, "b": 2},
  {"a": 2, "b": 40},
  {"a": 4, "b": 12}
]

def sort_list(sort_by, lst):
    return sorted(lst, key=lambda v: v[sort_by], reverse=True)
