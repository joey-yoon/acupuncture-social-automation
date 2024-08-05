import tweepy
import logging

logger = logging.getLogger(__name__)

class TwitterBot:
    def __init__(self, api_key, api_secret, access_token, access_token_secret):
        try:
            auth = tweepy.OAuthHandler(api_key, api_secret)
            auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(auth)
            logger.info("Twitter 봇이 초기화되었습니다.")
        except Exception as e:
            logger.error(f"Twitter 봇 초기화 중 오류 발생: {str(e)}")
            raise

    def post_tweet(self, message):
        try:
            self.api.update_status(message)
            logger.info(f"트윗 게시 성공: {message}")
        except tweepy.TweepError as e:
            logger.error(f"트윗 게시 실패: {str(e)}")
            raise