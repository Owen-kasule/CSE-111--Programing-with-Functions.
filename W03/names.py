# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

def make_full_name(given_name, family_name):
    """Return a string in this form "family_name; given_name". For
    example, if this function were called like this:
    make_full_name("Sally", "Brown"), it would return "Brown; Sally".

    Parameters
        given_name: a string that contains a person's given name
        family_name: a string that contains a person's family name
    Return: a string in the form "family_name; given_name"
    """
    # Add a space after the semicolon for correct formatting.
    full_name = f"{family_name}; {given_name}"
    return full_name

def extract_family_name(full_name):
    """Extract and return the family name from a string in this form:
    "family_name; given name". For example, if this function were
    called like this:
    extract_family_name("Brown; Sally"), it would return "Brown".

    Parameter:
        full_name: a string in the form "family_name; given name"
    Return: a string that contains a person's family name
    """
    try:
        # Split the full name and extract the family name.
        family_name, _ = full_name.split("; ")
        return family_name
    except ValueError:
        raise ValueError(f"Input does not match the expected format: {full_name}")

def extract_given_name(full_name):
    """Extract and return the given name from a string in this form:
    "family_name; given name". For example, if this function were
    called like this:
    extract_given_name("Brown; Sally"), it would return "Sally".

    Parameter:
        full_name: a string in the form "family_name; given name"
    Return: a string that contains a person's given name
    """
    try:
        # Split the full name and extract the given name.
        _, given_name = full_name.split("; ")
        return given_name
    except ValueError:
        raise ValueError(f"Input does not match the expected format: {full_name}")
