##### Q: How do I use this?

Personally, I:
1. Open "twitter_activity_log_processor.py" in SublimeText2,
2. Scroll down to "main()" and change the filename I want to process,
3. Then hit "Ctrl+B" to run it.


##### Q: How long would it take to process the entire tweets.csv file?

The first 5000 rows / tweets are 273kb.

It took 21.7s to process the first 5000.

The full tweets.csv file is 1,560,129kb.

In other words, it's ~5714 times as big as the first 5000 tweets.

Thus, I estimate tweets.csv will take at least 5714 times as long to process as the first 5000.

Thus, I estimate it will take more than 35 hours to process tweets.csv.