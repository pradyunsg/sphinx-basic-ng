# Related pages

Sphinx provides "next page" and "previous page" information, when
rendering a page. This information is useful for documentation which
has some sort of flow, as well as providing more navigational
capabilities to the reader.

## Usage

```jinja
{% include "components/related-pages.html" with context %}
```

This will add a single `div.related-pages`, which may be empty.

The structure of this component is:

- `div.related-pages`
  - `a[href].next-page` (omitted if there's no next page)
    - `div.page-info`
      - `div.context`
        - `span`
          - "Next" with translation
      - `div.title`
        - Title of the page
  - `a[href].prev-page` (omitted if there's no previous page)
    - `div.page-info`
      - `div.context`
        - `span`
          - "Previous" with translation
      - `div.title`
        - Title of the page

## Configurability

None.
