# Breadcrumbs

A breadcrumb navigation provide links back to each "parent" page of the
current page, showing the user's current location in a website and
giving them a good way to navigate within it.

## Usage

```jinja
{% include "components/breadcrumbs.html" %}
```

When the page does not have "parent" pages (in the top-level of the hierarchy), this will be empty.

In all other cases, the structure looks like:

- a single `nav.breadcrumb-nav`
  - a single `ol.breadcrumb-nav-list`
    - one-or-more `breadcrumb-nav-list-item` containing a single
      `a[href]` tag.
    - a single `breadcrumb-nav-list-item` contain a single `span` tag.

```{tip}
See [this page][w3schools-breadcrumbs] for an example of how to stylise
breadcrumbs with this structure.
```

## Configurability

None.

[w3schools-breadcrumbs]: https://www.w3schools.com/howto/howto_css_breadcrumbs.asp
