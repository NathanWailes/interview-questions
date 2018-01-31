import csv
from datetime import datetime, timedelta
from dateutil import parser
from user import User
from tweet import Tweet
from user_week_row import UserWeekRow

class TwitterActivityLogProcessor:
    '''I don't love the name of this class. I'll try to think of a better one.'''
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        return

    def set_first_and_last_sundays(self):
        input_path = self.input_path
        [earliest_tweet, latest_tweet] = self.get_first_and_last_tweets(input_path)

        sunday = 6 # 6 is the datetime.weekday() code for Sunday
        while earliest_tweet.weekday() != sunday:
            earliest_tweet += timedelta(days=1)
        while latest_tweet.weekday() != sunday:
            latest_tweet -= timedelta(days=1)

        self.earliest_sunday = datetime(earliest_tweet.year, earliest_tweet.month, 
                                     earliest_tweet.day, 0, 0, 0)
        self.latest_sunday = datetime(latest_tweet.year, latest_tweet.month,
                                   latest_tweet.day, 0, 0, 0)

    def get_first_and_last_tweets(self, input_path):
        with open(input_path, newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')

            next(csv_reader) #skip the header row

            earliest_tweet = datetime(2100, 1, 1)
            latest_tweet = datetime(1900, 1, 1)

            for timestamp, user_id, action, target_user_id in csv_reader:
                tweet_datetime = parser.parse(timestamp)

                if tweet_datetime > latest_tweet:
                    latest_tweet = tweet_datetime
                if tweet_datetime < earliest_tweet:
                    earliest_tweet = tweet_datetime

        return [earliest_tweet, latest_tweet]

    def step_through_input_csv(self):
        '''Come up with a better name for this function.'''
        with open(self.input_path, newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            last_user = 0

            #skip the header row
            next(csv_reader)

            for timestamp, user_id, action, target_user_id in csv_reader:
                #get the tweet ready
                datetime_timestamp = parser.parse(timestamp)
                current_tweet = Tweet(datetime_timestamp, user_id, action,
                                      target_user_id)

                #Set the user who should have the tweet added.
                #(It assumes the users' tweets will all be grouped together.)
                if (last_user != 0) and (last_user.id == user_id): 
                    current_user = last_user
                else:
                    #If it's a new user, export the last one's data.
                    if (last_user != 0) and (last_user.id != user_id):
                        #output csv data
                        print("Now exporting user: " + last_user.id)
                        self.output_user_data(last_user)

                        #clear memory
                        last_user = None
                    current_user = User(user_id)

                #add the tweet
                current_user.add_tweet(current_tweet)

                #keep track of the current user for the next row
                last_user = current_user

            #need this to handle the last user in the csv file
            print("Now exporting user: " + last_user.id)
            self.output_user_data(last_user)
        return

    def output_user_data(self, user):
        # The first week ends 7 days after the first Sunday
        current_week = UserWeekRow(user, self.earliest_sunday + timedelta(days=7))

        while current_week.ending_sunday <= self.latest_sunday:
            #Output the current week
            current_week.output_csv_row(self.output_path)

            #Prepare the next week
            current_week = UserWeekRow(user, current_week.ending_sunday + timedelta(days=7))

def main():
    input_path = "sample.csv"
    output_path = "output.csv"
    processor = TwitterActivityLogProcessor(input_path, output_path)
    processor.set_first_and_last_sundays()
    processor.step_through_input_csv()

if __name__ == '__main__':
    main()
