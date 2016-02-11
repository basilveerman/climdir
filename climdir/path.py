# -*- coding: utf-8 -*-

import os

import climdir

from .exceptions import PathError

"""Cmip5 path operations

This module provides parsers for a variety of Cmip5 file path formats
"""

def get_cmor_fp_meta(fp):
    """Processes a CMOR style file path.

    Section 3.1 of the `Data Reference Syntax`_ details:

        The standard CMIP5 output tool CMOR optionally writes output files
        to a directory structure mapping DRS components to directory names as:
            <activity>/<product>/<institute>/<model>/<experiment>/<frequency>/
            <modeling_realm>/<variable_name>/<ensemble_member>/<CMOR filename>.nc

    Arguments:
        fp (str): A file path conforming to DRS spec.

    Returns:
        dict: Metadata as extracted from the file path.

    .. _Data Reference Syntax:
       http://cmip-pcmdi.llnl.gov/cmip5/docs/cmip5_data_reference_syntax.pdf
    """

    # Copy metadata list then reverse to start at end of path
    directory_meta = list(climdir.CMOR_FP_ATTS)
    directory_meta.reverse()

    return get_cmor_dir_meta(fp, directory_meta)

def get_datanode_fp_meta(fp):
    """Processes a datanode style file path.

    Section 3.2 of the `Data Reference Syntax`_ details:

        It is recommended that ESGF data nodes should layout datasets
        on disk mapping DRS components to directories as:
            <activity>/<product>/<institute>/<model>/<experiment>/
            <frequency>/<modeling_realm>/<mip_table>/<ensemble_member>/
            <version_number>/<variable_name>/<CMOR filename>.nc

    Arguments:
        fp (str): A file path conforming to DRS spec.

    Returns:
        dict: Metadata as extracted from the file path.

    .. _Data Reference Syntax:
       http://cmip-pcmdi.llnl.gov/cmip5/docs/cmip5_data_reference_syntax.pdf
    """

    # Copy metadata list then reverse to start at end of path
    directory_meta = list(climdir.DATANODE_FP_ATTS)
    directory_meta.reverse()

    return get_cmor_dir_meta(fp, directory_meta)

def get_cmor_dir_meta(fp, atts):
    """Pop path information and map to supplied atts
    """

    dirname, basename = os.path.split(fp)
    meta = dirname.split('/')

    res = {}

    try:
        for key in atts:
            res[key] = meta.pop()
    except IndexError:
        raise PathError(dirname)

    # Prefer meta extracted from filename
    res.update(get_cmor_fname_meta(basename))

    return res

def get_cmor_fname_meta(fname):
    """Processes a CMOR style file name.

    Section 3.3 of the `Data Reference Syntax`_ details:

        filename = <variable name>_<mip_table>_<model>_<experiment>_
            <ensemble_member>[_<temporal_subset>][_<geographical_info>].nc

    Temporal subsets are detailed in section 2.4:

        Time instants or periods will be represented by a construction
        of the form “N1-N2”, where N1 and N2 are of the form
        ‘yyyy[MM[dd[hh[mm[ss]]]]][-suffix]’, where ‘yyyy’, ‘MM’, ‘dd’,
        ‘hh’ ‘mm’ and ‘ss’ are integer year, month, day, hour, minute,
        and second, respectively, and the precision with which time is
        expressed must unambiguously resolve the interval between
        timesamples contained in the file or virtual file

    Geographic subsets are also detailed in section 2.4:

        The DRS specification for this indicator is a string of the
        form g-XXXX[-YYYY]. The “g-” indicates that some spatial selection
        or processing has been done (i.e., selection of a sub-global region
        and possibly spatial averaging).

    Arguments:
        fname (str): A file name conforming to DRS spec.

    Returns:
        dict: Metadata as extracted from the filename.

    .. _Data Reference Syntax:
       http://cmip-pcmdi.llnl.gov/cmip5/docs/cmip5_data_reference_syntax.pdf
    """

    fname, ext = os.path.splitext(fname)
    meta = fname.split('_')

    res = {}

    try:
        for key in climdir.CMOR_FNAME_REQUIRED_ATTS:
            res[key] = meta.pop(0)
    except IndexError:
        raise PathError(fname)

    # Determine presence and order of optional metadata
    if len(meta) > 2:
        raise PathError(fname)

    is_geo = lambda x: x[0] == 'g'

    for key in meta:
        if is_geo(key):
            res['geographical_info'] = key
        else:
            res['temporal_subset'] = key

    return res
