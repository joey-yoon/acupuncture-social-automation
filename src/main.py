from social_media.twitter import TwitterBot
from social_media.facebook import FacebookBot
from social_media.linkedin import LinkedInBot
from social_media.instagram import InstagramBot
from acupuncture.content_generator import ContentGenerator

def main():
    print("침술 소셜 자동화 프로그램을 시작합니다.")
    
    twitter_bot = TwitterBot()
    facebook_bot = FacebookBot()
    linkedin_bot = LinkedInBot()
    instagram_bot = InstagramBot()
    content_gen = ContentGenerator()

    content = content_gen.generate_content()
    twitter_bot.post_tweet(content)
    facebook_bot.post_status(content)
    linkedin_bot.post_update(content)
    instagram_bot.post_photo(content, "https://example.com/acupuncture_image.jpg")  # 예시 URL

if __name__ == "__main__":
    main()