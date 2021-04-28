# Sidebar Drawer Toggles

The default skeleton provides drawers, as part of providing a responsive skeleton for the themes. As a part of this, the various pages need to include toggles so that users can show/hide the corresponding sidebars.

## Usage

```jinja
{% include "components/toggle-sidebar-primary.html" %}
{% include "components/toggle-sidebar-secondary.html" %}
```

This will add a single `label`, which contains a hamburger `svg` by default. These labels are hidden with `display: none` when the corresponding sidebar is visible-by-default.

## Configurability

The theme author can change the inner contents of the label by overriding `{% block content %}`.
