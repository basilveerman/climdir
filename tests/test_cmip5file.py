from climdir import Cmip5File, get_cmor_fp_meta, get_datanode_fp_meta, get_cmor_fname_meta

# def test_cmip5file_from_cmor_fp(cmip5_cmor_fp):
#     cf = Cmip5File(cmor_fp = cmip5_cmor_fp)
#     assert eval(repr(cf)) == cf

# def test_cmip5file_from_datanode_fp(cmip5_datanode_fp):
#     cf = Cmip5File(datanode_fp = cmip5_datanode_fp)

def test_get_cmor_fp_meta(cmip5_cmor_fp):
    '/CMIP5/output/MOHC/HadCM3/decadal1990/day/atmos/tas/r3i2p1/file.nc'
    meta = get_cmor_fp_meta(cmip5_cmor_fp)
    r = {
        'activity': 'CMIP5',
        'product': 'output',
        'institute': 'MOHC',
        'model': 'HadCM3',
        'experiment': 'decadal1990',
        'frequency': 'day',
        'modeling_realm': 'atmos',
        'variable_name': 'tas',
        'ensemble_member': 'r3i2p1',
    }
    for att, val in r.items():
        assert meta[att] == r[att]

def test_get_datanode_fp_meta(cmip5_datanode_fp):
    meta = get_datanode_fp_meta(cmip5_datanode_fp)
    r = {
        'activity': 'CMIP5',
        'product': 'output1',
        'institute': 'UKMO',
        'model': 'HadCM3',
        'experiment': 'decadal1990',
        'frequency': 'mon',
        'modeling_realm': 'atmos',
        'mip_table': 'Amon',
        'ensemble_member': 'r3i2p1',
        'version_number': 'v20100105',
        'variable_name': 'tas',
    }
    for att, val in r.items():
        assert meta[att] == r[att]

def test_get_cmor_fname_meta(cmip5_cmor_fname):
    meta = get_cmor_fname_meta(cmip5_cmor_fname)
    r = {
        'variable_name': 'tas',
        'mip_table': 'Amon',
        'model': 'HADCM3',
        'experiment': 'decadal1990',
        'ensemble_member': 'r3i2p1',
        'temporal_subset': '199001-199012'
    }
    for att, val in r.items():
        assert meta[att] == r[att]