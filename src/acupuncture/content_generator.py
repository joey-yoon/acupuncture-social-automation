import random
import logging

logger = logging.getLogger(__name__)

class ContentGenerator:
    def __init__(self):
        self.topics = [
            "Benefits of Acupuncture", "Acupoints", "Acupuncture and Stress Relief", 
            "History of Acupuncture", "Acupuncture for Pain Management", 
            "Modern Applications of Acupuncture", "Principles of Oriental Medicine"
        ]
        self.facts = [
            "Acupuncture is a treatment method with thousands of years of history.",
            "Acupuncture activates the body's natural healing abilities.",
            "The World Health Organization (WHO) recognizes acupuncture as an effective treatment.",
            "Acupuncture helps manage various chronic pain conditions.",
            "Acupuncture is effective for stress reduction and relaxation."
        ]
        logger.info("ContentGenerator가 초기화되었습니다.")

    def generate_content(self):
        topic = random.choice(self.topics)
        fact = random.choice(self.facts)
        content = f"Today's Acupuncture Topic: {topic}\n\nDid you know? {fact}"
        logger.info(f"새로운 콘텐츠가 생성되었습니다: {content}")
        return content