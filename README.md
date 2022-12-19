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
    goodbye_prefect_google_sheets,
    hello_prefect_google_sheets,
)

# Use `with_options` to customize options on any existing task or flow:

custom_goodbye_prefect_google_sheets = goodbye_prefect_google_sheets.with_options(
    name="My custom task name",
    retries=2,
    retry_delay_seconds=10,
)

@flow
def example_flow():
    hello_prefect_google_sheets
    custom_goodbye_prefect_google_sheets

example_flow()
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
