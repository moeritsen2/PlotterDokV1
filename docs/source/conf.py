# Configuration file for the Sphinx documentation builder.

# -- Project information

project = "OBP-Plotter V4 Dokumentation"
copyright = "2024, Open Boat Projects"
author = "Michael Maass"

#release = '0.1'
#version = '0.1.0'

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
]

intersphinx_mapping = {
    "rtd": ("https://docs.readthedocs.io/en/stable/", None),
    "python": ('https://docs.python.org/3/', None),
    "sphinx": ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# -- Options for EPUB output
epub_show_urls = "footnote"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"

html_theme_options = {
    # 'typekit_id': 'hiw1hhg',
    # 'analytics_id': '',
    # 'sticky_navigation': True  # Set to False to disable the sticky nav while scrolling.
    #'logo_only': True,  # if we have a html_logo below, this shows /only/ the logo with no title text
    'collapse_navigation': False,  # Collapse navigation (False makes it tree-like)
    # 'display_version': True,  # Display the docs version
    # 'navigation_depth': 4,  # Depth of the headers shown in the navigation bar
}

html_static_path = ["_static"]

def setup(app):
    app.add_stylesheet("my-styles.css")
