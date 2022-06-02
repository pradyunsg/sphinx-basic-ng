# "Hide search matches" link

Sphinx provides functionality to hide search matches, after the user lands on a
page from search. This component exposes that to the user, allowing them to read
the content once they've found it, without being distracted by the highlights.

## Usage

```jinja
{% include "components/search-hide.html" %}
{% include "components/toggle-sidebar-secondary.html" %}
```

This will add a single empty `div`, with the id `searchbox`. When a page has
highlights, Sphinx's built-in search JS will inject the following HTML into this
element:

```html
<p class="highlight-link">
  <a href="javascript:Documentation.hideSearchWords()">Hide Search Matches</a>
</p>
```

## Configurability

None.
