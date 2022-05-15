from collections import defaultdict


def topNCompetitors(numCompetitors, topNCompetitors, competitors,
                    numReviews, reviews):
    mentions = defaultdict(int)
    lowercased_split_reviews = [review.lower().split() for review in reviews]
    lowercased_competitor_names = [name.lower() for name in competitors]
    for review in lowercased_split_reviews:
        for competitor_name in lowercased_competitor_names:
            if competitor_name in review:
                mentions[competitor_name] += 1
    mentioned_competitors = [(name, number_of_mentions) for name, number_of_mentions in mentions.items()]
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