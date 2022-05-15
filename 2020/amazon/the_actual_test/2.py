

def reorderElements(logFileSize, logLines):
    """ My approach here is to first separate out the lines that contain numbers
    from those that contain words into separate lists, then sort the list with
    the lines that contain words, then recombine the lists.

    :param logFileSize:
    :param logLines:
    :return:
    """
    split_lines = [line.split() for line in logLines]

    tuples_of_the_identifiers_and_line_values = [(split_line[0], ' '.join(split_line[1:])) for split_line in split_lines]
    word_lines_tuples = []
    number_lines_tuples = []
    for tuple_of_identifier_and_value in tuples_of_the_identifiers_and_line_values:
        line_value = tuple_of_identifier_and_value[1]
        first_character_of_the_line_value = line_value[0]
        if first_character_of_the_line_value.isdigit():
            number_lines_tuples.append(tuple_of_identifier_and_value)
        else:
            word_lines_tuples.append(tuple_of_identifier_and_value)

    word_lines_tuples = sorted(word_lines_tuples, key=lambda item: (item[1], item[0]))
    combined_result = word_lines_tuples + number_lines_tuples
    return [identifier + ' ' + value for identifier, value in combined_result]


if __name__ == '__main__':
    answer = reorderElements(
        5,
        [
            'a 9',
            'e act car',
            'b act car',
            'c 4',
            'd off key dog',
            'e act zoo',
        ]
    )
    print(answer)
    assert answer == [
        'b act car',
        'e act zoo',
        'd off key dog',
        'a 9',
        'c 4'
    ]
