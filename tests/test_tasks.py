from unittest.mock import Mock

import pandas as pd
import pytest
from prefect import flow

from prefect_google_sheets.exceptions import (
    GoogleSheetsConfigurationException,
    GoogleSheetServiceAccountError,
)
from prefect_google_sheets.tasks import (
    read_google_sheet_as_data_frame,
    read_google_sheet_as_dict_of_lists,
    read_google_sheet_as_list_of_lists,
)

# read_google_sheet_as_data_frame task tests


def test_read_google_sheet_as_data_frame_no_service_account():
    @flow
    def test_flow():
        return read_google_sheet_as_data_frame()

    exc_message = "Missing Google Service Account information."
    with pytest.raises(GoogleSheetsConfigurationException, match=exc_message):
        test_flow()


def test_read_google_sheet_as_data_frame_no_sheet_key():
    @flow
    def test_flow():
        return read_google_sheet_as_data_frame(google_service_account="foo")

    exc_message = "Missing the Google Sheet key identifier."
    with pytest.raises(GoogleSheetsConfigurationException, match=exc_message):
        test_flow()


def test_read_google_sheet_as_data_frame_no_sheet_name():
    @flow
    def test_flow():
        return read_google_sheet_as_data_frame(
            google_service_account="foo", google_sheet_key="bar"
        )

    exc_message = "Missing the Google Sheet name identifier."
    with pytest.raises(GoogleSheetsConfigurationException, match=exc_message):
        test_flow()


def test_read_google_sheet_as_data_frame_public(mocker):
    mocker_sheet_call = mocker.patch("prefect_google_sheets.tasks.get_sheet_dataframe")
    mocker_sheet_call.return_value = "test_call"

    @flow
    def test_flow():
        return read_google_sheet_as_data_frame(
            is_public_sheet=True, google_sheet_key="foo", google_sheet_name="bar"
        )

    result = test_flow()

    assert mocker_sheet_call.called is True
    assert result == "test_call"


def test_read_google_sheet_as_data_frame_private_wrong_sa():
    @flow
    def test_flow():
        return read_google_sheet_as_data_frame(
            is_public_sheet=False,
            google_service_account=["foo"],
            google_sheet_key="foo",
            google_sheet_name="bar",
        )

    exc_message = (
        "Wrong type for the Google Service Account param. Valid ones: dict, str"
    )
    with pytest.raises(GoogleSheetServiceAccountError, match=exc_message):
        test_flow()


def test_read_google_sheet_as_data_frame_private_malformed_credentials(mocker):
    mocker_sheet_call = mocker.patch(
        "google.oauth2.service_account.Credentials.from_service_account_info"
    )
    mocker_sheet_call.side_effect = GoogleSheetServiceAccountError(
        "An error occurred while retrieving Google credentials - generic"
    )

    @flow
    def test_flow():
        return read_google_sheet_as_data_frame(
            is_public_sheet=False,
            google_service_account={"foo": "bar"},
            google_sheet_key="foo",
            google_sheet_name="bar",
        )

    exc_message = "An error occurred while retrieving Google credentials - generic"
    with pytest.raises(GoogleSheetServiceAccountError, match=exc_message):
        test_flow()


def test_read_google_sheet_as_data_frame_private(mocker):
    mocker_google_credentials_call = mocker.patch(
        "prefect_google_sheets.tasks.generate_google_credentials"
    )
    mocker_google_credentials_call.return_value = ""

    mocker_gspread_authorize_call = mocker.patch(
        "prefect_google_sheets.tasks.gspread.authorize"
    )
    mocker_gspread_authorize_call.return_value = Mock()

    mocker_sheet_call = mocker.patch("prefect_google_sheets.tasks.get_sheet_dataframe")
    mocker_sheet_call.return_value = "test_call"

    @flow
    def test_flow():
        return read_google_sheet_as_data_frame(
            is_public_sheet=False,
            google_service_account={"correct": "credentials"},
            google_sheet_key="foo",
            google_sheet_name="bar",
        )

    result = test_flow()

    assert mocker_sheet_call.called is True
    assert result == "test_call"


# read_google_sheet_as_list_of_lists task tests


def test_read_google_sheet_as_list_of_lists_no_service_account():
    @flow
    def test_flow():
        return read_google_sheet_as_list_of_lists()

    exc_message = "Missing Google Service Account information."
    with pytest.raises(GoogleSheetsConfigurationException, match=exc_message):
        test_flow()


def test_read_google_sheet_as_list_of_lists_no_sheet_key():
    @flow
    def test_flow():
        return read_google_sheet_as_list_of_lists(google_service_account="foo")

    exc_message = "Missing the Google Sheet key identifier."
    with pytest.raises(GoogleSheetsConfigurationException, match=exc_message):
        test_flow()


def test_read_google_sheet_as_list_of_lists_no_sheet_name():
    @flow
    def test_flow():
        return read_google_sheet_as_list_of_lists(
            google_service_account="foo", google_sheet_key="bar"
        )

    exc_message = "Missing the Google Sheet name identifier."
    with pytest.raises(GoogleSheetsConfigurationException, match=exc_message):
        test_flow()


def test_read_google_sheet_as_list_of_lists_public(mocker):
    mocker_sheet_call = mocker.patch("prefect_google_sheets.tasks.get_sheet_dataframe")
    mocker_sheet_call.return_value = pd.DataFrame(data=["foo", "bar"])

    @flow
    def test_flow():
        return read_google_sheet_as_list_of_lists(
            is_public_sheet=True, google_sheet_key="foo", google_sheet_name="bar"
        )

    result = test_flow()

    assert mocker_sheet_call.called is True
    assert result == [["foo"], ["bar"]]


def test_read_google_sheet_as_list_of_lists_private_wrong_sa():
    @flow
    def test_flow():
        return read_google_sheet_as_list_of_lists(
            is_public_sheet=False,
            google_service_account=["foo"],
            google_sheet_key="foo",
            google_sheet_name="bar",
        )

    exc_message = (
        "Wrong type for the Google Service Account param. Valid ones: dict, str"
    )
    with pytest.raises(GoogleSheetServiceAccountError, match=exc_message):
        test_flow()


def test_read_google_sheet_as_list_of_lists_private_malformed_credentials(mocker):
    mocker_sheet_call = mocker.patch(
        "google.oauth2.service_account.Credentials.from_service_account_info"
    )
    mocker_sheet_call.side_effect = GoogleSheetServiceAccountError(
        "An error occurred while retrieving Google credentials - generic"
    )

    @flow
    def test_flow():
        return read_google_sheet_as_list_of_lists(
            is_public_sheet=False,
            google_service_account={"foo": "bar"},
            google_sheet_key="foo",
            google_sheet_name="bar",
        )

    exc_message = "An error occurred while retrieving Google credentials - generic"
    with pytest.raises(GoogleSheetServiceAccountError, match=exc_message):
        test_flow()


def test_read_google_sheet_as_list_of_lists_private(mocker):
    mocker_google_credentials_call = mocker.patch(
        "prefect_google_sheets.tasks.generate_google_credentials"
    )
    mocker_google_credentials_call.return_value = ""

    mocker_gspread_authorize_call = mocker.patch(
        "prefect_google_sheets.tasks.gspread.authorize"
    )
    mocker_gspread_authorize_call.return_value = Mock()

    mocker_sheet_call = mocker.patch("prefect_google_sheets.tasks.get_sheet_dataframe")
    mocker_sheet_call.return_value = pd.DataFrame(data=["foo", "bar"])

    @flow
    def test_flow():
        return read_google_sheet_as_list_of_lists(
            is_public_sheet=False,
            google_service_account={"correct": "credentials"},
            google_sheet_key="foo",
            google_sheet_name="bar",
        )

    result = test_flow()

    assert mocker_sheet_call.called is True
    assert result == [["foo"], ["bar"]]


# read_google_sheet_as_dict_of_lists task tests


def test_read_google_sheet_as_dict_of_lists_no_service_account():
    @flow
    def test_flow():
        return read_google_sheet_as_dict_of_lists()

    exc_message = "Missing Google Service Account information."
    with pytest.raises(GoogleSheetsConfigurationException, match=exc_message):
        test_flow()


def test_read_google_sheet_as_dict_of_lists_no_sheet_key():
    @flow
    def test_flow():
        return read_google_sheet_as_dict_of_lists(google_service_account="foo")

    exc_message = "Missing the Google Sheet key identifier."
    with pytest.raises(GoogleSheetsConfigurationException, match=exc_message):
        test_flow()


def test_read_google_sheet_as_dict_of_lists_no_sheet_name():
    @flow
    def test_flow():
        return read_google_sheet_as_dict_of_lists(
            google_service_account="foo", google_sheet_key="bar"
        )

    exc_message = "Missing the Google Sheet name identifier."
    with pytest.raises(GoogleSheetsConfigurationException, match=exc_message):
        test_flow()


def test_read_google_sheet_as_dict_of_lists_public(mocker):
    mocker_sheet_call = mocker.patch("prefect_google_sheets.tasks.get_sheet_dataframe")
    mocker_sheet_call.return_value = pd.DataFrame(
        columns=["col_1", "col_2"], data={"col_1": ["foo"], "col_2": ["bar"]}
    )

    @flow
    def test_flow():
        return read_google_sheet_as_dict_of_lists(
            is_public_sheet=True, google_sheet_key="foo", google_sheet_name="bar"
        )

    result = test_flow()

    assert mocker_sheet_call.called is True
    assert result == {"col_1": ["foo"], "col_2": ["bar"]}


def test_read_google_sheet_as_dict_of_lists_private_wrong_sa():
    @flow
    def test_flow():
        return read_google_sheet_as_dict_of_lists(
            is_public_sheet=False,
            google_service_account=["foo"],
            google_sheet_key="foo",
            google_sheet_name="bar",
        )

    exc_message = (
        "Wrong type for the Google Service Account param. Valid ones: dict, str"
    )
    with pytest.raises(GoogleSheetServiceAccountError, match=exc_message):
        test_flow()


def test_read_google_sheet_as_dict_of_lists_private_malformed_credentials(mocker):
    mocker_sheet_call = mocker.patch(
        "google.oauth2.service_account.Credentials.from_service_account_info"
    )
    mocker_sheet_call.side_effect = GoogleSheetServiceAccountError(
        "An error occurred while retrieving Google credentials - generic"
    )

    @flow
    def test_flow():
        return read_google_sheet_as_dict_of_lists(
            is_public_sheet=False,
            google_service_account={"foo": "bar"},
            google_sheet_key="foo",
            google_sheet_name="bar",
        )

    exc_message = "An error occurred while retrieving Google credentials - generic"
    with pytest.raises(GoogleSheetServiceAccountError, match=exc_message):
        test_flow()


def test_read_google_sheet_as_dict_of_lists_private(mocker):
    mocker_google_credentials_call = mocker.patch(
        "prefect_google_sheets.tasks.generate_google_credentials"
    )
    mocker_google_credentials_call.return_value = ""

    mocker_gspread_authorize_call = mocker.patch(
        "prefect_google_sheets.tasks.gspread.authorize"
    )
    mocker_gspread_authorize_call.return_value = Mock()

    mocker_sheet_call = mocker.patch("prefect_google_sheets.tasks.get_sheet_dataframe")
    mocker_sheet_call.return_value = pd.DataFrame(
        columns=["col_1", "col_2"], data={"col_1": ["foo"], "col_2": ["bar"]}
    )

    @flow
    def test_flow():
        return read_google_sheet_as_dict_of_lists(
            is_public_sheet=False,
            google_service_account={"correct": "credentials"},
            google_sheet_key="foo",
            google_sheet_name="bar",
        )

    result = test_flow()

    assert mocker_sheet_call.called is True
    assert result == {"col_1": ["foo"], "col_2": ["bar"]}
