import tweepy
from config import BOT_USERNAME
from utils.twitter_client import create_twitter_client, reply_to_tweet
from utils.ai_agent import ask_ai

api = create_twitter_client()

class MentionListener(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        if BOT_USERNAME.lower() in tweet.text.lower():
            print(f"New mention: {tweet.text}")
            answer = ask_ai(tweet.text)
            reply_to_tweet(api, tweet.id, answer)
            print(f"Replied with: {answer}")

def main():
    print("Xpumpit Bot is running...")
    # Streaming mentions
    listener = MentionListener(bearer_token="YOUR_BEARER_TOKEN")
    listener.add_rules(tweepy.StreamRule(f"@{BOT_USERNAME}"))
    listener.filter()

if __name__ == "__main__":
    main()
