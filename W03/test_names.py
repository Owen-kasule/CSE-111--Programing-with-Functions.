from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    # Test normal names
    assert make_full_name("John", "Doe") == "Doe; John"
    assert make_full_name("Marie", "Curie") == "Curie; Marie"
    
    # Test hyphenated names
    assert make_full_name("Anna", "Smith-Jones") == "Smith-Jones; Anna"
    
    # Test short names
    assert make_full_name("A", "B") == "B; A"

def test_extract_family_name():
    # Test normal names
    assert extract_family_name("Doe; John") == "Doe"
    assert extract_family_name("Curie; Marie") == "Curie"
    
    # Test hyphenated names
    assert extract_family_name("Smith-Jones; Anna") == "Smith-Jones"
    
    # Test short names
    assert extract_family_name("B; A") == "B"

def test_extract_given_name():
    # Test normal names
    assert extract_given_name("Doe; John") == "John"
    assert extract_given_name("Curie; Marie") == "Marie"
    
    # Test hyphenated names
    assert extract_given_name("Smith-Jones; Anna") == "Anna"
    
    # Test short names
    assert extract_given_name("B; A") == "A"

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])