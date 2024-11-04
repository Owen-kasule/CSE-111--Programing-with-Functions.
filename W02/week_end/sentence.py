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
    if tense == "past":
        return random.choice(verbs["past"])
    elif tense == "present":
        return random.choice(verbs["present_singular"] if quantity == 1 else verbs["present_plural"])
    elif tense == "future":
        return random.choice(verbs["future"])

def get_preposition():
    """Return a randomly chosen preposition from a list of prepositions."""
    prepositions = [
        "about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"
    ]
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase with a preposition, determiner, and noun."""
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    return f"{preposition} {determiner} {noun}"

def get_adjective():
    """Return a randomly chosen adjective from a list of adjectives."""
    adjectives = ["quick", "lazy", "sleepy", "noisy", "happy", "bright", "red", "green", "blue", "big"]
    return random.choice(adjectives)

def get_adverb():
    """Return a randomly chosen adverb from a list of adverbs."""
    adverbs = ["quickly", "slowly", "loudly", "quietly", "happily", "sadly", "brightly", "gracefully"]
    return random.choice(adverbs)

def make_sentence(quantity, tense):
    """Construct a grammatically correct sentence with determiner, noun, verb, two prepositional phrases, and optionally adjective and adverb."""
    determiner = get_determiner(quantity)
    adjective = get_adjective()
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    adverb = get_adverb()
    prepositional_phrase1 = get_prepositional_phrase(quantity)
    prepositional_phrase2 = get_prepositional_phrase(quantity)
    
    # Construct the sentence
    sentence = f"{determiner.capitalize()} {adjective} {noun} {prepositional_phrase1} {adverb} {verb} {prepositional_phrase2}."
    return sentence

def main():
    # Print sentences with different quantities and tenses
    print(make_sentence(1, "past"))     # single, past
    print(make_sentence(1, "present"))  # single, present
    print(make_sentence(1, "future"))   # single, future
    print(make_sentence(2, "past"))     # plural, past
    print(make_sentence(2, "present"))  # plural, present
    print(make_sentence(2, "future"))   # plural, future

# Call the main function
if __name__ == "__main__":
    main()
