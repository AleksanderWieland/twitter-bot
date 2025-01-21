import tweepy
import os
from dotenv import load_dotenv



# create an OAuthHandler instance


# create a tweet
def send_tweet(text):
    try:
        # credentials to access Twitter API
        API_KEY= os.getenv("API_KEY")
        API_KEY_SECRET=os.getenv("API_KEY_SECRET")
        BEARER_TOKEN=os.getenv("BEARER_TOKEN")
        ACCESS_TOKEN=os.getenv("ACCESS_TOKEN")
        ACCESS_TOKEN_SECRET=os.getenv("ACCESS_TOKEN_SECRET")
        client = tweepy.Client(
        BEARER_TOKEN,
        API_KEY,
        API_KEY_SECRET,
        ACCESS_TOKEN,
        ACCESS_TOKEN_SECRET
        )
        client.create_tweet(text=str(text))
        print(text)
        print("Tweet has been published.")
    except tweepy.errors.Forbidden as e:
        # Check if the error is related to duplicate tweets
        if "You are not allowed to create a Tweet with duplicate content" in str(e):
            print("Error: Duplicate tweet. You cannot send the same tweet twice.")
        else:
            # Other Forbidden errors
            print(f"A Forbidden error occurred: {e}")
    except Exception as e:
        # Handle other exceptions
        print(f"Another error occurred: {e}")
