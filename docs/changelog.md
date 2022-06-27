# Changelog

## 0.0.1.alpha12

- Add a `view-this-page` component
- Improve `edit-this-page` component's extensibility
- Lint the entire codebase with prettier
- Expand the documentation with more content
- Tweak the size of the highest breakpoint

## 0.0.1.alpha11

- Declare Sphinx 5 compatibility.
- Drop support for Python 3.6.

## 0.0.1.alpha10

- Move the container tag inside the container block.
- Add a new `sections/header-content.html`.
- Implement `search.html`.
- Implement `genindex*.html`.
- Implement `domainindex.html`.
- Clarify handling of overlays for sidebars.
- Improve handling of padding around main content.
- Increase the z-index of overlay'd sidebars.

## 0.0.1.alpha9

- Move the JS files to the end of body.

## 0.0.1.alpha8

- Improve `debug.css`.
- Expand the breadcrumbs conditional to do the right thing.
- Include block names in endblock, in the Jinja templates.
- Allow for full-width content styles.
- Extend scaffold to fit 90rem screens.
- Add `match-content-width` for content heading and footer.
- Use viewport width for containers on mobile.
- Only show `edit-this-page` if `source_suffix` is known.
- Lightly tweak example theme.
- Present better warnings in noxfile.
- Drop `_html_page_context`.
- Improve `breadcrumbs.html` implementation.
- Add clearer "not implemented" warnings.
- Drop the overflow handling, which is incompatible with `sticky`.

## 0.0.1.alpha7

- Add additional breakpoint of 50rem (800px) for content width.

## 0.0.1.alpha6

- Bump up to Sphinx 4.
- Add example documentation, with an inline theme
- Add header-article section.
- Add `!important` for the hiding of sidebar toggles.
- Fix the search input example.
- Tweak announcement container, to not be centered.

## 0.0.1.alpha5

- Allow omitting skeleton.css, via html-context.

## 0.0.1.alpha4

- Add component: search-input
- Add component: search-hide
- Add components for toggling sidebars

## 0.0.1.alpha3

- Add a nice introduction to `sections/article.html`
- Add component: related-pages
- Add responsive off-canvas sidebars, and corresponding components.
- Host documentation on ReadTheDocs.
- Rename certain sections of the scaffolding.
- Add more headers and footers to the scaffolding.

## 0.0.1.alpha2

- Add initial documentation scaffolding.
- Add component: breadcrumbs
- Add component: edit-this-page
- Add component: ethical-ads
- Add component: logo
- Remove Sphinx variables from skeleton.
- Updating terminology for parts of this project.

## 0.0.1.alpha1

Initial release.
