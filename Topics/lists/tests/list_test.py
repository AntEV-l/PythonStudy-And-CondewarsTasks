import pytest
from Topics.lists.tasks import easy
from Topics.lists.tasks import medium
from Topics.lists.tasks import hard

def test_max_in_list():
    assert easy.max_in_list([1,2,3,4,5]) == 5
    assert easy.max_in_list([0,0,0,0,123]) == 123

def test_delete_duplicates():
    assert easy.delete_duplicates([1,2,2,3,3,3,4,5,5,5]) == [1,2,3,4,5]

def test_reverse_without_revers():
    assert easy.reverse_without_revers(["a","b","c","d"]) == ["d","c","b","a"]

def test_amount_off_even():
    assert easy.amount_of_even([1,2,3,4,5,6]) == 3


def test_amount_celsium_to_farengheit():
    assert easy.celsium_to_farengheit([0,10,20,30,40]) == [32,50,68,86,104]

#middle
def test_filtration_of_string_with_len_more_four():
    assert medium.filtration_of_string_with_len_more_four(["hello", "world", "python", "programming", "code", "list"]) == ['hello', 'world', 'python', 'programming']

def test_create_all_list():
    assert medium.create_all_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 4, 5,6,7,8,9]
    assert medium.create_all_list([[1, 2, 3], [4, 5, 6], [7, 8, 9], 10,11,12, "abc"])

def test_unic_elem_with_strict_order():
    assert hard.unic_elem_with_strict_order([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]