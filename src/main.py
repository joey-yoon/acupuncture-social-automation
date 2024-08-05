import logging
import os

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='acupuncture_social_automation.log'
)
logger = logging.getLogger(__name__)

import os
from social_media.twitter import TwitterBot
from social_media.facebook import FacebookBot
from social_media.linkedin import LinkedInBot
from social_media.instagram import InstagramBot
from acupuncture.content_generator import ContentGenerator

def main():
    logger.info("침술 소셜 자동화 프로그램을 시작합니다.")
    
    try:
        twitter_bot = TwitterBot(
            os.getenv('TWITTER_API_KEY'),
            os.getenv('TWITTER_API_SECRET'),
            os.getenv('TWITTER_ACCESS_TOKEN'),
            os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        )
        facebook_bot = FacebookBot()
        linkedin_bot = LinkedInBot()
        instagram_bot = InstagramBot()
        content_gen = ContentGenerator()

        content = content_gen.generate_content()
        logger.info(f"생성된 콘텐츠: {content}")

        try:
            twitter_bot.post_tweet(content)
        except Exception as e:
            logger.error(f"Twitter 게시 중 오류 발생: {str(e)}")

        try:
            facebook_bot.post_status(content)
        except Exception as e:
            logger.error(f"Facebook 게시 중 오류 발생: {str(e)}")

        try:
            linkedin_bot.post_update(content)
        except Exception as e:
            logger.error(f"LinkedIn 게시 중 오류 발생: {str(e)}")

        try:
            instagram_bot.post_photo(content, "https://example.com/acupuncture_image.jpg")
        except Exception as e:
            logger.error(f"Instagram 게시 중 오류 발생: {str(e)}")

    except Exception as e:
        logger.error(f"프로그램 실행 중 오류 발생: {str(e)}")
    else:
        logger.info("모든 소셜 미디어 게시가 완료되었습니다.")

if __name__ == "__main__":
    main()