# -*- coding: utf-8 -*-

from setuptools import setup
import versioneer

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
    entry_points = {
        'sphinx.html_themes': [
            'mdanalysis_sphinx_theme = mdanalysis_sphinx_theme',
        ]
    }
)
