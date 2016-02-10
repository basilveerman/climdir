from climdir import Cmip5File

def test_cmip5file_from_cmor_fp(cmip5_cmor_fp):
    cf = Cmip5File(cmor_fp = cmip5_cmor_fp)
    assert eval(repr(cf)) == cf

def test_cmip5file_from_datanode_fp(cmip5_datanode_fp):
    cf = Cmip5File(datanode_fp = f)
