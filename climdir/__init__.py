# -*- coding: utf-8 -*-

def get_cmor_fp_meta():
    """Processes a CMOR style file path.
    """
    raise NotImplemented

def get_datanode_fp_meta():
    """Processes a datanode style file path.
    """
    raise NotImplemented

def get_cmor_fname_meta():
    """Processes a CMOR style file name.
    """
    raise NotImplemented

class Cmip5File():
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
        raise NotImplemented