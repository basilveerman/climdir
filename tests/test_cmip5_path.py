import pytest

from cmme.cmip5file import get_cmor_fp_meta, get_datanode_fp_meta, get_cmor_fname_meta

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