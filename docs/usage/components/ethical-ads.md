# Ethical Ads

A lot of Sphinx documentation is hosted on [ReadTheDocs], who provide
free docs hosting for open source projects. [Ethical Ads] is a
privacy-respecting ad network built by ReadTheDocs, and is one of the
contributors to their sustainability.

Adding this component to your page in the correct places, helps you make
sure that when ReadTheDocs tries to show ethical ads in documentation
built with your theme, they are well integrated with it and show up
where you expect them to be visible.

## Usage

```jinja
{% include "components/ethical-ads.html" %}
```

It is also expected that the page will [manually load ads]. This is done
for pages hosted by ReadTheDocs automatically.

## Configurability

There are 3 values that can be provided via the html-context, which
correspond to the following configuration attributes on the ethical ad
`div`:

- `ethical_ad_class`: maps to `class`
- `ethical_ad_type`: maps to `data-ea-type`
- `ethical_ad_publisher`: maps to `data-ea-publisher`

If these values are not set, they will take reasonable values for
ReadTheDocs-based documentation.

The `div` for the ad is only included on the page if the documentation
is being built on ReadTheDocs or `ethical_ad_publisher` is set.

```{tip}
If you need additional control/configuration, it is recommended to
include the this component as shown here, and to override the
`components/ethical-ads.html` file in your theme.
```

[ReadTheDocs]: https://readthedocs.org/
[Ethical Ads]: https://www.ethicalads.io/
[manually load ads]: https://ethical-ad-client.readthedocs.io/en/latest/#manually-loading-ads
