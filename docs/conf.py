# docs/conf.py

project = "reportrabbit"
author = "Raghav Gupta"

extensions = [
    "myst_parser",
    "autoapi.extension",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

# AutoAPI: point to your src/ layout
autoapi_dirs = ["../src"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Theme (you already depend on pydata-sphinx-theme)
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
