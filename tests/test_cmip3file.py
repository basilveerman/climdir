import pytest

from cmme import Cmip3File
from cmme.exceptions import PathError

## Cmip3File instantiation
def test_can_inst_cmip3file_from_fp(cmip3_fp):
    cf = Cmip3File(fp = cmip3_fp)

def test_can_inst_cmip3file_from_dict(cmip3_meta_dict):
    cf = Cmip3File(**cmip3_meta_dict)

def test_can_generate_cmip3_dirname(cmip3_fp):
    cf = Cmip3File(fp = cmip3_fp)
    assert cf.dirname == 'sresa2/pr/csiro_mk3_0/run1'

def test_can_generate_cmip3_fname(cmip3_fp):
    cf = Cmip3File(fp = cmip3_fp)
    assert cf.fname == 'csiro_mk3_0-sresa2-pr-run1.nc'

def test_can_generate_cmip3_fp(cmip3_fp):
    cf = Cmip3File(fp = cmip3_fp)
    assert cf.fp == 'sresa2/pr/csiro_mk3_0/run1/csiro_mk3_0-sresa2-pr-run1.nc'