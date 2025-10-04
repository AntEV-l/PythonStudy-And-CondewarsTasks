# https://www.codewars.com/kata/54edbc7200b811e956000556/train/python
list_sheep = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]


def count_sheeps(sheep):
    counter = 0
    for item in sheep:
        if item:
            counter += 1
    return counter
print(count_sheeps(list_sheep))