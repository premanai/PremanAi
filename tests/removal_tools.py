import unittest
from src.removal_tools import remove_background, remove_watermark

class TestRemovalTools(unittest.TestCase):
    def test_remove_background(self):
        result = remove_background("image_with_bg.jpg")
        self.assertIn("Background removed", result)
        self.assertIn("image_with_bg.jpg", result)

    def test_remove_watermark(self):
        result = remove_watermark("watermarked_image.jpg")
        self.assertIn("Watermark removed", result)
        self.assertIn("watermarked_image.jpg", result)

if __name__ == "__main__":
    unittest.main()
