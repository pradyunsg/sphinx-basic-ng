# Search input

Sphinx provides offline search to allow users to search the generated
documentation.

## Usage

```jinja
{% include "components/search-input.html" %}
```

This will add a single `form.search-container`, containing a single
`input.search-input` with the translated placeholder text: "Search". Pressing
{kbd}`Enter` in this element redirects the user to the search page, with the
appropriate query parameters.

```{important}
Sphinx's search JS looks inside elements with `[role="main"]`, so make sure that all user provided content is within an element with that attribute.
```

## Configurability

None.
