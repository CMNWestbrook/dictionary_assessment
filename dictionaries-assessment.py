"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""


def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    word_and_occurrence = {}
    phrase = phrase.split()

    for word in phrase:
        if word in word_and_occurrence:
            word_and_occurrence[word] += 1
        else:
            word_and_occurrence[word] = 1

    return word_and_occurrence


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """
    melons = {"Watermelon": 2.95, "Cantaloupe": 2.50, "Musk": 3.25, "Christmas": 14.25}

    return melons.get(melon_name, "No price found")
    # for melon, price in melons.items():
    #     if str(melon) == str(melon_name):
    #         return price
    #     else:
    #         return "No price found"


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

        >>> word_length_sorted(["porcupine", "ok"])
        [(2, ['ok']), (9, ['porcupine'])]
    """
    dict_of_lengths = {}
    list_of_tuples = []

    for word in words:
        length_word = len(word)
        if length_word in dict_of_lengths:
            dict_of_lengths[length_word].append(word)
            # list_of_tuples.append((length_word, [word[1]] + [word]))
            # length_word = length_word[[word[0]] + [word]]
            #list_of_tuples.append((length_word, [word[1]] + [word]))
        else:
            dict_of_lengths[length_word] = [word]
            #.append((length_word, [word]))
                #list_of_tuples.append((word.extend(word)),)
    #list_of_tuples = list_of_tuples.sort()
    for key, value in dict_of_lengths.items():
        list_of_tuples.append((key, sorted(value)))

    list_of_tuples = sorted(list_of_tuples)

    return list_of_tuples

    # for word in words:
    #     for letters in word:
    #         i = len(letters)
    #         if i in list_of_tuples:
    #             list_of_tuples.append((i, [word],))
    #         else:
    #             list_of_tuples.append((i, [word + word],))

    #             #list_of_tuples.append((word.extend(word)),)
    # list_of_tuples = list_of_tuples.sort()
    # return list_of_tuples

    #     list_of_tuples = []
    # i = 1
    # for word in words:
    #     if word in list_of_tuples:
    #         list_of_tuples.append(((i += 1), word.append(word))
    #     else:
    #         list_of_tuples.append((i, [word]))

    # return list_of_tuples


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    english_to_pirate = {"sir": "matey", "hotel": "fleabag inn", "student": "swabbie",
    "man": "matey", "professor": "foul blaggart", "restaurant": "galley",
    "your": "yer", "excuse": "arr", "students": "swabbies", "are": "be", "restroom": "head",
    "my": "me", "is": "be"}

    phrase = phrase.split()
    updated_phrase = ""
    #for english_word, pirate_word in english_to_pirate.items():
    for word in phrase:
        if word in english_to_pirate:
            pirate_word = english_to_pirate[word]
            updated_phrase = str(updated_phrase) + ' ' + str(pirate_word)
        else:
            updated_phrase = str(updated_phrase) + ' ' + str(word)
    #.strip included to delete extra white space at beginning or end of the new string
    return updated_phrase.strip()


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    #An empty dictionary stores the first_letter in each name as a key and to 
    #store the words that all start with that letter as the value inside a list
    nonsense_words_beginning = {}
    #this list will store the new list of words to return
    new_nonsense_list = []
    for name in names:
        first_letter = name[0]
        if first_letter in nonsense_words_beginning:
            nonsense_words_beginning[first_letter].append(name)
        else:
            nonsense_words_beginning[first_letter] = [name]

    new_nonsense_list.append(names[0])

    current_name = names[0]
    while True:
        last_char = current_name[-1]
        if last_char in nonsense_words_beginning:
            words = nonsense_words_beginning[last_char]
            next_word = words[0]
            new_nonsense_list.append(next_word)
            words.remove(next_word)
            if len(words) < 1:
                del nonsense_words_beginning[last_char]
        else:
            break

    # for name in names:
    #     #key, value = nonsense_words_beginning
    #     for key, value in nonsense_words_beginning.items():
    #         if name[-1] == key:
    #             new_nonsense_list.append(value[0])
    #             value.remove(value[0])

    #soooo close!
    return new_nonsense_list



#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
