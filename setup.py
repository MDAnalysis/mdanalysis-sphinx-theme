# -*- coding: utf-8 -*-

import re
from setuptools import setup, find_namespace_packages
from pathlib import Path
import shutil
import warnings
import versioneer


def dynamic_author_list():
    """Generate __authors__ from AUTHORS

    This function generates authors.py that contains the list of the
    authors from the AUTHORS file. This avoids having that list maintained in
    several places. Note that AUTHORS is sorted chronologically while we want
    __authors__ in authors.py to be sorted alphabetically.

    The authors are written in AUTHORS as bullet points under the
    "Chronological list of authors" title.
    """
    authors = []
    current_dir = Path(__file__).parent.resolve()
    author_file = current_dir / "AUTHORS.md"

    with open(author_file, "r") as f:
        lines = [x.strip() for x in f.readlines()]

    pattern = r"^- ([\w '.]+) @[\w_-]+$"
    for line in lines:
        match = re.match(pattern, line)
        if match:
            authors.append(match.group(1))

    authors.sort(key=lambda name: name.split()[-1])
    authors.remove("Lily Wang")
    prior_authors = [
        "Matthew Harrigan",
        "Robert T. McGibbon",
        "Christian Schwantes",
        "Martin K. Scherer",
        "Joshua A. Mitchell",
        "Simon Boothroyd",
    ]
    for name in prior_authors:
        authors.remove(name)

    authors = ["Lily Wang"] + authors

    # Write the authors.py file.
    out_path = current_dir / "mdanalysis_sphinx_theme" / "authors.py"
    author_lines = "\n".join([f'    u"{name}",' for name in authors])
    template = f"""\
#-*- coding:utf-8 -*-

# This file is generated from the AUTHORS file during the installation process.
# Do not edit it as your changes will be overwritten.

__authors__ = [
{author_lines}
]
"""

    with out_path.open("w") as f:
        f.write(template)


def copy_mda_assets():
    static_dir = Path('.') / 'mdanalysis_sphinx_theme' / 'static'
    branding_dir = Path('.') / 'branding'

    # outdir for logos and icons
    static_logos = static_dir / 'logo'

    # main logo to appear in nav bar
    mda_logo_base_file = 'mdanalysis-logo_bgwhite@600ppi.png'
    mda_logo = branding_dir / 'logos' / 'rastered' / mda_logo_base_file

    mda_favicon = branding_dir / 'logos' / 'icons' / 'mdanalysis-logo.ico'

    if not mda_logo.exists():
        raise FileNotFoundError("Could not find the MDAnalysis logo. "
                                "Check that the branding submodule is "
                                "initialized.")

    if not mda_favicon.exists():
        raise FileNotFoundError("Could not find the MDAnalysis icon. "
                                "Check that the branding submodule is "
                                "initialized.")

    if not static_dir.exists():
        raise FileNotFoundError("Could not find the theme static directory.")

    shutil.copy(mda_logo, static_logos / 'mda_logo.png')
    shutil.copy(mda_favicon, static_logos / 'mda_favicon.ico')


if __name__ == '__main__':
    try:
        dynamic_author_list()
    except (OSError, IOError):
        warnings.warn('Cannot write the list of authors.')

    copy_mda_assets()

    setup(
        name='mdanalysis_sphinx_theme',
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
        url='https://github.com/mdanalysis/mdanalysis-sphinx-theme/',
        license='MIT',
        author='MDAnalysis',
        author_email='mdanalysis@numfocus.org',
        description='Modification to sphinx_rtd_theme',
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        zip_safe=False,
        packages=find_namespace_packages(),
        package_data={'mdanalysis_sphinx_theme': [
            'theme.conf',
            '*.html',
            'static/*/*.*',
            'sass/*.*',
            'sass/*/*.*',
            'sass/bulma/sass/*/*.*',
            'branding/*',
            'branding/*/*',
            'branding/*/*/*'
        ]},
        include_package_data=True,
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'License :: OSI Approved :: MIT License',
            'Environment :: Console',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'Programming Language :: Python :: 3',
            'Operating System :: OS Independent',
            'Topic :: Documentation',
            'Topic :: Software Development :: Documentation',
        ],
        python_requires='>=3.9',
        install_requires=[
            'sphinx_rtd_theme>=1.3',
            'sphinx>=6.2.1',
            'beautifulsoup4',
            'python-slugify[unidecode]',
            'css_html_js_minify',
            'lxml',
            'libsass'
        ],
        entry_points={
            'sphinx.html_themes': [
                'mdanalysis_sphinx_theme = mdanalysis_sphinx_theme',
            ]
        }
    )
