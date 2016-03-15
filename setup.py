import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "cfmeta",
    version =read('VERSION.txt'),
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
