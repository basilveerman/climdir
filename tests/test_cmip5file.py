import pytest

from climdir import Cmip5File

## Cmip5File instantiation
def test_can_inst_cmip5file_from_cmip5_cmor_fp(cmip5_cmor_fp):
    cf = Cmip5File(cmor_fp = cmip5_cmor_fp)

def test_can_inst_cmip5file_from_cmip5_datanode_fp(cmip5_datanode_fp):
    cf = Cmip5File(datanode_fp = cmip5_datanode_fp)

def test_can_inst_cmip5file_from_cmor_fname(cmip5_cmor_fname):
    cf = Cmip5File(cmor_fname = cmip5_cmor_fname)

def test_can_inst_cmip5file_from_dict(cmip5_meta_dict):
    cf = Cmip5File(**cmip5_meta_dict)

## Generate CMOR file name
def test_cmor_fname_generate(cmip5_cmor_fname):
    cf = Cmip5File(cmor_fname = cmip5_cmor_fname)
    assert cf.cmor_fname == cmip5_cmor_fname

def test_cmor_fname_generate_error(cmip5_cmor_fname):
    cf = Cmip5File(cmor_fname = cmip5_cmor_fname)
    cf.__dict__.pop('model')
    with pytest.raises(AttributeError):
        assert cf.cmor_fname == cmip5_cmor_fname

## Generate CMOR file path
def test_cmor_fp_generate(cmip5_cmor_fp):
    cf = Cmip5File(cmor_fp = cmip5_cmor_fp)
    assert cf.cmor_fp in cmip5_cmor_fp

def test_cmor_fp_generate_error(cmip5_cmor_fp):
    cf = Cmip5File(cmor_fp = cmip5_cmor_fp)
    cf.__dict__.pop('model')
    with pytest.raises(AttributeError):
        assert cf.cmor_fp in cmip5_cmor_fp

## Generate datanode CMOR file path
def test_datanode_fp_generate(cmip5_datanode_fp):
    cf = Cmip5File(datanode_fp = cmip5_datanode_fp)
    assert cf.datanode_fp in cmip5_datanode_fp

def test_datanode_fp_generate_error(cmip5_datanode_fp):
    cf = Cmip5File(datanode_fp = cmip5_datanode_fp)
    cf.__dict__.pop('model')
    with pytest.raises(AttributeError):
        assert cf.datanode_fp in cmip5_datanode_fp

def test_cmip5file_extra_attrs_error(cmip5_cmor_fp):
    with pytest.raises(SyntaxWarning):
        cf = Cmip5File(cmor_fp=cmip5_cmor_fp, bad_arg='whoops')

def test_cmip5file_repr(cmip5_cmor_fp):
    cf = Cmip5File(cmip5_cmor_fp)
    assert eval(repr(cf)) == cf