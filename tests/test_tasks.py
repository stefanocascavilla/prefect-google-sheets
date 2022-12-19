from prefect import flow

from prefect_google_sheets.tasks import (
    goodbye_prefect_google_sheets,
    hello_prefect_google_sheets,
)


def test_hello_prefect_google_sheets():
    @flow
    def test_flow():
        return hello_prefect_google_sheets()

    result = test_flow()
    assert result == "Hello, prefect-google-sheets!"


def goodbye_hello_prefect_google_sheets():
    @flow
    def test_flow():
        return goodbye_prefect_google_sheets()

    result = test_flow()
    assert result == "Goodbye, prefect-google-sheets!"
