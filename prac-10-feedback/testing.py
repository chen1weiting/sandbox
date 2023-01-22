def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)
test_car = Car()
    assert test_car.fuel == 0, "Car does not set fuel correctly using default value"
    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Car does not set fuel correctly using value passed in"
def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length
ef format_phrase_as_sentence(phrase):
    """
    Format the phrase as a sentence, starting with a capital and ending with a single full stop.
    >>> format_phrase_as_sentence('hello')
    'Hello.'
    >>> format_phrase_as_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_phrase_as_sentence('this is a test')
    'This is a test.'
    """
    if phrase[-1] != '.':
        return phrase.capitalize() + '.'
    else:
        return phrase