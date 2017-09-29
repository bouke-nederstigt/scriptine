from setuptools import setup
import os

name = "scriptinep3"
version = "0.3.1"

setup(
    name = name,
    version = version,
    author = "Oliver Tonnhofer",
    author_email = "",
    description = 'python shell scripts made easy - scriptine Ported to python 3',
    long_description=open('README.rst').read() +'\n' + open('CHANGELOG.txt').read(),
    license = 'MIT License',
    url = 'https://github.com/bouke-nederstigt/scriptine',
    classifiers=[
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python',
      ],
    packages = ['scriptine'],
    install_requires=[
        "wrapt"
    ],
    zip_safe = False
)
