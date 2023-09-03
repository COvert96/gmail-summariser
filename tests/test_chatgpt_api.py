import unittest
from src.summariser.chatgpt_api import summarise_text


class TestChatGPTAPI(unittest.TestCase):
    def test_summarize_text(self):
        # As this function interacts with external service,
        # Mocking might be a better approach for pure unit test.
        text = "This is a simple text for summarization, this should be used as a test for summarising a medium sized " \
               "amount of text. "
        summary = summarise_text(text)
        self.assertIsInstance(summary, str)
        self.assertTrue(len(summary) <= len(text))  # Ensure it's a summary and shorter in length.
