"""A modern skeleton for Sphinx themes."""

__version__ = "0.0.1.a6"

from pathlib import Path
from typing import Any, Dict

import sphinx

_THEME_PATH = (Path(__file__).parent / "theme" / "basic-ng").resolve()


def _html_page_context(
    app: sphinx.application.Sphinx,
    pagename: str,
    templatename: str,
    context: Dict[str, Any],
    doctree: Any,
) -> None:
    if "content_width" not in context:
        context["content_width"] = "40rem"
    if "sidebar_width" not in context:
        context["sidebar_width"] = "15rem"


def setup(app: sphinx.application.Sphinx) -> Dict[str, Any]:
    """Entry point for sphinx theming."""
    app.require_sphinx("3.0")

    app.add_html_theme("basic-ng", str(_THEME_PATH))

    app.connect("html-page-context", _html_page_context)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": __version__,
    }
