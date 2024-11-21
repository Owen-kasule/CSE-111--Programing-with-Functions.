from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("John", "Doe") == "Doe; John"
    assert make_full_name("Ava", "Smith-Jones") == "Smith-Jones; Ava"
    assert make_full_name("Jane", "O'Connor") == "O'Connor; Jane"
    assert make_full_name("Emily", "Van Buren") == "Van Buren; Emily"

def test_extract_family_name():
    assert extract_family_name("Doe; John") == "Doe"
    assert extract_family_name("Smith-Jones; Ava") == "Smith-Jones"
    assert extract_family_name("Van Buren; Emily") == "Van Buren"
    assert extract_family_name("O'Connor; Jane") == "O'Connor"

def test_extract_given_name():
    assert extract_given_name("Doe; John") == "John"
    assert extract_given_name("Smith-Jones; Ava") == "Ava"
    assert extract_given_name("Van Buren; Emily") == "Emily"
    assert extract_given_name("O'Connor; Jane") == "Jane"

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])