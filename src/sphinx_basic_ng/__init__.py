"""A modern skeleton for Sphinx themes."""

__version__ = "0.1.0.dev0"

from pathlib import Path
import sphinx
from typing import Any, Dict


THEME_PATH = (Path(__file__).parent / "theme" / "basic-ng").resolve()


def setup(app: sphinx.application.Sphinx) -> Dict[str, Any]:
    """Entry point for sphinx theming."""
    app.require_sphinx("3.0")

    app.add_html_theme("basic-ng", str(THEME_PATH))

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": __version__,
    }
