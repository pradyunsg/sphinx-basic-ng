# "Edit this page" link

It is fairly common for technical documentation websites to contain a link to
edit the original sources of a page. This makes it easy for a reader to quickly
fix a typo and provides a decent way to navigate to the source repository of the
project.

## Usage

```jinja
{% include "components/edit-this-page.html" with context %}
```

This will add a single `a[href]` tag, with the text "Edit this page".

You also need to declare the following in `theme.conf`'s `options` section:

```ini
source_edit_link =
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
    "source_edit_link": "https://my.host/project/edit/docs/{filename}",
    "source_repository": "https://my.host/project",
    "source_branch": "main",
    "source_directory": "docs/",
}
```

Those user-provided values are used to determine the link for editing the
generated page on their code hosting platform.

This component can be customised in a theme-specific manner in two ways, both of
which require adding a new template file (typically,
`components/edit-this-page.html` file in the theme).

1. Extending

   This is be done by extending this file and overriding the the
   `link_available` and `link_not_available` blocks, which are used based on
   whether the edit link can be rendered -- i.e. whether the user has provided
   the configuration values noted above.

   ```jinja
   {% extends "basic-ng/components/edit-this-page.html" %}

   {% block link_not_available %}
   {{ warning("Hey user! Provide the repository information!" )}}
   {% endblock link_not_available %}
   ```

2. Overriding

   This can be done by _not_ extending the base template. This allows the theme
   to have complete control over the way the URL provided is used. If a theme
   does this, it is also responsible for presenting warnings to the user when
   the user has not provided all the required configuration variables to the
   theme (see the sources of `edit-this-page.html`, after macros).

   It is possible to use the `determine_page_edit_link` macro, to get the
   relevant URL from the regular configuration (it assumes the user has it set).

   ```jinja
   {% from "basic-ng/components/edit-this-page.html" import determine_page_edit_link with context %}

    <a href="{{ determine_page_edit_link() }}">{{ _("Edit this page") }}</a>
   ```
