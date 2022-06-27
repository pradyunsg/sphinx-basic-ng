# Goals

The primary goal is to make it easier to write Sphinx themes, by providing theme
authors with a consistent vocabulary for things in a Sphinx theme as well as an
easy-to-build-upon base theme. The theme is meant to provide a nicer base theme
for Sphinx theme authors than the Sphinx's built-in `basic` theme and to enable
sharing of certain common components for documentation themes for Sphinx.

## What it provides

Currently, `sphinx-basic-ng` provides two things to themes that derive from it:

- Components for common design patterns on documentation websites.
- Skeleton markup and styling for a 3-column website.

Additionally, the documentation and implementation serves as a resource for all
Sphinx theme authors on how to implement various common things in Sphinx themes
(eg: breadcrumbs, edit this page buttons etc).

## What it does not provide

This theme does not provide:

- components that require any Python or Javascript to implement them.
- styling for any of the components.
- any styling beyond what is necessary for the skeleton markup.
