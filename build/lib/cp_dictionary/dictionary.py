def generator_of_words(of_length=None):
    """
    A generator for a list of words from a dictionary.
    :param of_length: Length. If not specified, all words will be returned.
    :return: Yields a new word at every iteration, as long as there are words.
    """

    if of_length:
        dictionary_file = "txt/words%d.txt" % of_length
    else:
        dictionary_file = "txt/words.txt"

    try:
        dictionary = open(dictionary_file, 'r')
        for line in dictionary:
            word = line.rstrip('\n')
            if word == "":  # We don't want empty lines.
                continue
            yield word
        dictionary.close()

    except IOError:
        raise Exception("Unable to find or read dictionary (%s)." % dictionary_file)


def list_of_words(of_length=None):
    """
    Returns a list of words from a dictionary.
    :param of_length: Length. If not specified, all words will be returned.
    :return: A list of lowercase words.
    """
    return list(generator_of_words(of_length=of_length))
