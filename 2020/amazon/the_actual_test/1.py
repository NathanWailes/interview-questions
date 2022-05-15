from collections import defaultdict


def topNCompetitors(numCompetitors, topNCompetitors, competitors,
                    numReviews, reviews):
    lowercased_split_reviews = [review.lower().split() for review in reviews]
    lowercased_competitor_names = [name.lower() for name in competitors]
    word_counts = defaultdict(int)
    for review in lowercased_split_reviews:
        words_in_review = set(review)
        for word in words_in_review:
            word_counts[word] += 1

    names_to_number_of_mentions = defaultdict(int)
    for competitor_name in lowercased_competitor_names:
        if competitor_name in word_counts:
            names_to_number_of_mentions[competitor_name] = word_counts[competitor_name]

    mentioned_competitors = [(name, number_of_mentions) for name, number_of_mentions in names_to_number_of_mentions.items()]
    sorted_mentions = sorted(mentioned_competitors, key=SortedByNumberOfMentionsReversedAndThenAlphabetically)
    return [name for name, number_of_mentions in sorted_mentions[:topNCompetitors]]


class SortedByNumberOfMentionsReversedAndThenAlphabetically:
    def __init__(self, name_mention_tuple, *args):
        self.name = name_mention_tuple[0]
        self.number_of_mentions = name_mention_tuple[1]

    def __lt__(self, other):
        return self.number_of_mentions > other.number_of_mentions \
               or self.number_of_mentions == other.number_of_mentions \
               and self.name < other.name

    def __gt__(self, other):
        return self.number_of_mentions < other.number_of_mentions \
               or self.number_of_mentions == other.number_of_mentions \
               and self.name > other.name

    def __le__(self, other):
        return self.number_of_mentions > other.number_of_mentions \
               or self.number_of_mentions == other.number_of_mentions \
               and (self.name < other.name or self.name == other.name)

    def __ge__(self, other):
        return self.number_of_mentions < other.number_of_mentions \
               or self.number_of_mentions == other.number_of_mentions \
               and (self.name > other.name or self.name == other.name)

    def __eq__(self, other):
        return self.number_of_mentions == other.number_of_mentions \
               and self.name == other.name

    def __ne__(self, other):
        return self.number_of_mentions != other.number_of_mentions \
               or self.name != other.name


if __name__ == '__main__':
    answer = topNCompetitors(999, 2, ['a'], 999, ['a'])
    print(answer)
    assert(answer == ['a'])

    answer = topNCompetitors(999, 2, ['a', 'a'], 999, ['a', 'a'])
    print(answer)
    assert(answer == ['a'])

    answer = topNCompetitors(999, 2, ['b', 'a'], 999, ['a', 'a'])
    print(answer)
    assert(answer == ['a'])

    answer = topNCompetitors(999, 2, ['b', 'a'], 999, ['ab', 'a'])
    print(answer)
    assert(answer == ['a'])

    answer = topNCompetitors(999, 2, ['ba', 'a'], 999, ['b', 'a'])
    print(answer)
    assert(answer == ['a'])

    answer = topNCompetitors(999, 2,
        [
            'anacell',
            'betacellular',
            'certracular',
            'deltacellular',
            'eurocell'
        ],
        3,
        [
            'Best services provided by anacell',
            'betacellular has great services',
            'anacell provides much better services than all other'
        ]
    )
    print(answer)
    assert(answer == ['anacell', 'betacellular'])

    answer = topNCompetitors(
        999,
        2,
        [
            'anacell',
            'betacellular',
            'certracular',
            'deltacellular',
            'eurocell'
        ],
        3,
        [
            'eurocell',
            'eurocell',
            'betacellular has great services',
            'Best services provided by anacell',
            'anacell provides much better services than all other',
            'betacellular has great services',
        ]
    )
    print(answer)
    assert(answer == ['anacell', 'betacellular'])

    answer = topNCompetitors(
        999,
        2,
        [
            'anacell',
            'betacellular',
            'certracular',
        ],
        3,
        [
            'anacell',
            'betacellular',
            'betacellular',
            'certracular',
            'certracular',
            'certracular',
        ]
    )
    print(answer)
    assert(answer == ['certracular', 'betacellular'])
