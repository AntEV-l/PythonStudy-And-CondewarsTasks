import pytest
from Topics.dict.Tasks import grok_easy
from Topics.dict.Tasks import grok_elementary

def test_add_fruit():
    assert grok_easy.add_fruit("banana", 12) == {'apple': 1, 'orange': 2, 'banana': 12}

def test_get_key():
    assert grok_easy.get_key(grok_easy.fruits,"apple" ) == "apple"
    assert grok_easy.get_key(grok_easy.fruits, "some_key") is None

def test_check_key():
    assert grok_easy.check_key(grok_easy.fruits,"apple") is True
    assert grok_easy.check_key(grok_easy.fruits,"not a key") is False

def test_unification_two_dict():
    assert (grok_elementary.unification_two_dict({"apple":1}, {"orange":2})
            == {"apple": 1, "orange": 2})
