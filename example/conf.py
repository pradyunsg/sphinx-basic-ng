# Configuration file for the Sphinx documentation builder.
#
# Full list of options can be found in the Sphinx documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

#
# -- Project information -----------------------------------------------------
#

project = "sphinx-basic-ng sample"
copyright = "2021, Pradyun Gedam"
author = "Pradyun Gedam"

#
# -- General configuration ---------------------------------------------------
#

extensions = ["myst_parser"]

#
# -- Options for HTML output -------------------------------------------------
#

html_theme = "basic-ng"
html_style = "sample.css"
templates_path = ["_theme"]
html_static_path = ["_static"]
html_context = {
    "theme_announcement": "Site wide announcement!",
}
