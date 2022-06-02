# Breadcrumbs

A breadcrumb navigation provide links back to each "parent" page of the current
page, showing the user's current location in a website and giving them a good
way to navigate within it.

## Usage

```jinja
{% include "components/breadcrumbs.html" %}
```

When there are no list-items to show in the breadcrumb, this component will
render empty.

In all other cases, the structure looks like:

- a single `nav.breadcrumb-nav`
  - a single `ol.breadcrumb-nav-list`
    - one-or-more `breadcrumb-nav-list-item` containing a single `a[href]` tag.
    - a single `breadcrumb-nav-list-item` contain a single `span` tag.

```{tip}
See [this page][w3schools-breadcrumbs] for an example of how to stylise
breadcrumbs with this structure.
```

## Configurability

There are 2 values that can be provided via the html-context, which provide
control over the components shown in the breadcrumbs:

- `breadcrumb_include_index_as`: If provided, this name is used as the first
  list-item of the breadcrumb on pages other than the `index` page.The
  corresponding list-item will have an additional class:
  `breadcrumb-nav-index-item`.

- `breadcrumb_include_page`: If truthy, the current page is included in the
  breadcrumb as the final list-item, with only a `span` (there's no `a[href]` in
  it). The corresponding list-item will have an additional class:
  `breadcrumb-nav-page-item`.

[w3schools-breadcrumbs]:
  https://www.w3schools.com/howto/howto_css_breadcrumbs.asp
