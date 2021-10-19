# Getting Started

This is a short guide to getting started with the `basic-ng` theme.
This tutorial focuses on modifying a theme directly from a Sphinx site.

:::{seealso}
It is also possible to create a `pip`-installable theme that you can distribute for others to use.
This tutorial does **not** cover this use-case, and instead focuses on modifying this theme from a Sphinx site.
For an example of a standalone theme, see the [`basic-ng-template` repository](https://github.com/choldgraf/sphinx-basic-ng-template) which follows similar steps described here, and bundles the theme as a standalone package.
:::

## Quick background on theming with Sphinx

It is a good idea to familiarize yourself with [HTML theming in Sphinx](https://www.sphinx-doc.org/en/master/usage/theming.html).
By default, Sphinx ships with a theme called `basic` that serves as an ancestor for many other Sphinx themes.
Theme creators then use that theme as a base, and add customizations on top of it.
The `basic-ng` theme is used _instead of_ the default `basic` theme.

To use this theme with your Sphinx site, follow the sections below.

## Install the `sphinx-basic-ng` theme

Install with pip.

% TODO: Convert this to pip once it's ready to be installed from there
```console
$ pip install https://github.com/pradyunsg/sphinx-basic-ng/archive/refs/heads/main.zip
```

## Create a new Sphinx project

Create an empty Sphinx project with the following command:

```console
$ sphinx-quickstart mytestsite
```

Answer the prompts (you can generally accept the defaults) to build a skeleton Sphinx site.

## Configure your Sphinx project to use the `sphinx-basic-ng` theme

In `mytestsite/conf.py` modify the `html_theme` variable like so:

```
html_theme = "basic-ng"
```

Your Sphinx site will now use the `basic-ng` templates to build HTML for the documentation.

## Build your Sphinx site

The following commands will build the HTML for your Sphinx site, and place them in the folder `_build/html`:

```console
$ cd mytestsite
$ sphinx-build -b html . _build/html
```

## Look at the rendered documentation

Open `_build/html/index.html`, you should see the `sphinx-basic-ng` skeleton, with different colors showing major areas of the theme.

Each area of the theme is defined in a template named `sections/<section-name>.html`.

The areas are displaying their default text, which you can over-ride by defining your own template HTML files.
In the middle should be a short welcome message that describes what is going on.

Next we will customize one of the sections.

## Customize a section

:::{note}
This expects that the `_templates` folder was created when you ran `sphinx-quickstart` and that the following configuration exists in `conf.py`:


```python
html_templates = ["_templates"]
```
:::

You can customize sections of this template by defining your own HTML template at the same location as the section.

We'll do this by following these steps:

Create an HTML file that has the same path as a section we want to over-write.
We'll start by over-riding the main article section, at `sections/article.html`.
We'll create a new file with:

```console
$ mkdir _templates/sections
$ touch _templates/sections/article.html`
```

Now add the following test to it:

```html
<p>This is a test!</p>
```

Finally, save and re-build your site:

```console
$ sphinx-build -b . _build/html
```

Open `_build/html/index.html`, and you should see that the main article area now contains your text.

You can customize any of the sections in this way.
Next we will add a component to a section.

## Add a component

Components are small snippets of HTML that do specific things in your theme (like add an "edit this page" button).
You add components to a page by using them with `{% include %}` functions in your theme templates.

:::{seealso}
For more information about `{% include %}`, see [the Jinja documentation](https://jinja.palletsprojects.com/en/3.0.x/templates/#include).
:::

Components each have a name like `components/<component-name>.html`.
We'll add a "search input" component to our left sidebar, so that a user can search things on our site.
To do so, first create an override template for the "primary" sidebar:

```
touch _templates/sections/sidebar-primary.html
```

Now put the following HTML into the template you just created:

```html
There should be a searchbox under me.

{% include "components/search-input.html" %}
```

Now re-build your site:

```console
$ sphinx-build -b . _build/html
```

When you look at your site's built HTML, you should now see a search bar component in your primary sidebar.

## Remove a section

If you want a section to go away entirely, you can simply define an **empty HTML template** at that section's location in your templates folder.
In general, when sections are removed, the other sections will re-size to accommodate the extra space.

To remove the secondary header at `sections/header-secondary.html`, create an empty HTML template at its location:

```console
$ touch _templates/sections/header-secondary.html
```

And re-build your site.

```console
$ sphinx-build -b . _build/html
```

That section of the output should now be gone!

## Add your own CSS

Finally, let's add some style rules to our site.
There are many ways to do this in Sphinx, but we'll use the method that is commonly used when creating standalone Sphinx themes.

First, create a CSS file that will define some custom rules:

```console
$ mkdir _static/css
$ touch _static/css/custom.css
```

Next, add two CSS rules to it:

```css
p {
  font-size: 3em;
}

.sb-sidebar-primary {
    width: 5rem;
}
```

Finally, configure your Sphinx build to **use** this CSS file.
To do so, add a simple `setup` function to your `conf.py` file.

```python
def setup(app):
    app.add_css_file("css/custom.css")
```

Now build your Sphinx site (you may need to delete the old site files in `_build/html`):

```console
$ sphinx-build -b . _build/html
```

You should now see the style applied to your site.
The text in the middle of the page should be bigger, and the primary sidebar should be narrower.
Note that for the sidebar, as it shrinks, the other content on the page will grow to accommodate the extra space.

## Next steps: create a standalone sub-theme

This tutorial covered the basics of installing and modifying this theme with a Sphinx site.
If you wish to develop a **standalone theme** that is `pip`-installable, you can follow many of the same patterns described here, but you will need to structure your theme slightly differently.
% TODO: update this link if the repository is moved.
See the [`sphinx-basic-ng-template` repository](https://github.com/choldgraf/sphinx-basic-ng-template) for an example of a standalone theme that uses this theme as a parent.
