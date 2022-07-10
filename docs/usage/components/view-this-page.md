# "View this page" link

It is fairly common for technical documentation websites to contain a link to
view the original sources of a page. This makes it easy for a reader to quickly
see how something is written in the markup and provides a decent way to navigate
to the source repository of the project.

## Usage

```jinja
{% include "components/view-this-page.html" with context %}
```

This will add a single `a[href]` tag, with the text "View this page".

This uses the user-provided source repository links if provided. If they're not
provided and the documentation is built with `html_copy_source = True` _and_
`html_show_sourcelink = True` (which are the default), the link points to the
Sphinx-copied sources.

You also need to declare the following in `theme.conf`'s `options` section:

```ini
source_view_link =
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

```python
html_theme_options = {
    "source_view_link": "https://my.host/project/view/docs/{filename}",
    "source_repository": "https://my.host/project",
    "source_branch": "main",
    "source_directory": "docs/",
}
```

Those user-provided values are used to determine the link for viewing the
generated page on the hosting platform. Currently supported platforms are
`https://github.com`, `https://bitbucket.org` and `https://gitlab.io/`.

This component can be customised in a theme-specific manner in two ways, both of
which require adding a new template file (typically,
`components/view-this-page.html` file in the theme).

1. Extending

   This is be done by extending this file and overriding the the
   `link_available` and `link_not_available` blocks, which are used based on
   whether the view link can be rendered -- i.e. whether the user has provided
   the configuration values noted above.

   ```jinja
   {% extends "basic-ng/components/view-this-page.html" %}

   {% block link_not_available %}
   {{ warning("Hey user! Provide the repository information!" )}}
   {% endblock link_not_available %}
   ```

2. Overriding

   This can be done by _not_ extending the base template. This allows the theme
   to have complete control over the way the URL provided is used. If a theme
   does this, it is also responsible for presenting warnings to the user when
   the user has not provided all the required configuration variables to the
   theme (see the sources of `view-this-page.html`, after macros).

   It is possible to use the `determine_page_view_link` macro, to get the
   relevant URL from the regular configuration (it assumes the user has it set).

   ```jinja
   {% from "basic-ng/components/view-this-page.html" import determine_page_view_link with context %}

    <a href="{{ determine_page_view_link() }}">{{ _("View this page") }}</a>
   ```
