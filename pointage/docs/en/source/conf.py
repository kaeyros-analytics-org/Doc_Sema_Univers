# Configuration file for the Sphinx documentation builder.

import os
import sys
import sphinx_rtd_theme

# Ajouter le chemin vers le dossier parent pour trouver les modules Python
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------

project = 'Pointage En'
copyright = '2025, Kaeyros Analytics'
author = 'Kaeyros Analytics'
release = '1.0'


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autosectionlabel',
    'myst_parser',  # remplacer 'recommonmark' par 'myst_parser'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']
html_css_files = [
    'css/custom.css',
]

# html_favicon = 'images/favicon.ico'
# html_logo = 'images/logo.png'
