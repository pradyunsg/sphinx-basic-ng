# Expectations

This is an explanation page, describing what the expectations are around:

- how this project is scoped, and why we might say no to certain things.
- how this project will react to upstream Sphinx changes.
- how this project would interact with derivative theme authors.

## Project Scope

This project is intended to serve as a fairly-unopinionated base for Sphinx
themes to use. It has one opinionated part -- the skeleton provided -- that can
be removed/omitted if the theme authors wish to do so.

Any new components added to the project should be generally applicable and
should not need any Python code to support it. There is no reason to add
theme-specific components, since derivative themes can extend the components
they can use by adding a `components/<name>.html` template file in their own
source tree.

## Sphinx

This project tracks the Sphinx project fairly loosely. The general expectation
is that Sphinx will evolve slowly and there is no urgency in keeping up with a
new Sphinx major version bump, when it happens.

This project will be updated in response to changes in Sphinx, as quickly as
feasible with the development and community management resources available. This
does mean that, if this project does not have sufficient resources to do so,
these updates will be slow.

## Derivative Themes

At the time of writing, this project has a no backwards compatibility policy --
the project is in an alpha state, with only two known downstream themes: Furo
and Lutra.

If you do use this in your project, please feel welcome to do so! We'd
appreciate if you reach out over the issue tracker to let us know that you're
doing this. It's likely that there will be some changes to the skeleton as well
as components, and we welcome any feedback on how to improve both of them and
make them work better.
