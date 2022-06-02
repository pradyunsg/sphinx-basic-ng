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

Those user-provided values are used to determine the link for editting the
generated page on the hosting platform.

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

   This is done by depending on the `determine_page_edit_link` macro, to get the
   relevant URL and _not_ extending this file. This allows the theme to have
   complete control over the way the URL provided is used.

   If a theme does this, it is also responsible for presenting warnings to the
   user when the user has not provided all the required configuration variables
   to the theme.

   ```jinja
   {% from "basic-ng/components/edit-this-page.html" import determine_page_edit_link with context %}

   {%- if page_source_suffix -%}
    {%- if READTHEDOCS and github_repo %}
      {% set url = "https://github.com/{{ github_user }}/{{ github_repo }}/edit/{{ github_version }}{{ conf_py_path }}{{ pagename }}{{ page_source_suffix }}" %}
      <a class="muted-link" href="{{ url }}">{{ _("Edit this page") }}</a>
    {%- elif theme_source_repository -%}
      {%- if not theme_source_branch -%}
        {{ warning("Provided `source_repository` but not `source_branch`. ")}}
      {%- endif -%}
      <a class="muted-link" href="{{ determine_page_edit_link() }}">{{ _("Edit this page") }}</a>
    {%- endif -%}
   {%- endif -%}
   ```
