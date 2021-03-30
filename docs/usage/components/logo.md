# Site Logo

Sphinx allows users to set a logo for their site, using the
[`html_logo`][sphinx-html_logo] variable in `conf.py`. Themes are
expected to have this on the page, if provided by the user.

## Usage

```jinja
{% include "components/logo.html" %}
```

If the logo is set, this adds an `img.site-logo` with the correct URL
for the logo. Otherwise, this is empty.

## Configurability

None.
