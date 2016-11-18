#!/usr/bin/env python
"""EUFAR Metadata Cretator.

The goal of the EUFAR Metadata Creator is to produce 
metadata to facilitate data storage and searches for 
Airborne Scientific Campaigns. 

This utility is maintained by EUFAR.
"""
from ui._version import _version


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

classifiers = """\
Development Status :: 5 - Production/Stable
Environment :: X11 Applications :: Qt
Environment :: Win32 (MS Windows)
Intended Audience :: Developers
Intended Audience :: Education
Intended Audience :: Science/Research
License :: OSI Approved :: BSD License
Natural Language :: English
Programming Language :: Python :: 3.5
Topic :: Scientific/Engineering :: Atmospheric Science
Topic :: Text Processing :: Markup :: XML
"""

doclines = __doc__.split('\n')

setup(name='eufar_metadata_creator',
      version=_version,
      description=doclines[0],
      long_description='\n'.join(doclines[2:]),
      author='EUFAR',
      author_email='bureau@eufar.net',
      maintainer='Olivier Henry',
      maintainer_email='olivier.henry@meteo.fr',
      url='http://www.eufar.net',
      download_url='https://github.com/eufarn7sp/emc-eufar',
      license='New BSD License',
      keywords=['airbornescience', 'xml', 'eufar', 'science', 'metadata'],
      packages=['Documentation','eufar_aircrafts','fonts','functions','icons','sqlite','ui'],
      classifiers=filter(None, classifiers.split("\n")),
      requires=['PyQt5']
      )

