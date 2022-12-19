"""
utils function focus on dataframes
"""

from typing import Union

from gspread.worksheet import Worksheet
from gspread_dataframe import get_as_dataframe
from pandas import DataFrame, read_csv

from prefect_google_sheets.exceptions import GoogleSheetValueError


def get_sheet_dataframe(
    google_sheet: Union[Worksheet, str],
    header: int,
    parse_dates: bool,
    on_bad_lines: str,
    clean: bool,
) -> DataFrame:
    """
    Read the content of a Google Sheet.

    Args:
        - google_sheet: The google sheet reference
        - header: The row representing the header of the sheet
        - parse_dates: Whether to parse dates as date obj or not
        - ob_bad_lines: What to do if bad rows are detected
        - clean: Whether to remove blank columns/rows if any

    Raises:
        - GoogleSheetValueError: If an exception is thrown
            while reading the Google Sheet

    Return: The Google Sheet content as a pandas DataFrame
    """
    try:
        if isinstance(google_sheet, Worksheet):
            sheet_df = get_as_dataframe(
                google_sheet,
                header=header,
                parse_dates=parse_dates,
                on_bad_lines=on_bad_lines,
            )
        else:
            sheet_df = read_csv(
                google_sheet,
                header=header,
                parse_dates=parse_dates,
                on_bad_lines=on_bad_lines,
            )
    except Exception as exc:
        exc_message = f"Error while reading the Sheet - {exc}"
        raise GoogleSheetValueError(exc_message)
    else:
        if clean:
            sheet_df.dropna(inplace=True, axis=1, how="all")
            sheet_df.dropna(inplace=True, axis=0, how="all")
        return sheet_df
