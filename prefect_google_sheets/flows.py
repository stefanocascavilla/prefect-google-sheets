"""This is an example flows module"""
from prefect import flow

from prefect_google_sheets.blocks import GooglesheetsBlock
from prefect_google_sheets.tasks import (
    goodbye_prefect_google_sheets,
    hello_prefect_google_sheets,
)


@flow
def hello_and_goodbye():
    """
    Sample flow that says hello and goodbye!
    """
    GooglesheetsBlock.seed_value_for_example()
    block = GooglesheetsBlock.load("sample-block")

    print(hello_prefect_google_sheets())
    print(f"The block's value: {block.value}")
    print(goodbye_prefect_google_sheets())
    return "Done"


if __name__ == "__main__":
    hello_and_goodbye()
