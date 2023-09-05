.. _customization:

=============
Customization
=============

There are two methods to alter the theme.
The first, and simplest, uses the options exposed through ``html_theme_options`` in ``conf.py``.
This site's options are:

.. literalinclude:: conf.py
   :language: python
   :lines: 86-110
   :lineno-start: 86
   :linenos:

Many of these settings are provided in this site as examples; for a minimalistic example, see :ref:`quickstart`.

Configuration Options
=====================

Listed below are important customisation options for the `mdanalysis-sphinx-theme`.
Please see the `sphinx-rtd-theme configuration`_ documentation for more
information on other options.

``repo_url``
   Set the repo url for the link to appear.
``repo_name``
   The name of the repo.
   It must be set if repo_url is set.
``mda_official``
   Whether to use official MDA branding, e.g. its logo
``color_accent``
   Accent color. Choose any valid CSS color, or `mdanalysis-orange`.
``css_minify``
   Minify css files found in the output directory.

Sidebars
========
You must set ``html_sidebars`` in order for the side bar to appear.
There are four in the complete set.

.. code-block:: python

   html_sidebars = {
       "**": ["globaltoc.html", "localtoc.html", "searchbox.html"]
   }


You can exclude any to hide a specific sidebar.
For example, if this is changed to

.. code-block:: python

   html_sidebars = {
       "**": ["globaltoc.html"]
   }

then only the global ToC would appear on all pages (``**`` is a glob pattern).

Customizing the layout
======================

You can customize the theme by overriding Jinja template blocks.
For example, 'layout.html' contains several blocks that can be overridden or extended.

Place a 'layout.html' file in your project's '/_templates' directory.

.. code-block:: bash

    mkdir source/_templates
    touch source/_templates/layout.html

Then, configure your 'conf.py':

.. code-block:: python

    templates_path = ['_templates']

Finally, edit your override file ``source/_templates/layout.html``:

.. code-block:: jinja

    {# Import the theme's layout. #}
    {% extends '!layout.html' %}

    {%- block extrahead %}
    {# Add custom things to the head HTML tag #}
    {# Call the parent block #}
    {{ super() }}
    {%- endblock %}


.. _`sphinx-rtd-theme configuration`: https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html