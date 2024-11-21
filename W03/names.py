# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

from names import make_full_name, extract_family_name, extract_given_name
import pytest

def make_full_name(given_name, family_name):
    """Return a string in this form "family_name; given_name". For
    example, if this function were called like this:
    make_full_name("Sally", "Brown"), it would return "Brown; Sally".

    Parameters
        given_name: a string that contains a person's given name
        family_name: a string that contains a person's family name
    Return: a string in the form "family_name; given_name"
    """
    full_name = f"{family_name};{given_name}"
    return full_name

def extract_family_name(full_name):
    """Extract and return the family name from a string in this form:
    "family_name; given_name". For example, if this function were
    called like this:
    extract_family_name("Brown; Sally"), it would return "Brown".

    Parameter:
        full_name: a string in the form "family_name; given name"
    Return: a string that contains a person's family name
    """
    # Find the index where "; " appears within the full name string.
    semicolon_index = full_name.index("; ")

    # Extract a substring from the full name and return it.
    family_name = full_name[0 : semicolon_index]
    return family_name

def extract_given_name(full_name):
    """Extract and return the given name from a string in this form:
    "family_name; given name". For example, if this function were
    called like this:
    extract_given_name("Brown; Sally"), it would return "Sally".

    Parameter:
        full_name: a string in the form "family_name; given name"
    Return: a string that contains a person's given name
    """
    # Find the index where "; " appears within the full name string.
    semicolon_index = full_name.index("; ")

    # Extract a substring from the full name and return it.
    given_name = full_name[semicolon_index + 2 : ]
    return given_name

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