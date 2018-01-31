class User:

    def __init__(self, user_id):
        self.id = user_id
        self.tweets = []

    def add_tweet(self, tweet):
        self.tweets.append(tweet)

    def count_tweets_between_dates(self, start_date, end_date, tweet_type):
        tweet_sum = 0
        for tweet in self.tweets:
            if tweet_type != tweet.action and tweet_type != "Any":
                continue
            elif tweet.timestamp > start_date and tweet.timestamp < end_date:
                tweet_sum += 1
        return tweet_sum

    def count_distinct_target_users_between_dates(self, start_date, end_date):
        distinct_target_users = set()
        for tweet in self.tweets:
            if tweet.timestamp > start_date and tweet.timestamp < end_date:
                distinct_target_users.add(tweet.target_user_id)
        return len(distinct_target_users)

def main():
    test_user = User("12345")
    print (test_user.id)

if __name__ == '__main__':
    main()
