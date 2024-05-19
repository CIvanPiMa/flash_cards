"""
Entrypoint module, for `python -m flash_cards`.

# References:
- https://www.python.org/dev/peps/pep-0338/
- https://docs.python.org/3/using/cmdline.html#cmdoption-m
"""

from .cli import cli

if __name__ == "__main__":
    cli()
