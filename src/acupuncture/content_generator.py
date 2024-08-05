import random

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

    def generate_content(self):
        topic = random.choice(self.topics)
        fact = random.choice(self.facts)
        return f"Today's Acupuncture Topic: {topic}\n\nDid you know? {fact}"