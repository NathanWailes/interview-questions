import csv
from datetime import timedelta

class UserWeekRow:
    def __init__(self, user, ending_sunday):
        self.user = user

        #Timestamp (should always be a Sat midnight CDT)
        self.ending_sunday = ending_sunday #assuming a datetime object
        self.starting_sunday = self.ending_sunday - timedelta(days=7)
        self.date_31_days_before = self.ending_sunday - timedelta(days=31)

        self.mentions_in_past_7_days = self.count_tweets("Mention", 7)
        self.mentions_in_past_31_days = self.count_tweets("Mention", 31)

        self.replies_in_past_7_days = self.count_tweets("Reply", 7)
        self.replies_in_past_31_days = self.count_tweets("Reply", 31)

        self.retweets_in_past_7_days = self.count_tweets("Retweet", 7)
        self.retweets_in_past_31_days = self.count_tweets("Retweet", 31)

        self.distinct_target_users_in_last_31_days = user.count_distinct_target_users_between_dates(self.date_31_days_before, self.ending_sunday)
        self.number_of_actions_in_last_31_days = self.count_tweets("Any", 31)

        #Ratio of # Distinct Target Users to # Actions in Past 31 Days
        #(0 if no actions)
        if self.number_of_actions_in_last_31_days == 0:
            self.targets_to_actions_ratio = 0
        else:
            targets = self.distinct_target_users_in_last_31_days
            actions = self.number_of_actions_in_last_31_days
            self.targets_to_actions_ratio = float(targets) / actions

    def count_tweets(self, tweet_type, days_back):
        start_date = self.ending_sunday - timedelta(days=days_back)
        tweet_count = self.user.count_tweets_between_dates(start_date, self.ending_sunday, tweet_type)
        return tweet_count

    def output_csv_row(self, output_path):
        with open(output_path, "a") as csv_output:
            csv_writer = csv.writer(csv_output, lineterminator = '\n')
            csv_writer.writerow([self.user.id,
                                 self.ending_sunday.strftime('%a %b %d %H:%M:%S CDT %Y'),
                                 self.mentions_in_past_7_days,
                                 self.mentions_in_past_31_days,
                                 self.replies_in_past_7_days,
                                 self.replies_in_past_31_days,
                                 self.retweets_in_past_7_days,
                                 self.retweets_in_past_31_days,
                                 self.targets_to_actions_ratio])
