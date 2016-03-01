# -*- coding: utf-8 -*-

import os.path

from .exceptions import PathError
from .path import get_cmor_fp_meta, get_datanode_fp_meta, get_cmor_fname_meta

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
    'geographical_info',
    't_start',
    't_end',
    'temporal_suffix'
]


class CmipFile(object):
    def __init__(self, **kwargs):
        print kwargs
        self.update(**kwargs)

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
        """Updates instance attributes with supplied keyword arguments.
        """
        for k, v in kwargs.items():
            if k not in ATTR_KEYS:
                # Warn if passed in unknown kwargs
                raise SyntaxWarning('Unknown argument: {}'.format(k))
            elif not v: # Delete attributes with falsey values
                delattr(self, k)
            else:
                setattr(self, k, v)

    def update(self, **kwargs):
        """Updates instance attributes with supplied keyword arguments.

        If a supplied value is falsey, the attribute will be deleted.

        Arguments:
            **kwargs (dict): keyword arguments to update instance with

        Raises:
            SyntaxWarning: If a supplied key is not recognized as valid metadata
        """

        self._update_known_atts(**kwargs)

    def delete(self, *args):
        """Delete instance metadata by attribute name.
        """

        self._update_known_atts(**{k: False for k in args})

    # Temporal subset elements
    def set_timeval(self, index, value):
        if self.temporal_subset:
            l = self.temporal_subset.split('-')
            l[index] = value
            self.temporal_subset = '-'.join(l)

    @property
    def t_start(self):
        if self.temporal_subset:
            return self.temporal_subset.split('-')[0]

    @t_start.setter
    def t_start(self, value):
        self.set_timeval(0, value)

    @property
    def t_end(self):
        if self.temporal_subset:
            return self.temporal_subset.split('-')[1]

    @t_end.setter
    def t_end(self, value):
        self.set_timeval(1, value)

    @property
    def temporal_suffix(self):
        if self.temporal_subset and len(self.temporal_subset.split('-')) > 2:
            return self.temporal_subset.split('-')[2]
        else:
            return None

    @temporal_suffix.setter
    def temporal_suffix(self, value):
        if self.temporal_subset:
            l = self.temporal_subset.split('-')
            if self.temporal_suffix: # Replace temporal_suffix if exists, else append to temporal_subset
                l[2] = value
            else:
                l.append(value)

            self.temporal_subset = '-'.join(l)

    def get_joined_dir_name(self, atts):
        """Returns a joined path populated with the supplied attribute names
        """

        return os.path.join(*[getattr(self, x) for x in atts])

    def get_joined_file_name(self, atts, optional_atts = None):
        """Returns a joined path populated with the supplied attribute names
        """

        return '_'.join(
            [getattr(self, x) for x in atts] +
            [getattr(self, x) for x in optional_atts if x in self.__dict__]
        ) + '.nc'


CMIP5_FNAME_REQUIRED_ATTS = ['variable_name','mip_table','model','experiment','ensemble_member']
CMIP5_FNAME_OPTIONAL_ATTS = ['temporal_subset', 'geographical_info']

CMIP5_FP_ATTS = [
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

CMIP5_DATANODE_FP_ATTS = [
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

class Cmip5File(CmipFile):
    """Represents a Cmip5File.

    Metadata is parsed based on interpreting the following documentation as best as possible:

    - `Metadata requirements`_
    - `Data Reference Syntax`_
    - `Standard Output (CMOR Tables)`_

    .. _Metadata Requirements:
       http://cmip-pcmdi.llnl.gov/cmip5/docs/CMIP5_output_metadata_requirements.pdf
    .. _Data Reference Syntax:
       http://cmip-pcmdi.llnl.gov/cmip5/docs/cmip5_data_reference_syntax.pdf
    .. _Standard Output (CMOR Tables):
       http://cmip-pcmdi.llnl.gov/cmip5/docs/standard_output.pdf

    """

    def __init__(self,
                 cmor_fp = None,
                 datanode_fp = None,
                 cmor_fname = None,
                 **kwargs):
        """Initializes a Cmip5File.

        """

        meta = {}

        # Initialize with file path
        if cmor_fp:
            meta.update(get_cmor_fp_meta(cmor_fp))
        elif datanode_fp:
            meta.update(get_datanode_fp_meta(datanode_fp))
        elif cmor_fname:
            meta.update(get_cmor_fname_meta(cmor_fname))

        meta.update(kwargs)

        super(Cmip5File, self).__init__(**meta)

    # Path generators
    @property
    def cmor_fname(self):
        """Generates a CMOR filename from object attributes.
        """

        return self.get_joined_file_name(CMIP5_FNAME_REQUIRED_ATTS, CMIP5_FNAME_OPTIONAL_ATTS)

    @property
    def cmor_fp(self):
        """Generates a standard CMOR file path from object attributes
        """

        return self.get_joined_dir_name(CMIP5_FP_ATTS)

    @property
    def datanode_fp(self):
        """Generates a datanode extended CMOR file path from object attributes
        """

        return self.get_joined_dir_name(CMIP5_DATANODE_FP_ATTS)
