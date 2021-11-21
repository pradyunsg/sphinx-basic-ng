from dataclasses import dataclass
from typing import Any, Dict, List, Optional

import rich
import sphinx.addnodes
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx.environment.collectors import EnvironmentCollector
from sphinx.util import url_re
from sphinx.util.osutil import relative_uri

_GOLDEN_NAVIGATION_TREE = None


@dataclass
class NavigationTreeNode:
    current: bool
    caption: Optional[str]
    title: Optional[str]
    reference: Optional[str]
    entries: "List[NavigationTreeNode]"
    hidden: bool


class TocTreeCollector(EnvironmentCollector):
    """Collect toctrees associated with each document.

    The collected information is cached in the environment, as ``basic_ng_toctrees``
    alongside the actual document, making this reasonably performant as well.

    The final structure of the ``basic_ng_toctrees`` is a dictionary where the key is
    the document name and the value is a list of ``toctree`` nodes.
    """

    def enable(self, app: Sphinx):
        super().enable(app)

        # The environment might be populated from the cache. If it is, the
        # attribute will already exist and it does not need to be re-initialized.
        if not hasattr(app.env, "basic_ng_toctrees"):
            app.env.basic_ng_toctrees = {}

    def clear_doc(self, app: Sphinx, env: BuildEnvironment, docname: str) -> None:
        env.basic_ng_toctrees.pop(docname, None)

    def merge_other(
        self,
        app: Sphinx,
        env: BuildEnvironment,
        docnames: List[str],
        other: BuildEnvironment,
    ) -> None:
        for docname in docnames:
            env.basic_ng_toctrees[docname] = other.basic_ng_toctrees[docname]

    def process_doc(self, app: Sphinx, doctree: sphinx.addnodes.document) -> None:
        docname = app.env.docname

        app.env.basic_ng_toctrees[docname] = doctree.traverse(sphinx.addnodes.toctree)


def _html_page_context(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: Dict[str, Any],
    doctree: Any,
) -> None:
    """Add `navigation_json` that will be available on templates.

    While the documentation tree is same across a single build, this is called
    once-per-page as sections of the tree might be collapsed and the path to
    the current page needs to be marked "active".
    """

    def get_entry(
        doctree: sphinx.addnodes.toctree,
        *,
        parent_docnames: List[str],
        hidden: bool,
    ) -> NavigationTreeNode:
        caption = doctree.get("caption")
        raw_entries = doctree.get("entries")
        hidden = doctree.get("hidden") or hidden

        entries = []
        pagename_in_this_tree = False
        for title, ref in raw_entries:
            # Break any potential cycles. Sphinx already prints a warning.
            if ref in parent_docnames:
                continue

            if ref == "self":
                entry = NavigationTreeNode(
                    current=True,
                    caption=None,
                    title=title,
                    reference="#",
                    entries=[],
                    hidden=hidden,
                )
            elif url_re.match(ref):
                entry = NavigationTreeNode(
                    current=False,
                    caption=None,
                    title=title,
                    reference=ref,
                    entries=[],
                    hidden=hidden,
                )
            else:
                entry = get_entry_for_document(
                    ref,
                    title_override=title,
                    parent_docnames=parent_docnames,
                    hidden=hidden,
                )

            entries.append(entry)

            if entry.current:
                pagename_in_this_tree = True

        return NavigationTreeNode(
            current=pagename_in_this_tree,
            caption=caption,
            title=None,
            entries=entries,
            reference=None,
            hidden=hidden,
        )

    def get_entry_for_document(
        docname: str,
        *,
        title_override: str,
        parent_docnames: List[str],
        hidden: bool,
    ) -> NavigationTreeNode:
        baseuri = app.builder.get_target_uri(pagename).rsplit("#", 1)[0]
        toc_uri = app.builder.get_target_uri(docname).rsplit("#", 1)[0]
        url = relative_uri(baseuri, toc_uri)

        if title_override is None:
            title = app.env.titles[docname].astext()
        else:
            title = title_override
        return NavigationTreeNode(
            current=docname == pagename,
            caption=None,
            title=title,
            entries=[
                get_entry(
                    tree, parent_docnames=parent_docnames + [docname], hidden=hidden
                )
                for tree in app.env.basic_ng_toctrees[docname]
            ],
            reference=url,
            hidden=hidden,
        )

    # Each toctree will create navigation section
    result = get_entry_for_document(
        app.env.config.root_doc,
        title_override=app.env.config.html_index_name,
        parent_docnames=[],
        hidden=False,
    )
    context["basic_ng_site_structure"] = result


def setup_navigation(app: Sphinx) -> Dict[str, Any]:
    app.add_env_collector(TocTreeCollector)
    app.connect("html-page-context", _html_page_context)
    app.add_config_value("html_index_name", default="Home", rebuild="html")
