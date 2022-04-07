import datetime
import unittest

from quickbooks import QuickBooks
from quickbooks.objects.preferences import Preferences


def check_valid_date(date_text):
    try:
      datetime.datetime.strptime(date_text, '%Y-%m-%d')
      return True
    except ValueError:
      raise ValueError("Incorrect data format, should be YYYY-MM-DD")


class PreferencesTests(unittest.TestCase):
    def test_unicode(self):
        preferences = Preferences()

        self.assertEqual(str(preferences), "Preferences")

    def test_valid_date(self):
        preferences = Preferences()
        preferences.BookDateClosed = "2022-04-07"

        self.assertEqual(check_valid_date(preferences.BookDateClosed), True)

    def test_valid_object_name(self):
        obj = Preferences()
        client = QuickBooks()
        result = client.isvalid_object_name(obj.qbo_object_name)

        self.assertTrue(result)