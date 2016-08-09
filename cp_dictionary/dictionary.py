from .words import all_words


def generator_of_words(of_length=None):
    """
    A generator for a list of words from a dictionary.
    :param of_length: Length. If not specified, all words will be returned.
    :return: Yields a new word at every iteration, as long as there are words.
    """

    for word in all_words:

        if word == "":  # We don't want empty lines.
            continue

        if (of_length is not None) and (of_length != len(word)):
            continue

        yield word


def list_of_words(of_length=None):
    """
    Returns a list of words from a dictionary.
    :param of_length: Length. If not specified, all words will be returned.
    :return: A list of lowercase words.
    """
    return list(generator_of_words(of_length=of_length))

