# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
import sys
# sys.path.insert(0, os.path.abspath('.'))
if sys.platform == 'win32':
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# -- Project information -----------------------------------------------------

project = 'mermaid'
copyright = '2021, xinetzone'
author = 'xinetzone'

# The full version, including alpha/beta/rc tags
release = '0.0.1'

extensions = [
    "sphinx_book_theme",
    "myst_nb",
    "sphinx_copybutton",
    "sphinxcontrib.mermaid",
    # "sphinx.ext.todo",
    # "sphinxcontrib.bibtex",
    # "sphinx_togglebutton",
    # "sphinx.ext.viewcode",
    # "sphinx.ext.autodoc",
    # "sphinx.ext.doctest",
    # "sphinx_design",
    # "sphinx.ext.ifconfig",
    # "sphinx_automodapi.automodapi",
    # "sphinxext.opengraph",
]

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build', 'Thumbs.db', '.DS_Store',
    'docs/_navbar.md', 'docs/_sidebar.md',
    'src/dagre-wrapper/GraphObjects.md', 'todo.md',
    '.github/*'
]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
# html_css_files = ["theme_themed.css", "theme.css"]

# MyST NB 设置
nb_render_priority = {
    "html": (
        "application/vnd.jupyter.widget-view+json",
        "application/javascript",
        "text/html",
        "image/svg+xml",
        "image/png",
        "image/jpeg",
        "text/markdown",
        "text/latex",
        "text/plain",
    ),
    'gettext': ()
}

html_theme_options = {
    "path_to_docs": "web/",
    "repository_url": "https://github.com/daobook/mermaid",
    "repository_branch": "main",
    "use_issues_button": True,
    "use_download_button": True,
    "use_edit_page_button": True,
    "use_fullscreen_button": True,
    "use_repository_button": True,
    "home_page_in_toc": False,
    "toc_title": "导航",
    "launch_buttons": {
        # https://mybinder.org/v2/gh/daobook/daobook.github.io/main
        "binderhub_url": "https://mybinder.org",
        # "jupyterhub_url": "https://datahub.berkeley.edu",  # For testing
        "colab_url": "https://colab.research.google.com/",
        # 你可以控制有人点击启动按钮时打开的界面。
        "notebook_interface": "jupyterlab",
        # "thebe": True,  # Thebe 实时代码单元格
    },
}