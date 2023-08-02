# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------


# -- Project information -----------------------------------------------------

project = "MDAnalysis Sphinx theme"
html_title = "MDAnalysis Sphinx theme"
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath("."))
# from distutils.version import LooseVersion

copyright = "2023, MDAnalysis"
author = "MDAnalysis"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "nbsphinx",
    "mdanalysis_sphinx_theme",
    "sphinxcontrib.autodoc_pydantic",
    "sphinx_search.extension",
]

# Autodoc settings
autosummary_generate = True

autodoc_default_options = {
    "members": True,
    "inherited-members": True,
    "member-order": "bysource",
}
autodoc_preserve_defaults = True
autodoc_typehints_format = "short"
# Workaround for autodoc_typehints_format not working for attributes
# see https://github.com/sphinx-doc/sphinx/issues/10290#issuecomment-1079740009
python_use_unqualified_type_names = True

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

napoleon_numpy_docstring = True
napoleon_google_docstring = False
napoleon_attr_annotations = True
napoleon_custom_sections = [("attributes", "params_style")]
napoleon_use_rtype = False
napoleon_use_param = True
napoleon_use_ivar = True
napoleon_preprocess_types = True

# Add any paths that contain templates here, relative to this directory.
# templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "mdanalysis_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named 'default.css' will overwrite the builtin 'default.css'.
html_static_path = ["_static"]

# If HTML theme settings isn't lines 90-160, remember to change customization.rst

# -- HTML theme settings ------------------------------------------------
html_show_sourcelink = True
html_sidebars = {
    "**": ["globaltoc.html", "localtoc.html", "searchbox.html"],
    "customization": ["globaltoc.html", "searchbox.html"],
    "subpage/second-subsubpage": ["globaltoc.html", "searchbox.html"],
}

# material theme options (see theme.conf for more information)
html_theme_options = {
    "base_url": "https://minium.com.au/mdanalysis-sphinx-theme/",
    "repo_url": "https://github.com/lilyminium/mdanalysis-sphinx-theme/",
    "repo_name": "mdanalysis-sphinx-theme",
    "mda_official": True,
}

# If HTML theme settings isn't lines 90-160, remember to change customization.rst

language = "en"
html_last_updated_fmt = ""

todo_include_todos = True

html_use_index = True
html_domain_indices = True

nbsphinx_execute = "always"
nbsphinx_kernel_name = "python3"

extlinks = {
    "duref": (
        "http://docutils.sourceforge.net/docs/ref/rst/" "restructuredtext.html#%s",
        "%s",
    ),
    "durole": ("http://docutils.sourceforge.net/docs/ref/rst/" "roles.html#%s", "%s"),
    "dudir": (
        "http://docutils.sourceforge.net/docs/ref/rst/" "directives.html#%s",
        "%s",
    ),
}
