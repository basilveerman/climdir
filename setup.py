import os
from setuptools import setup, find_packages

__version__ = '0.0.2'

setup(
    name = "cfmeta",
    version = __version__,
    author = "Basil Veerman",
    author_email = "bveerman@uvic.ca",
    license = "GPL-3.0",
    keywords = "",
    description = ("Utility for processing CF metadata"),
    url = "http://www.pacificclimate.org/",
    packages = find_packages('.'),
    extras_require = {
        'netCDF': ['netCDF4'],
    },
    zip_safe = True,
    )
