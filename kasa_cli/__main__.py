__version__ = '0.1.0'
import asyncio
import sys
from kasa.cli.__main__ import cli

if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    cli()
