# -*- coding: utf-8 -*-

import os.path
# import warnings

ATTR_KEYS = [
    'activity',
    'product',
    'institute',
    'model',
    'experiment',
    'frequency',
    'modeling_realm',
    'mip_table',
    'ensemble_member',
    'version_number',
    'variable_name',
    'temporal_subset',
    'geographical_info'
]

CMOR_FNAME_REQUIRED_ATTS = ['variable_name','mip_table','model','experiment','ensemble_member']
CMOR_FNAME_OPTIONAL_ATTS = ['temporal_subset', 'geographical_info']

CMOR_FP_ATTS = [
    'activity',
    'product',
    'institute',
    'model',
    'experiment',
    'frequency',
    'modeling_realm',
    'variable_name',
    'ensemble_member',
]

DATANODE_FP_ATTS = [
    'activity',
    'product',
    'institute',
    'model',
    'experiment',
    'frequency',
    'modeling_realm',
    'mip_table',
    'ensemble_member',
    'version_number',
    'variable_name',
]

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

    # Copy metadata list since it will be modified
    directory_meta = list(CMOR_FP_ATTS)

    dirname, basename = os.path.split(fp)
    meta = dirname.split('/')

    res = {}

    # Extract meta starting at end of array
    directory_meta.reverse()
    try:
        for key in directory_meta:
            res[key] = meta.pop()
    except IndexError:
        raise Exception('Directory structure {} does not match CMOR spec'.format(dirname))

    # Prefer meta extracted from filename
    res.update(get_cmor_fname_meta(basename))

    return res

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

    # Copy metadata list since it will be modified
    directory_meta = list(DATANODE_FP_ATTS)

    dirname, basename = os.path.split(fp)
    meta = dirname.split('/')

    res = {}

    # Extract meta starting at end of array
    directory_meta.reverse()
    try:
        for key in directory_meta:
            res[key] = meta.pop()
    except IndexError:
        raise Exception('Directory structure {} does not match CMOR spec'.format(dirname))

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

    mandatory_meta = ['variable_name','mip_table','model','experiment','ensemble_member']

    fname, ext = os.path.splitext(fname)
    meta = fname.split('_')

    res = {}

    try:
        for key in mandatory_meta:
            res[key] = meta.pop(0)
    except IndexError:
        raise Exception('Filename {} does not match CMOR spec'.format(fname))

    # Determine presence and order of optional metadata
    if len(meta) > 2:
        raise Exception('Filename {} does not match CMOR spec'.format(fname))

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

    def __init__(self,
                 cmor_fp = None,
                 datanode_fp = None,
                 cmor_fname = None,
                 **kwargs):
        """Initializes a Cmip5File.

        """

        # Initialize with file path
        if cmor_fp:
            self.__dict__.update(get_cmor_fp_meta(cmor_fp))
        elif datanode_fp:
            self.__dict__.update(get_datanode_fp_meta(datanode_fp))
        elif cmor_fname:
            self.__dict__.update(get_cmor_fname_meta(cmor_fname))

        self._update_known_atts(**kwargs)

    def __repr__(self):
        s = "Cmip5File("
        args = ", ".join(["{} = '{}'".format(k, v) for k, v in self.__dict__.items() if k in ATTR_KEYS])
        s += args + ")"
        return s

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def _update_known_atts(self, **kwargs):
        for k, v in kwargs.items():
            if k not in ATTR_KEYS:
                # Warn if passed in unknown kwargs
                raise SyntaxWarning('Unknown argument: {}'.format(k))
            else:
                setattr(self, k, v)

    def update(self, **kwargs):
        """Update the Cmip5File instance with new attributes.
        """

        self._update_known_atts(**kwargs)

    @property
    def cmor_fname(self):
        """Generates a CMOR filename from object attributes.
        """

        return '_'.join(
            [getattr(self, x) for x in CMOR_FNAME_REQUIRED_ATTS] +
            [getattr(self, x) for x in CMOR_FNAME_OPTIONAL_ATTS if x in self.__dict__]
        ) + '.nc'

    @property
    def cmor_fp(self):
        """Generates a standard CMOR file path from object attributes
        """

        return os.path.join(*[getattr(self, x) for x in CMOR_FP_ATTS] + [self.cmor_fname])

    @property
    def datanode_fp(self):
        """Generates a datanode extended CMOR file path from object attributes
        """

        return os.path.join(*[getattr(self, x) for x in DATANODE_FP_ATTS] + [self.cmor_fname])
