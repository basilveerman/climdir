import pytest

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

def test_get_cmor_fname_meta_basic(cmip5_cmor_fname):
    meta = get_cmor_fname_meta(cmip5_cmor_fname)
    r = {
        'variable_name': 'tas',
        'mip_table': 'Amon',
        'model': 'HADCM3',
        'experiment': 'decadal1990',
        'ensemble_member': 'r3i2p1',
    }
    for att, val in r.items():
        assert meta[att] == r[att]

@pytest.mark.parametrize(('fname', 'expected'), [
    (
        "tas_Amon_HADCM3_decadal1990_r3i2p1_19710201-19710214-avg.nc",
        {'temporal_subset': '19710201-19710214-avg'}
    ), (
        "tas_Amon_HADCM3_decadal1990_r3i2p1_196001-198912-clim.nc",
        {'temporal_subset': '196001-198912-clim'}
    ), (
        "tas_Amon_HADCM3_decadal1990_r3i2p1_g-lat20S20Nlon170W130W.nc",
        {'geographical_info': 'g-lat20S20Nlon170W130W'}
    ), (
        "tas_Amon_HADCM3_decadal1990_r3i2p1_g-lat20S20N-lnd-zonalavg.nc",
        {'geographical_info': 'g-lat20S20N-lnd-zonalavg'}
    ), (
        "tas_Amon_HADCM3_decadal1990_r3i2p1_199001-199012-clim_g-global-ocn-areaavg.nc",
        {
            'temporal_subset': '199001-199012-clim',
            'geographical_info': 'g-global-ocn-areaavg'
        }
    )
])
def test_get_cmor_fname_meta_extended(fname, expected):
    meta = get_cmor_fname_meta(fname)

    for att, val in expected.items():
        assert meta[att] == val

def test_can_inst_cmip5file_from_cmip5_cmor_fp(cmip5_cmor_fp):
    cf = Cmip5File(cmor_fp = cmip5_cmor_fp)

def test_can_inst_cmip5file_from_cmip5_datanode_fp(cmip5_datanode_fp):
    cf = Cmip5File(datanode_fp = cmip5_datanode_fp)

def test_can_inst_cmip5file_from_cmor_fname(cmip5_cmor_fname):
    cf = Cmip5File(cmor_fname = cmip5_cmor_fname)

def test_can_inst_cmip5file_from_dict(cmip5_meta_dict):
    cf = Cmip5File(**cmip5_meta_dict)

def test_cmor_fname_generate(cmip5_cmor_fname):
    cf = Cmip5File(cmor_fname = cmip5_cmor_fname)
    assert cf.cmor_fname == cmip5_cmor_fname

def test_cmor_fname_generate_error(cmip5_cmor_fname):
    cf = Cmip5File(cmor_fname = cmip5_cmor_fname)
    cf.__dict__.pop('model')
    with pytest.raises(AttributeError):
        assert cf.cmor_fname == cmip5_cmor_fname

def test_cmip5file_extra_attrs_error(cmip5_cmor_fp):
    with pytest.raises(SyntaxWarning):
        cf = Cmip5File(cmor_fp=cmip5_cmor_fp, bad_arg='whoops')

def test_cmip5file_repr(cmip5_cmor_fp):
    cf = Cmip5File(cmip5_cmor_fp)
    assert eval(repr(cf)) == cf