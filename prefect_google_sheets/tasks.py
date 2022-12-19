"""
prefect-google-sheets tasks
"""

from typing import Dict, List, Optional, Union

import gspread
from pandas import DataFrame
from prefect import task

from prefect_google_sheets.exceptions import GoogleSheetsConfigurationException
from prefect_google_sheets.utils.dataframe import get_sheet_dataframe
from prefect_google_sheets.utils.google import generate_google_credentials


@task
def read_google_sheet_as_data_frame(
    is_public_sheet: bool = False,
    google_service_account: Union[Dict, str] = None,
    google_sheet_key: Optional[str] = None,
    google_sheet_name: Optional[str] = None,
    first_row_header: Optional[bool] = True,
    on_bad_lines: Optional[str] = "error",
    clean: Optional[bool] = False,
) -> DataFrame:
    """
    This task leverages the Google Sheets API v4 through the gspread library
    in order to read the content of a Google Sheet and return it as a pandas Dataframe.
    Args:
        is_public_sheet: Whether the Google Sheet is public or not.
            If True, the google_service_account param will be ignored.
        google_service_account: The Service Account to be used
            in order to interact with the Google Sheet.
            This can be a dict or a string representing the JSON
            Service Account body.
        google_sheet_key: The key of the Google Sheet to read data from.
        google_sheet_name: The name of the Sheet to read data from.
        first_row_header: Whether the first row is the header.
            If True, the first row will be used as header and data won't
            be read. Otherwise, if set to False. Default set to True
        on_bad_lines: What to do if bad lines are discovered:
            'error': An Exception is raised
            'warn': A warning is printed and the line  is skipped
            'skip': The line is skipped with no warnings
            Default set to 'error'
        clean: Used in order to remove blank columns and rows left
            in the Google Sheet.
    Raises:
        - `GoogleSheetsConfigurationException`
            if google_service_account not provided or None
        - `GoogleSheetsConfigurationException`
            if google_sheet_key not provided or None
        - `GoogleSheetsConfigurationException`
            if google_sheet_name not provided or None
        - `GoogleSheetServiceAccountError`
            if the google_service_account is not valid or malformed
    Returns:
        The content of a specific Sheet as a pandas dataframe.
    """

    if not is_public_sheet and not google_service_account:
        exc_message = "Missing Google Service Account information."
        raise GoogleSheetsConfigurationException(exc_message)

    if not google_sheet_key:
        exc_message = "Missing the Google Sheet key identifier."
        raise GoogleSheetsConfigurationException(exc_message)

    if not google_sheet_name:
        exc_message = "Missing the Google Sheet name identifier."
        raise GoogleSheetsConfigurationException(exc_message)

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

    sheet_df = get_sheet_dataframe(
        sheet,
        header=0 if first_row_header is True else None,
        parse_dates=True,
        on_bad_lines=on_bad_lines,
        clean=clean,
    )
    return sheet_df


@task
def read_google_sheet_as_list_of_lists(
    is_public_sheet: bool = False,
    google_service_account: Union[Dict, str] = None,
    google_sheet_key: Optional[str] = None,
    google_sheet_name: Optional[str] = None,
    first_row_header: Optional[bool] = True,
    on_bad_lines: Optional[str] = "error",
    clean: Optional[bool] = False,
) -> List[List]:
    """
    This task leverages the Google Sheets API v4 through the gspread library
    in order to read the content of a Google Sheet and return it as a list of lists.
    Args:
        is_public_sheet: Whether the Google Sheet is public or not.
            If True, the google_service_account param will be ignored.
        google_service_account: The Service Account to be used in order to interact with
            the Google Sheet. This can be a dict or a string representing the JSON
            Service Account body.
        google_sheet_key: The key of the Google Sheet to read data from.
        google_sheet_name: The name of the Sheet to read data from.
        first_row_header: Whether the first row is the header.
            If True, the first row will be used as header and data won't be read.
            Otherwise, if set to False. Default set to True
        on_bad_lines: What to do if bad lines are discovered:
            'error': An Exception is raised
            'warn': A warning is printed and the line  is skipped
            'skip': The line is skipped with no warnings
            Default set to 'error'
        clean: Used in order to remove blank columns and rows left in the Google Sheet.
    Raises:
        - `GoogleSheetsConfigurationException`
            if google_service_account not provided or None
        - `GoogleSheetsConfigurationException`
            if google_sheet_key not provided or None
        - `GoogleSheetsConfigurationException`
            if google_sheet_name not provided or None
        - `GoogleSheetServiceAccountError`
            if the google_service_account is not valid or malformed
    Returns:
        The content of a specific Sheet as a list of lists.
    """

    if not is_public_sheet and not google_service_account:
        exc_message = "Missing Google Service Account information."
        raise GoogleSheetsConfigurationException(exc_message)

    if not google_sheet_key:
        exc_message = "Missing the Google Sheet key identifier."
        raise GoogleSheetsConfigurationException(exc_message)

    if not google_sheet_name:
        exc_message = "Missing the Google Sheet name identifier."
        raise GoogleSheetsConfigurationException(exc_message)

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

    sheet_df = get_sheet_dataframe(
        sheet,
        header=0 if first_row_header is True else None,
        parse_dates=True,
        on_bad_lines=on_bad_lines,
        clean=clean,
    )
    return sheet_df.values.tolist()


@task
def read_google_sheet_as_dict_of_lists(
    is_public_sheet: bool = False,
    google_service_account: Union[Dict, str] = None,
    google_sheet_key: Optional[str] = None,
    google_sheet_name: Optional[str] = None,
    first_row_header: Optional[bool] = True,
    on_bad_lines: Optional[str] = "error",
    clean: Optional[bool] = False,
) -> List[Dict]:
    """
    This task leverages the Google Sheets API v4 through the gspread library
    in order to read the content of a Google Sheet and return it as a dict of lists.
    Args:
        is_public_sheet: Whether the Google Sheet is public or not.
            If True, the google_service_account param will be ignored.
        google_service_account: The Service Account to be used in order to interact with
            the Google Sheet. This can be a dict or a string representing the JSON
            Service Account body.
        google_sheet_key: The key of the Google Sheet to read data from.
        google_sheet_name: The name of the Sheet to read data from.
        first_row_header: Whether the first row is the header.
            If True, the first row will be used as header and data won't be read.
            Otherwise, if set to False. Default set to True
        on_bad_lines: What to do if bad lines are discovered:
            'error': An Exception is raised
            'warn': A warning is printed and the line  is skipped
            'skip': The line is skipped with no warnings
            Default set to 'error'
        clean: Used in order to remove blank columns and rows left in the Google Sheet.
    Raises:
        - `GoogleSheetsConfigurationException`
            if google_service_account not provided or None
        - `GoogleSheetsConfigurationException`
            if google_sheet_key not provided or None
        - `GoogleSheetsConfigurationException`
            if google_sheet_name not provided or None
        - `GoogleSheetServiceAccountError`
            if the google_service_account is not valid or malformed
    Returns:
        The content of a specific Sheet as a dict of lists.
    """

    if not is_public_sheet and not google_service_account:
        exc_message = "Missing Google Service Account information."
        raise GoogleSheetsConfigurationException(exc_message)

    if not google_sheet_key:
        exc_message = "Missing the Google Sheet key identifier."
        raise GoogleSheetsConfigurationException(exc_message)

    if not google_sheet_name:
        exc_message = "Missing the Google Sheet name identifier."
        raise GoogleSheetsConfigurationException(exc_message)

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

    sheet_df = get_sheet_dataframe(
        sheet,
        header=0 if first_row_header is True else None,
        parse_dates=True,
        on_bad_lines=on_bad_lines,
        clean=clean,
    )
    return {
        column_name: sheet_df[column_name].values.tolist()
        for column_name in sheet_df.columns.values
    }
