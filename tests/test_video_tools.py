import unittest
from src.video_tools import video_to_audio, video_to_images, video_to_prompt_text

class TestVideoTools(unittest.TestCase):
    def setUp(self):
        self.video_path = "sample_video.mp4"
        self.video_title = "Epic Volcano Eruption"

    def test_video_to_audio(self):
        result = video_to_audio(self.video_path)
        self.assertIn(self.video_path, result)
        self.assertTrue(result.startswith("Audio extracted"))

    def test_video_to_images(self):
        results = video_to_images(self.video_path)
        self.assertIsInstance(results, list)
        self.assertTrue(all(self.video_path in img for img in results))

    def test_video_to_prompt_text(self):
        result = video_to_prompt_text(self.video_title)
        self.assertIn(self.video_title, result)
        self.assertTrue(result.startswith("Detailed cinematic prompt"))

if __name__ == "__main__":
    unittest.main()
