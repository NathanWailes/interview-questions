"""
findWord(["P>E","E>R","R>U"]) // PERU
findWord(["I>N","A>I","P>A","S>P"]) // SPAIN


"""


def find_word(list_of_relations):
    """
    >>> find_word(['P>E', 'E>R', 'R>U'])
    'PERU'

    >>> find_word(['I>N', 'A>I', 'P>A', 'S>P'])
    'SPAIN'

    >>> find_word(['I>N'])
    'IN'

    :return:
    """
    dict_of_characters_to_next_characters = {}
    for index, relationship_as_a_string in enumerate(list_of_relations):
        first_character = relationship_as_a_string[0]
        second_character = relationship_as_a_string[2]
        dict_of_characters_to_next_characters[first_character] = second_character

    first_character_in_the_word = None
    for character in dict_of_characters_to_next_characters.keys():
        if character not in dict_of_characters_to_next_characters.values():
            first_character_in_the_word = character

    word = ''
    word += first_character_in_the_word
    next_character = dict_of_characters_to_next_characters[first_character_in_the_word]
    while next_character:
        word += next_character
        next_character = dict_of_characters_to_next_characters.get(next_character)

    return word


print(find_word(["U>N", "G>A", "R>Y", "H>U", "N>G", "A>R"])) #// HUNGARY
print(find_word(["I>F", "W>I", "S>W", "F>T"])) #// SWIFT
print(find_word(["R>T", "A>L", "P>O", "O>R", "G>A", "T>U", "U>G"])) #// PORTUGAL
print(find_word(["W>I", "R>L", "T>Z", "Z>E", "S>W", "E>R", "L>A", "A>N", "N>D", "I>T"])) #// SWITZERLAND