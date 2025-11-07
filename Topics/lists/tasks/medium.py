def filtration_of_string_with_len_more_four(lst):
    return [x for x in lst if len(x) > 4]


def create_all_list(lst):
    res = []
    for row in lst:
        if isinstance(row, list):
            for elem in row:
                res.append(elem)
        else:
            res.append(row)
    return res
