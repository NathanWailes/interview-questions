class Tweet:
    def __init__(self, timestamp, user_id, action, target_user_id):
        self.timestamp = timestamp #assuming a datetime object
        self.user_id = user_id #string user id, not a User object
        self.action = action
        self.target_user_id = target_user_id
