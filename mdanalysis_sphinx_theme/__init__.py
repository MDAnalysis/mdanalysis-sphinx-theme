"""MDAnalysis Sphinx theme."""

import hashlib
import inspect
import os
import sys
from multiprocessing import Manager
from pathlib import Path
from typing import List, Optional
from xml.etree import ElementTree

import bs4
import sass
import slugify
from bs4 import BeautifulSoup
from css_html_js_minify.html_minifier import html_minify
from sass import SassColor
from sphinx.util import console, logging
import sphinx

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions

ROOT_SUFFIX = "--page-root"


def setup(app):
    """Setup connects events to the sitemap builder"""
    app.site_pages = []
    app.add_html_theme(
        "mdanalysis_sphinx_theme", html_theme_path()[0]
    )
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def set_default_settings(app, config):
    if not config.html_sidebars:
        config.html_sidebars["**"] = [
            "globaltoc.html",
            "localtoc.html",
            "searchbox.html",
        ]
    if config.html_permalinks_icon == "¶":
        config.html_permalinks_icon = "<i class='fas fa-link'></i>"


def html_theme_path():
    return [os.path.dirname(os.path.abspath(__file__))]


def ul_to_list(node: bs4.element.Tag, fix_root: bool, page_name: str) -> List[dict]:
    out = []
    for child in node.find_all("li", recursive=False):
        if callable(child.isspace) and child.isspace():
            continue
        formatted = {}
        if child.a is not None:
            formatted["href"] = child.a["href"]
            formatted["contents"] = "".join(map(str, child.a.contents))
            if fix_root and formatted["href"] == "#" and child.a.contents:
                slug = slugify.slugify(page_name) + ROOT_SUFFIX
                formatted["href"] = "#" + slug
            formatted["current"] = "current" in child.a.get("class", [])
        if child.ul is not None:
            formatted["children"] = ul_to_list(child.ul, fix_root, page_name)
        else:
            formatted["children"] = []
        out.append(formatted)
    return out


def derender_toc(
    toc_text, fix_root=True, page_name: str = "md-page-root--link"
) -> List[dict]:
    nodes = []
    try:
        toc = BeautifulSoup(toc_text, features="html.parser")
        for child in toc.children:
            if callable(child.isspace) and child.isspace():
                continue
            if child.name == "p":
                nodes.append({"caption": "".join(map(str, child.contents))})
            elif child.name == "ul":
                nodes.extend(ul_to_list(child, fix_root, page_name))
            else:
                raise NotImplementedError
    except Exception as exc:
        logger = logging.getLogger(__name__)
        logger.warning(
            "Failed to process toctree_text\n" + str(exc) + "\n" + str(toc_text)
        )

    return nodes


# These final lines exist to give sphinx a stable str representation of
# this function across runs, and to ensure that the str changes
# if the source does.
derender_toc_src = inspect.getsource(derender_toc)
derender_toc_hash = hashlib.sha512(derender_toc_src.encode()).hexdigest()


class DerenderTocMeta(type):
    def __repr__(self):
        return f"derender_toc, hash: {derender_toc_hash}"

    def __str__(self):
        return f"derender_toc, hash: {derender_toc_hash}"


class DerenderToc(object, metaclass=DerenderTocMeta):
    def __new__(cls, *args, **kwargs):
        return derender_toc(*args, **kwargs)


def get_html_context():
    return {"derender_toc": DerenderToc}
