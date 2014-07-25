# -*- encoding: utf8 -*-
from setuptools import setup, find_packages

import os

setup(
    name = "django-uwsgi-cache",
    version = "0.2",
    url = 'https://github.com/ionelmc/django-uwsgi-cache',
    download_url = '',
    license = 'BSD',
    description = "uWSGI cache backend.",
    long_description = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    maintainer = 'Ionel Cristian Mărieș',
    maintainer_email = 'contact@ionelmc.ro',
    packages = find_packages('src'),
    package_dir = {'':'src'},
    py_modules = ['uwsgicache'],
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        'Django',
        'uWSGI',
    ]
)
