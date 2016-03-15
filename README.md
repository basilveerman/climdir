# cfmeta

[![Build Status](https://travis-ci.org/pacificclimate/cfmeta.svg?branch=master)](https://travis-ci.org/pacificclimate/cfmeta)
[![Code Health](https://landscape.io/github/pacificclimate/cfmeta/master/landscape.svg?style=flat)](https://landscape.io/github/pacificclimate/cfmeta/master)

cfmeta is a basic utility for generating and parsing CMIP5 file paths.

## Requirements

For basic functionality cfmeta has no special requirements.  The `netCDF` option requires the [netCDF4](http://unidata.github.io/netcdf4-python/) package.

## Installing cfmeta

cfmeta can be installed from the Python package index:

```bash
pip install cfmeta[netCDF]
```

from Github:

```bash
pip install git+git://https://github.com/basilveerman/cfmeta#egg=cfmeta
```

## Usage

Documentation is hosted at [ReadTheDocs](http://cfmeta.readthedocs.org/en/latest/)

## Contributing

### Generating Documentation

Generated using the `make doc` command

If required, documentation can be updated on gh-pages as such:

```bash
git branch -D gh-pages
git branch -D draft
git checkout -b draft
git add -f doc/build/html
git commit -am"Deploy docs on gh-pages"
git subtree split --prefix doc/build/html -b gh-pages
git push -f origin gh-pages:gh-pages
git checkout master
```

## Releasing

1. Build updated api docs and commit any changes
   ```bash
echo <VERSION_NUMBER> > VERSION.txt
make doc
git add doc/source/*.rst
git commit -m"Update api docs"
git add VERSION.txt
git commit -m"Bump to version <VERSION_NUMBER>"
git tag -am"<VERSION_NUMBER>" <VERSION_NUMBER>
git push --follow-tags
```
