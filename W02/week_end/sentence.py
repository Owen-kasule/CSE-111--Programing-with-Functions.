import random

def get_determiner(quantity):
    """Return a randomly chosen determiner."""
    determiners = {
        1: ["a", "one", "the"],
        "plural": ["some", "many", "the"]
    }
    return random.choice(determiners[1] if quantity == 1 else determiners["plural"])

def get_noun(quantity):
    """Return a randomly chosen noun."""
    nouns = {
        1: ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"],
        "plural": ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    }
    return random.choice(nouns[1] if quantity == 1 else nouns["plural"])

def get_verb(quantity, tense):
    """Return a randomly chosen verb based on tense and quantity."""
    verbs = {
        "past": ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"],
        "present_singular": ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"],
        "present_plural": ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"],
        "future": ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    }
    # Select the correct verb form based on quantity and tense
    if tense == "past":
        return random.choice(verbs["past"])
    elif tense == "present":
        key = "present_singular" if quantity == 1 else "present_plural"
        return random.choice(verbs[key])
    elif tense == "future":
        return random.choice(verbs["future"])

def get_preposition():
    """Return a randomly chosen preposition from a list."""
    prepositions = [
        "about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"
    ]
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase with a preposition, determiner, and noun."""
    return f"{get_preposition()} {get_determiner(quantity)} {get_noun(quantity)}"

def make_sentence(quantity, tense):
    """Construct and return a sentence with determiner, noun, verb, and two prepositional phrases."""
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase1 = get_prepositional_phrase(quantity)
    prepositional_phrase2 = get_prepositional_phrase(quantity)
    sentence = f"{determiner.capitalize()} {noun} {verb} {prepositional_phrase1} {prepositional_phrase2}."
    return sentence

def main():
    # Print six sentences with specified grammar combinations
    print(make_sentence(1, "past"))     # single, past
    print(make_sentence(1, "present"))  # single, present
    print(make_sentence(1, "future"))   # single, future
    print(make_sentence(2, "past"))     # plural, past
    print(make_sentence(2, "present"))  # plural, present
    print(make_sentence(2, "future"))   # plural, future

# Call the main function
if __name__ == "__main__":
    main()
