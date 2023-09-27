# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'iDerive'
copyright = '2023, Roie R. Black'
author = 'Roie R. Black'

# The full version, including alpha/beta/rc tags
release = '0.1.0'


# -- General configuration ---------------------------------------------------

extensions = [
        'sphinx_rtd_theme',
        'sphinx_ext.wordcount',
        'sphinxcontrib.bibtex',
        'sphinxcontrib.programoutput',
        'sphinx.ext.autodoc',
        'sphinx.ext.viewcode',
        'sphinx.ext.autosummary',
        'sphinx_ext.tikzimg',
]

bibtex_bibfiles = ['references.bib']
tikz_proc_suite = 'ImageMagick'

autodoc_member_order = "bysource"
autodoc_default_options = {
        "members": True,
        "show_inheritance": True
        }
autosummary_generate = True

linkcheck_timeout = 3
linkcheck_retries = 2
spelling_list_filename = ['spelling_wordlist.txt']
spelling_lang='en_US'

master_doc = 'index'
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

rst_prolog = """
..  include::   /header.inc
"""


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']
