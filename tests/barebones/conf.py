# Configuration file for the Sphinx documentation builder.
#
# Full list of options can be found in the Sphinx documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

#
# -- Project information -----------------------------------------------------
#

project = "sphinx-basic-ng demo"
copyright = "2021, Pradyun Gedam"
author = "Pradyun Gedam"

#
# -- General configuration ---------------------------------------------------
#

extensions = ["myst_parser"]

html_theme_options = {
    "announcement": ["components/demos/announcement-demo.html"],
    "topbar_left": ["components/demos/topbar-left-demo.html"],
    "topbar_middle": ["components/demos/topbar-middle-demo.html"],
    "topbar_right": ["components/demos/topbar-right-demo.html"],
    "sidebar_left": ["components/demos/sidebar-left-demo.html", "components/site-logo.html", "components/site-nav.html"],
    "sidebar_right": ["components/demos/sidebar-right-demo.html"],
    "middle_content": ["components/demos/middle-content-demo.html", "components/page-content.html"],
    "content_footer": ["components/demos/content-footer-demo.html", "components/next-prev.html"],
    "footer": ["components/demos/footer-demo.html"],
}

#
# -- Options for HTML output -------------------------------------------------
#

html_theme = "basic-ng"
