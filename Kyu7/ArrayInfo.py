# https://www.codewars.com/kata/57f12b4d5f2f22651c00256d/train/python
array = [0.001,2,' ']
# def array_info(x):
# ## the code isn't gonna write itself!
#     if len(x) == 0:
#         return 'Nothing in the array!'
#     integer = 0
#     float_num = 0
#     string_num = 0
#     whitespace = 0
#
#     for item in x:
#         if isinstance(item, int):
#             integer += 1
#         elif isinstance(item, float):
#             float_num += 1
#         elif isinstance(item, str):
#             if item.isspace():
#                 whitespace += 1
#             else:
#                 string_num += 1
#     integer = integer if integer > 0 else None
#     float_num = float_num if float_num > 0 else None
#     string_num = string_num if string_num > 0 else None
#     whitespace = whitespace if whitespace > 0 else None
#     return [[len(x)], [integer], [float_num], [string_num], [whitespace]]

def array_info(x):
    if not x:
        return 'Nothing in the array!'
    return [
        [len(x)],
        [sum(isinstance(i, int) for i in x) or None],
        [sum (isinstance(i, float) for i in x) or None],
        [sum (isinstance(i, str) and not i.isspace() for i in x) or None],
        [sum (isinstance(i, str) and i.isspace() for i in x) or None]
    ]
