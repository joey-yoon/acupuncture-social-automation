import random

class ContentGenerator:
    def __init__(self):
        self.topics = ["침술의 장점", "경혈점", "침술과 스트레스 해소", "침술의 역사"]

    def generate_content(self):
        topic = random.choice(self.topics)
        return f"오늘의 침술 주제: {topic}"