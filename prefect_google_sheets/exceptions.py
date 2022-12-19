"""
Exceptions to be used when working with Google Sheets
"""


class GoogleSheetsConfigurationException(Exception):
    """
    An exception happened if Google parameters are omitted or wrong.
    """


class GoogleSheetValueError(Exception):
    """
    An exception happened if an error is thrown while working with the sheet.
    """


class GoogleSheetServiceAccountError(Exception):
    """
    An exception happened if an error is thrown while using the service account.
    """
