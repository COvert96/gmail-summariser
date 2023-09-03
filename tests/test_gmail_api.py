import unittest
from src.email_fetcher.gmail_api import fetch_emails_from_last_n_hours


class TestGmailAPI(unittest.TestCase):
    def test_fetch_emails_from_last_n_hours(self):
        # As this function interacts with external service,
        # it's more of an integration test than a unit test.
        # Mocking might be a better approach for pure unit test.
        emails = fetch_emails_from_last_n_hours(1)  # Fetching for the last 1 hour for quickness
        self.assertIsInstance(emails, list)  # Ensure it's a list

        # Additional tests can be added based on expected email format/content.
