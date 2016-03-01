import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "cmme",
    version =read('VERSION.txt'),
    author = "Basil Veerman",
    author_email = "bveerman@uvic.ca",
    description = ("Utility for generating and parsing CMIP5 file paths"),
    url = "http://www.pacificclimate.org/",
    packages = find_packages('.'),
    extras_require = {
        'netCDF': ['netCDF4'],
    },
    )
