# prefect-google-sheets

<p align="center">
    <a href="https://pypi.python.org/pypi/prefect-google-sheets/" alt="PyPI version">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/prefect-google-sheets?color=0052FF&labelColor=090422"></a>
    <a href="https://github.com/stefanocascavilla/prefect-google-sheets/" alt="Stars">
        <img src="https://img.shields.io/github/stars/stefanocascavilla/prefect-google-sheets?color=0052FF&labelColor=090422" /></a>
    <a href="https://pepy.tech/badge/prefect-google-sheets/" alt="Downloads">
        <img src="https://img.shields.io/pypi/dm/prefect-google-sheets?color=0052FF&labelColor=090422" /></a>
    <a href="https://github.com/stefanocascavilla/prefect-google-sheets/pulse" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/m/stefanocascavilla/prefect-google-sheets?color=0052FF&labelColor=090422" /></a>
    <br>
    <a href="https://prefect-community.slack.com" alt="Slack">
        <img src="https://img.shields.io/badge/slack-join_community-red.svg?color=0052FF&labelColor=090422&logo=slack" /></a>
    <a href="https://discourse.prefect.io/" alt="Discourse">
        <img src="https://img.shields.io/badge/discourse-browse_forum-red.svg?color=0052FF&labelColor=090422&logo=discourse" /></a>
</p>

## Welcome!

Prefect collection of tasks in order to work with Google Sheets

## Getting Started

### Python setup

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `prefect-google-sheets` with `pip`:

```bash
pip install prefect-google-sheets
```

Then, register to [view the block](https://orion-docs.prefect.io/ui/blocks/) on Prefect Cloud:

```bash
prefect block register -m prefect_google_sheets
```

Note, to use the `load` method on Blocks, you must already have a block document [saved through code](https://orion-docs.prefect.io/concepts/blocks/#saving-blocks) or [saved through the UI](https://orion-docs.prefect.io/ui/blocks/).

### Write and run a flow

```python
from prefect import flow
from prefect_google_sheets.tasks import (
    read_google_sheet_as_data_frame,
    read_google_sheet_as_list_of_lists,
    read_google_sheet_as_dict_of_lists,
)


@flow
def read_sheets():
    sheet_df = read_google_sheet_as_data_frame(
        is_public_sheet="<True or False, depending if the sheet you are reading is public or not>",
        google_service_account="<The Google Service Account information in order to access the sheet>",
        google_sheet_key="<The key of the sheet to read>",
        google_sheet_name="<The name of the sheet to read>",
        first_row_header="<True or False, depending if the first row of the table needs to be considered as the header>",
        on_bad_lines="<What to do if bad lines are discovered while reading the sheet>",
        clean="<True or False, depending if blank columns and rows need to be removed>"
    )

    sheet_list_of_lists = read_google_sheet_as_list_of_lists(
        is_public_sheet="<True or False, depending if the sheet you are reading is public or not>",
        google_service_account="<The Google Service Account information in order to access the sheet>",
        google_sheet_key="<The key of the sheet to read>",
        google_sheet_name="<The name of the sheet to read>",
        first_row_header="<True or False, depending if the first row of the table needs to be considered as the header>",
        on_bad_lines="<What to do if bad lines are discovered while reading the sheet>",
        clean="<True or False, depending if blank columns and rows need to be removed>"
    )

    sheet_dict_of_lists = read_google_sheet_as_dict_of_lists(
        is_public_sheet="<True or False, depending if the sheet you are reading is public or not>",
        google_service_account="<The Google Service Account information in order to access the sheet>",
        google_sheet_key="<The key of the sheet to read>",
        google_sheet_name="<The name of the sheet to read>",
        first_row_header="<True or False, depending if the first row of the table needs to be considered as the header>",
        on_bad_lines="<What to do if bad lines are discovered while reading the sheet>",
        clean="<True or False, depending if blank columns and rows need to be removed>"
    )

read_sheet_as_dataframe()
```

For more tips on how to use tasks and flows in a Collection, check out [Using Collections](https://orion-docs.prefect.io/collections/usage/)!

## Resources

If you encounter any bugs while using `prefect-google-sheets`, feel free to open an issue in the [prefect-google-sheets](https://github.com/stefanocascavilla/prefect-google-sheets) repository.

If you have any questions or issues while using `prefect-google-sheets`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

Feel free to ⭐️ or watch [`prefect-google-sheets`](https://github.com/stefanocascavilla/prefect-google-sheets) for updates too!

## Development

If you'd like to install a version of `prefect-google-sheets` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/stefanocascavilla/prefect-google-sheets.git

cd prefect-google-sheets/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
