import datetime
import pytest
import unittest

from quickbooks import QuickBooks
from quickbooks.objects.preferences import Preferences


def check_valid_date(date_text):
    try:
      datetime.datetime.strptime(date_text, '%Y-%m-%d')
      return True
    except ValueError:
      raise ValueError("Incorrect data format, should be YYYY-MM-DD")


def test_unicode():
    preferences = Preferences()

    assert str(preferences) == "Preferences"


def test_valid_date():
    preferences = Preferences()
    preferences.BookDateClosed = "2022-04-07"

    assert check_valid_date(preferences.BookDateClosed) == True

    with pytest.raises(ValueError):
        check_valid_date("2022-04-07 10:46:32 AM")


def test_valid_object_name():
    obj = Preferences()
    client = QuickBooks()
    result = client.isvalid_object_name(obj.qbo_object_name)

    assert result == True
