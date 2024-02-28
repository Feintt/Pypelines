from setuptools import setup, find_packages
from codecs import open
from os import path

# Current directory
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pypelines',
    version='0.1.1',
    packages=find_packages(),
    description='A simple library to introduce functional programming concepts in python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Feintt',
    url='https://github.com/Feintt/python-pipeline',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent"
        "Intended Audience :: Developers",
    ],
    include_package_data=True,
)
