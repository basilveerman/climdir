# -*- coding: utf-8 -*-

import os.path

def get_cmor_fp_meta(fp):
    """Processes a CMOR style file path.
    """

    return {}

def get_datanode_fp_meta(fp):
    """Processes a datanode style file path.
    """

    return {}

def get_cmor_fname_meta(fname):
    """Processes a CMOR style file name.

    Section 3.3 of the `Data Reference Syntax`_ details:

        filename = <variable name>_<MIP table>_<model>_<experiment>_
            <ensemble member>[_<temporal subset>][_<geographical_info>].nc

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

    mandatory_meta = ['variable_name','mip_table','model','experiment','ensemble_member']

    fname, ext = os.path.splitext(fname)
    meta = fname.split('_')

    res = {}

    try:
        for key in mandatory_meta:
            res[key] = meta.pop(0)
    except IndexError:
        raise Exception('Filename {} does not match CMOR spec')

    # Determine presence and order of optional metadata
    if len(meta) > 2:
        raise Exception('Filename {} does not match CMOR spec')

    is_geo = lambda x: x[0] == 'g'

    for key in meta:
        if is_geo(key):
            res['geographical_info'] = key
        else:
            res['temporal_subset'] = key

    return res

class Cmip5File:
    """Represents a Cmip5File.

    .. _Metadata Requirements:
       http://cmip-pcmdi.llnl.gov/cmip5/docs/CMIP5_output_metadata_requirements.pdf
    .. _Data Reference Syntax:
       http://cmip-pcmdi.llnl.gov/cmip5/docs/cmip5_data_reference_syntax.pdf
    .. _Standard Output (CMOR Tables):
       http://cmip-pcmdi.llnl.gov/cmip5/docs/standard_output.pdf

    Metadata is parsed based on interpreting the following documentation as best as possible::

    - `Metadata requirements`_
    - `Data Reference Syntax`_
    - `Standard Output (CMOR Tables)`_

    """

    def __init__(self, cmor_fp = None, datanode_fp = None, **kwargs):
        """Initializes a Cmip5File.
        """
        raise NotImplementedError