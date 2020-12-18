import tweepy
import numpy
import csv

### AUTHENTICATOIN KEYS: remove before pushing to github ###


#use to search tweets by keyword or user
class Search():
    
    def __init__(self,myApi,sApi,at,sAt):
        self.tweepy = tweepy
        auth = tweepy.OAuthHandler(myApi, sApi)
        auth.set_access_token(at, sAt)
        self.api = tweepy.API(auth)
        
    # removing non ASCII characters    
    def strip_non_ascii(self,string):
        stripped = (c for c in string if 0 < ord(c) < 127)
        return ''.join(stripped)

    #selecting all the user's tweets    
    def user_search(self,user,csv_prefix):
        API_results = self.tweepy.Cursor(self.api.user_timeline,id=user,tweet_mode='extended').items()
        print("analyzing tweets for user: ", user, "...")
        with open(f'{csv_prefix}.csv', 'w', newline='') as csvfile:
            fieldnames = ['tweet_text', 'date', 'word', 'retweet_count']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            alert_words = ['lonely', 'alone', 'ugly', 'die', 'kill myself', 'sucks', 'hate', 'starving', 'skinny']
            counter = 0
            tweets = 0
            errors = 0
            for tweet in API_results:
                tweets += 1
                text = self.strip_non_ascii(tweet.full_text)
                date = tweet.created_at.strftime('%m/%d/%Y') 
                #looking through the tweets and finding which ones have negative keywords 
                for word in alert_words:
                    if word in text:
                        counter += 1
                        #print(word)
                        try:      
                            writer.writerow({
                                            #'tweet_id': tweet.id_str,
                                            'tweet_text': text,
                                            'date': date,
                                            #'user_id': tweet.user.id_str,
                                            'word': word,
                                            'retweet_count': tweet.retweet_count
                                            })
                        except UnicodeEncodeError:
                            print(" ")
                            errors += 1
            print(counter , 'out of' , tweets , 'were flagged as alarming language')
            ratio = counter / tweets
            print(ratio)
            if ratio > 0.1:
                print('This account has been labeled as At-Risk')
            print(errors, 'tweets were unable to be scanned')
           

t = Search(
    myApi = CONSUMER_KEY,
    sApi = CONSUMER_KEY_SECRET,
    at = ACCESS_TOKEN,
    sAt = ACCESS_TOKEN_SECRET)


t.user_search(user='username',csv_prefix='filename')