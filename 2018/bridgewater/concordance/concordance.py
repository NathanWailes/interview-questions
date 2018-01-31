import nltk
from nltk import tokenize


def main(input_string):
    input_string = " ".join(input_string.splitlines())

    try:
        sentences = tokenize.sent_tokenize(input_string)
    except LookupError:
        nltk.download('punkt')
        sentences = tokenize.sent_tokenize(input_string)

    concordance_dict = dict()

    for zero_indexed_sentence_index, sentence in enumerate(sentences):
        tokens = nltk.word_tokenize(sentence)  # This'll include both words and punctuation.
        words = [word for word in tokens if word.isalpha()]

        for word in words:
            one_indexed_sentence_index = zero_indexed_sentence_index + 1  # The question asked for one-indexed sentence indices
            if word not in concordance_dict:
                concordance_dict[word] = {'count': 1,
                                          'sentence_indices': {one_indexed_sentence_index}}
            else:
                incremented_count = concordance_dict[word]['count'] + 1
                sentence_indices = concordance_dict[word]['sentence_indices']
                sentence_indices.add(one_indexed_sentence_index)
                concordance_dict[word] = {'count': incremented_count,
                                          'sentence_indices': sentence_indices}

    # Convert to a list.
    output_list = []
    for word, count_and_sentence_indices in concordance_dict.items():
        count_and_sentence_indices['word'] = word
        output_list.append(count_and_sentence_indices)

    # Sort the list.
    output_list = sorted(output_list, key=lambda word_dict: word_dict['word'])

    return output_list


if __name__ == '__main__':
    test_input = """Given an arbitrary text document written in English, write a program that will generate a 
            concordance, i.e. an alphabetical list of all word occurrences, labeled with word frequencies.
            Bonus: label each word with the sentence numbers in which each occurrence appeared."""
    for entry in main(test_input):
        print(entry['word'], entry['count'], entry['sentence_indices'])
