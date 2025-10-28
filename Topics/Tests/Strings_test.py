import pytest

from Topics.Strings.count_vowels import count_vowels
from Topics.Strings.format_phone_number import format_phone_number
from Topics.Strings.palindrom import is_palindrome


def test_is_palindrome_true():
    assert is_palindrome("radar") == True

def test_is_palindrome_false():
    assert is_palindrome("hello") == False

@pytest.mark.parametrize("string", [
    "radar", "level", "nun", "deed"
])
def test_function(string):
    assert is_palindrome(string) == True



def test_count_vowels():
    assert count_vowels("hEllo") == 2

def test_count_vowels2():
    assert count_vowels("brrr") == "not found"

def test_format_phone_number():
    assert format_phone_number("39991234567") == "+3 (999) 123-45-67"

def test_format_phone_number_2():
    assert format_phone_number(39991234567) == "+3 (999) 123-45-67"
