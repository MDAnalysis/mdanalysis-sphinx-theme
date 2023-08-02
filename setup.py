# -*- coding: utf-8 -*-

from setuptools import setup
from pathlib import Path
import shutil
import versioneer


def copy_mda_assets():
    static_dir = Path('.') / 'mdanalysis_sphinx_theme' / 'static'
    branding_dir = Path('.') / 'branding'

    # outdir for logos and icons
    static_logos = static_dir / 'logo'

    # main logo to appear in nav bar
    mda_logo: Path = branding_dir / 'logos' /\
                                    'rastered' /\
                                    'mdanalysis-logo_bgwhite@600ppi.png'

    mda_favicon = branding_dir / 'logos' /\
                                 'icons' /\
                                 'mdanalysis-logo.ico'

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


copy_mda_assets()


setup(
    name='mdanalysis_sphinx_theme',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    url='https://github.com/lilyminium/mdanalysis-sphinx-theme/',
    license='MIT',
    author='MDAnalysis',
    author_email='mdanalysis@numfocus.org',
    description='Modification to sphinx_rtd_theme',
    zip_safe=False,
    packages=['mdanalysis_sphinx_theme'],
    package_data={'mdanalysis_sphinx_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/logo/*',
        'sass/*.*',
        'sass/*/*.*',
        'sass/bulma/sass/*/*.*',
    ]},
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
    install_requires=['sphinx_rtd_theme'],
    entry_points={
        'sphinx.html_themes': [
            'mdanalysis_sphinx_theme = mdanalysis_sphinx_theme',
        ]
    }
)
