import sys

sys.modules["uwsgi"] = sys

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.ifconfig",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]
source_suffix = ".rst"
master_doc = "index"
project = "Django uWSGI Cache"
year = "2014-2025"
author = "Ionel Cristian Mărieș"
copyright = f"{year}, {author}"
version = release = "1.1.0"

pygments_style = "trac"
templates_path = ["."]
extlinks = {
    "issue": ("https://github.com/ionelmc/django-uwsgi-cache/issues/%s", "#%s"),
    "pr": ("https://github.com/ionelmc/django-uwsgi-cache/pull/%s", "PR #%s"),
}

html_theme = "furo"
html_theme_options = {
    "source_repository": "https://github.com/ionelmc/django-uwsgi-cache/",
    "source_branch": "main",
    "source_directory": "docs/",
    "footer_icons": [
        {
            "url": "https://github.com/ionelmc/django-uwsgi-cache/",
            "html": "github.com/ionelmc/django-uwsgi-cache",
        },
    ],
}

html_use_smartypants = True
html_last_updated_fmt = "%b %d, %Y"
html_split_index = False
html_short_title = f"{project}-{version}"

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False
