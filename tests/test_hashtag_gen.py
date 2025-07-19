import unittest
from src.hashtag_gen import (
    generate_normal_hashtags,
    generate_absurd_hashtags,
    generate_seo_friendly_hashtags,
    generate_auto_scan_video_hashtags,
)

class TestHashtagGen(unittest.TestCase):
    def setUp(self):
        self.topic = "PremanAi"
        self.video_title = "Epic Disaster Video"

    def test_generate_normal_hashtags(self):
        tags = generate_normal_hashtags(self.topic)
        self.assertTrue(all(self.topic in tag for tag in tags))

    def test_generate_absurd_hashtags(self):
        tags = generate_absurd_hashtags(self.topic)
        self.assertTrue(all(self.topic in tag for tag in tags))

    def test_generate_seo_friendly_hashtags(self):
        tags = generate_seo_friendly_hashtags(self.topic)
        self.assertTrue(any("Tutorial" in tag or "Tips" in tag for tag in tags))

    def test_generate_auto_scan_video_hashtags(self):
        tags = generate_auto_scan_video_hashtags(self.video_title)
        base = self.video_title.lower().replace(" ", "")
        self.assertTrue(all(base in tag for tag in tags))

if __name__ == "__main__":
    unittest.main()
