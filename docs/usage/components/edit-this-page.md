# "Edit this page" link

It is fairly common for technical documentation websites to contain a
link to edit the original sources of a page. This makes it easy for a
reader to quickly fix a typo and provides a decent way to navigate to
the source repository of the project.

## Usage

```jinja
{% include "components/edit-this-page.html" with context %}
```

This will add a single `a[href]` tag, with the text "Edit this page".

You also need to declare the following in `theme.conf`'s `options`
section:

```ini
source_repository =
source_branch =
source_directory =
```

## Configurability

The documentation author can set values in their `conf.py` file using
`html_theme_options`:

```python
html_theme_options = {
  "source_repository": "https://github.com/pradyunsg/sphinx-basic-ng/",
  "source_branch": "main",
  "source_directory": "docs/",
}
```

Those user-provided values are used to determine the link for editting
the generated page on the hosting platform.

There are no knobs provided for the theme authors, who are expected to
override this component, if they wish to make customisations. They can
depend on the `determine_page_edit_link` macro to get the relevant URL.

```jinja
{% from "!components/edit-this-page.html" import determine_page_edit_link with context %}
```
