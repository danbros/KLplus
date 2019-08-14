from setuptools import setup, find_packages
from os.path import join, dirname


base_dir = dirname(__file__)
about = {}

with open(join(base_dir, 'KLplus', '__about__.py')) as f:
    exec(f.read(), about)

with open(join(base_dir, "README.rst")) as f:
    long_d = f.read()


setup(
    name = about['__name__'],
    version = about['__version__'],

    description = about['__summary__'],
    long_description = long_d,
    license = about['__license__'],
    url = about['__uri__'],

    author = about['__author__'],
    author_email = about['__email__'],

    platforms = ['Linux'], # Somente para metadados

    packages = find_packages(),
    install_requires = ['python-xlib==0.25'],
    dependency_links = [
        'https://github.com/python-xlib/python-xlib/archive/0.25.tar.gz'
    ],
    # dependency_links = [
    #     'https://github.com/python-xlib/python-xlib/tarball/master#egg=python-xlib-0.25'
    # ],
    zip_safe = False,

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython'
        'Topic :: System :: Monitoring',
        'Topic :: System :: Logging',
    ]
)