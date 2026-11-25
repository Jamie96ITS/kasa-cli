__version__ = '0.1.0'
import asyncio
import sys

import asyncclick as click
from kasa.cli import common
from kasa.cli.__main__ import cli

_echo = common.echo


def _echo_with_context_fallback(*args, **kwargs):
    if click.get_current_context(silent=True) is None:
        click.echo(*args, **kwargs)
    else:
        _echo(*args, **kwargs)


common.echo = _echo_with_context_fallback


if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    cli()
