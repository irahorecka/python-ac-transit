"""Setup for the actransit package."""

import setuptools


with open('README.rst') as f:
    README = f.read()

setuptools.setup(
    author="Ira Horecka",
    author_email="ira89@icloud.com",
    name='python-actransit',
    license="MIT",
    description='Simple Alameda-Contra Costa Transit District (AC Transit) API wrapper',
    version='v0.1.1',
    long_description=README,
    url='https://github.com/irahorecka/python-actransit',
    packages=['actransit'],
    python_requires=">=3.5",
    install_requires=['requests', 'gtfs-realtime-bindings', 'protobuf3-to-dict'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)