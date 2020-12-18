# Twitter_Scanning
search a user's tweets for alarming language

## Introduction
My idea for this project stemmed from a paper that I wrote two years ago in a class, Seminar in Science Writing. I discussed how there were algorithms to tell if someone was depressed or suffering from other mental illnesses based on their social media posts. This looked for certain filters on pictures, smiling faces, and words used in captions or tweets. Using tweepy and what I have learned about python, this seemed like a great opportunity to put some of that research to use and mix it with my coding knowledge. 322 million people worldwide live with depression and the use of social media starting at a young age is making that number grow even more.

## Get Started
Add your twitter credentials to access the API
```python
CONSUMER_KEY = 
CONSUMER_KEY_SECRET = 
ACCESS_TOKEN = 
ACCESS_TOKEN_SECRET =
```
Fill in the bottom line with a username and file name to start your scan
```python
t.user_search(user='username',csv_prefix='filename')
```

## Output
This will tell you how many tweets were analyzed, how many had alarming words, and how many could not be scanned. The percent of alarming tweets is displayed and if that percent is greater that 10%, you will get a message that the user is "At-Risk"
```python
analyzing tweets for user:  username ...
4 out of 109 were flagged as alarming language
=  3.669724770642202 %
0 tweets were unable to be scanned
```
