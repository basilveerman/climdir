import pytest

from cmme import Cmip3File
from cmme.exceptions import PathError

## Cmip3File instantiation
def test_can_inst_cmip3file_from_fp(cmip3_fp):
    cf = Cmip3File(fp = cmip3_fp)

def test_can_inst_cmip3file_from_dict(cmip3_meta_dict):
    cf = Cmip3File(**cmip3_meta_dict)
