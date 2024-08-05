import tweepy

class TwitterBot:
    def __init__(self, api_key, api_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)
        print("Twitter 봇을 초기화합니다.")

    def post_tweet(self, message):
        try:
            self.api.update_status(message)
            print(f"트윗 게시 성공: {message}")
        except tweepy.TweepError as e:
            print(f"트윗 게시 실패: {e}")