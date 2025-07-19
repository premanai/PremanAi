import unittest
 HEAD


 f5877e6 (Fix import path in test_converter.py)
from converter import flip_image, text_to_pdf

class TestConverter(unittest.TestCase):
    def test_flip_image(self):
        result = flip_image("dummy.jpg")
        self.assertIn("flipped", result.lower())
        self.assertIn("dummy.jpg", result)

    def test_text_to_pdf(self):
        result = text_to_pdf("Ini teks contoh", "output.pdf")
        self.assertIn("pdf saved", result.lower())
        self.assertIn("output.pdf", result)

if __name__ == "__main__":
    unittest.main()
