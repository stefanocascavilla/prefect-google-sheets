"""
Exceptions to be used when working with Google Sheets
"""

from gspread.exceptions import GSpreadException


class GoogleSheetsConfigurationException(GSpreadException):
    """
    An exception happened if Google parameters are omitted or wrong.
    """


class GoogleSheetValueError(GSpreadException):
    """
    An exception happened if an error is thrown while working with the sheet.
    """


class GoogleSheetServiceAccountError(GSpreadException):
    """
    An exception happened if an error is thrown while using the service account.
    """


class GoogleSheetClearException(GSpreadException):
    """
    An exception happened while trying to clear a Google Sheet.
    """


class GoogleSheetWriteException(GSpreadException):
    """
    An Exception happened while trying to write on a Google Sheet.
    """
