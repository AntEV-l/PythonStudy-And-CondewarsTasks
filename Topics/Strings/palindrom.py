def is_palindrome(s):
    return True if s == s[::-1] else False

def test_is_palindrome_true():
    assert is_palindrome("radar") == True
