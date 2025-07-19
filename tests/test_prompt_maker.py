import unittest
from src.prompt_maker import prompt_text_to_image

class TestPromptMaker(unittest.TestCase):
    def test_prompt_text_to_image(self):
        result = prompt_text_to_image("test")
        self.assertIn("test", result)
        self.assertTrue(result.startswith("Generate a hyper-realistic image"))

if __name__ == "__main__":
    unittest.main()
