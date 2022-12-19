"""
utils function focus on Google stuff
"""

import json
from typing import Dict, Union

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
        - google_service_account: The service account information

    Raises:
        - GoogleSheetServiceAccountError: If the service account
            format is wrong
        - GoogleSheetServiceAccountError: If the service account
            information are broken or wrong

    Return: The Google credentials
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
