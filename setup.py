import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pytest-rage',
    license='MIT',
    description='pytest plugin to implement PEP712',
    long_description=read("README.rst"),
    version='0.1',
    author='Leonardo Santagada',
    author_email='santagada@gmail.com',
    url='http://github.com/santagada/pytest-rage/',
    py_modules=['pytest_rage'],
    entry_points={'pytest11': ['rage = pytest_rage']},
    install_requires=['pytest>=2.0'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Testing',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        ]
)
