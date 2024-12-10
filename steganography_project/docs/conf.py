# File: docs/conf.py
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# Project information
project = 'Steganography Toolkit'
copyright = '2024, Your Name'
author = 'Your Name'
release = '1.0.0'

# Extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

# Theme
html_theme = 'sphinx_rtd_theme'

