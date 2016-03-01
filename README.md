# cmme

[![Build Status](https://travis-ci.org/pacificclimate/cmme.svg?branch=master)](https://travis-ci.org/pacificclimate/cmme)
[![Code Health](https://landscape.io/github/pacificclimate/cmme/master/landscape.svg?style=flat)](https://landscape.io/github/pacificclimate/cmme/master)

cmme is a basic utility for generating and parsing CMIP5 file paths.

## Requirements

For basic functionality cmme has no special requirements.  The `netCDF` option requires the [netCDF4](http://unidata.github.io/netcdf4-python/) package.

## Installing cmme

cmme can be installed from the Python package index:

```bash
pip install cmme[netCDF]
```

from Github:

```bash
pip install git+git://https://github.com/basilveerman/cmme#egg=cmme
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