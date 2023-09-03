import unittest
from src.notifier.desktop_notifier import send_notification


class TestDesktopNotifier(unittest.TestCase):
    def test_send_notification(self):
        # Basic test to see if the function executes without errors
        try:
            send_notification("Test Title", "Test Message")
            success = True
        except:
            success = False
        self.assertTrue(success)
