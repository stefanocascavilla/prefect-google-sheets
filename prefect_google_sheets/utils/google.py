"""
utils function focus on Google stuff
"""

import json
from typing import Dict, Union

import gspread
from google.oauth2 import service_account

from prefect_google_sheets.exceptions import GoogleSheetServiceAccountError

GOOGLE_CREDENTIALS_SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://spreadsheets.google.com/feeds",
]


def generate_google_credentials(
    google_service_account: Union[Dict, str]
) -> service_account.Credentials:
    """
    Generate the Google credentials based on Service Account information

    Args:
        google_service_account: The service account information

    Raises:
        - GoogleSheetServiceAccountError: If the service account
            format is wrong
        - GoogleSheetServiceAccountError: If the service account
            information are broken or wrong

    Returns: The Google credentials
    """
    if isinstance(google_service_account, dict):
        service_account_dict = google_service_account
    elif isinstance(google_service_account, str):
        service_account_dict = json.loads(google_service_account)
    else:
        exc_message = (
            "Wrong type for the Google Service Account param. Valid ones: dict, str"
        )
        raise GoogleSheetServiceAccountError(exc_message)

    try:
        credentials = service_account.Credentials.from_service_account_info(
            service_account_dict
        ).with_scopes(GOOGLE_CREDENTIALS_SCOPES)
    except ValueError as exc:
        exc_message = f"An error occurred while retrieving Google credentials - {exc}"
        raise GoogleSheetServiceAccountError(exc_message)
    else:
        return credentials


def get_google_sheet_reference(
    is_public_sheet: bool,
    google_service_account: Union[Dict, str],
    google_sheet_key: str,
    google_sheet_name: str,
) -> Union[str, gspread.Spreadsheet]:
    """
    Generate the Google Sheet reference.

    Args:
        is_public_sheet: Whether the Google Sheet is public or not.
            If True, the google_service_account param will be ignored.
        google_service_account: The Service Account to be used
            in order to interact with the Google Sheet.
            This can be a dict or a string representing the JSON
            Service Account body.
        google_sheet_key: The key of the Google Sheet to read data from.
        google_sheet_name: The name of the Sheet to read data from.

    Raises:
        - GoogleSheetServiceAccountError: If the service account
            format is wrong
        - GoogleSheetServiceAccountError: If the service account
            information are broken or wrong

    Returns: The Google credentials
    """

    if is_public_sheet:
        sheet = f"""https://docs.google.com/spreadsheets/d/{google_sheet_key}/
            export?format=csv&sheet={google_sheet_name}"""
    else:
        google_credentials = generate_google_credentials(
            google_service_account=google_service_account
        )
        gspread_client = gspread.authorize(google_credentials)
        sheet = gspread_client.open_by_key(google_sheet_key).worksheet(
            google_sheet_name
        )

    return sheet
