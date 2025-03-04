# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'tdmc'
copyright = 'Marko Petrovic'
author = 'Marko Petrovic'
release = '0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser',
              "sphinx.ext.autodoc",
              "sphinx.ext.viewcode",
              "sphinx_rtd_theme",
              "sphinx.ext.napoleon",
              "sphinx.ext.mathjax"
              ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_static_path = ['_static']
html_css_files = ['custom.css']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
