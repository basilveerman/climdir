# -*- coding: utf-8 -*-

"""A Python package to interact with CMIP file based metadata.

The ``climdir`` package makes it easy to extract standard CMIP metadata
from CMIP3/5 NetCDF filepaths and/or the metadata contained in the NetCDF
file itself. Metadata can be manipulated with a simple interface, and
CMIP3/5 compliant file paths generated from a metadata collection.

"""

from .path import get_dir_meta
from .cmip5file import Cmip5File, get_cmor_fp_meta, get_datanode_fp_meta, get_cmor_fname_meta
from .cmip3file import Cmip3File