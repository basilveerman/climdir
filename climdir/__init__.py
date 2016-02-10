# -*- coding: utf-8 -*-

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
    """

    return {}

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