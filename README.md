# climdir

![Travis CI](https://travis-ci.org/pacificclimate/climdir.svg?branch=master)
[![Code Climate](https://codeclimate.com/github/pacificclimate/climdir/badges/gpa.svg)](https://codeclimate.com/github/pacificclimate/climdir)

climdir is a basic utility for generating and parsing CMIP5 file paths.

## Requirements

For basic functionality climdir has no special requirements.  The `netCDF` option requires the [netCDF4](http://unidata.github.io/netcdf4-python/) package.

## Installing climdir

climdir can be installed from the Python package index:

```bash
pip install climdir[netCDF]
```

from Github:

```bash
pip install git+git://https://github.com/basilveerman/climdir#egg=climdir
```

## Usage

To Document...

## Documentation

Generated using Sphinx

```bash
cd doc
sphinx-apidoc -f -o source ..
make html
```