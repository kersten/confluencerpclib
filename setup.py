import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'confluencerpclib',
    version = '0.1',
    url = 'http://github.com/kersten/confluencerpclib',
    license = 'original BSD license',
    description = 'A python library to connect to Confluence wiki.',
    long_description = read('README'),

    author = 'Kersten Burkhardt',
    author_email = 'kerstenk@gmail.com',

    packages = find_packages('src'),
    package_dir = {'': 'src'},

    install_requires = ['setuptools'],

    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: original BSD license',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],

    entry_points = {})
