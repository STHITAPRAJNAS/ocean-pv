import sphinx_rtd_theme
import os
import sys
sys.path.insert(0, os.path.abspath('..'))


extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.todo',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
]

todo_include_todos = True

html_theme = "sphinx_rtd_theme"

# -- Project information -----------------------------------------------------

project = 'OCEAN Personality Visualization'
copyright = '2020, IgnisDa'
author = 'IgnisDa'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

master_doc = 'index'
