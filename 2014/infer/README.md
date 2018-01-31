# Processing Twitter Activity Logs

When analyzing datasets, munging (processing) the data and getting it into the shape you want can often be the most important part of the job.  For this assignment we’re going to work with a public dataset available from Twitter.  Your task is to process the data into a particular format, which is suitable for feeding into a statistical/machine learning algorithm for predicting future activities.

For the following, feel free to use any combination of programming languages, technology, libraries, etc. that you’d like.

You’re given a CSV of Twitter’s user activity logs:
```
Timestamp,User,Action,Target User
Wed Sep  3 05:15:39 CDT 2011,143248659,Retweet,55121922
Thu Sep  4 13:13:33 CDT 2011,143248659,Retweet,189474615
Sun Sep  7 14:23:36 CDT 2011,65165115,Mention,143248659
Mon Sep  8 01:39:08 CDT 2011,65165115,Retweet,236403070
Tue Sep  9 17:59:26 CDT 2011,143248659,Retweet,65165115
Wed Sep 10 18:57:31 CDT 2011,65165115,Retweet,257366925
Fri Sep 12 22:52:33 CDT 2011,65165115,Retweet,55121922
Thu Sep 18 04:34:04 CDT 2011,143248659,Retweet,65165115
Thu Sep 18 23:10:32 CDT 2011,65165115,Mention,230627444
Sat Sep 20 18:49:28 CDT 2011,65165115,Reply,310962238
```
Actions can be:

- Mention
- Reply
- Retweet

Produce a table containing, for each user and for each Sat midnight CDT (Sun 00:00:00 CDT), from the earliest to the latest Saturday present in the dataset, a rolled-up summary of their activity over various time windows ending that midnight.  The columns should be:

- User
- Timestamp (should always be a Sat midnight CDT)
- \# Mentions of Others in Past 7 Days
- \# Mentions of Others in Past 31 Days
- \# Replies in Past 7 Days
- \# Replies in Past 31 Days
- \# Retweets in Past 7 Days
- \# Retweets in Past 31 Days
- Ratio of # Distinct Target Users to # Actions in Past 31 Days (0 if no actions)

So the above table should be transformed into:
```
65165115,Sun Sep  7 00:00:00 CDT 2011,0,0,0,0,0,0,0
65165115,Sun Sep 14 00:00:00 CDT 2011,1,1,0,0,3,3,1.0
65165115,Sun Sep 21 00:00:00 CDT 2011,1,2,1,1,0,3,1.0
143248659,Sun Sep  7 00:00:00 CDT 2011,0,0,0,0,2,2,1.0
143248659,Sun Sep 14 00:00:00 CDT 2011,0,0,0,0,1,3,1.0
143248659,Sun Sep 21 00:00:00 CDT 2011,0,0,0,0,1,4,0.75
```