import os
import pytest

@pytest.fixture(scope='module')
def cmip5_cmor_fp():
    return '/CMIP5/output/MOHC/HadCM3/decadal1990/day/atmos/tas/r3i2p1/tas_day_HadCM3_decadal1990_r3i2p1_199001-199012.nc'

@pytest.fixture(scope='module')
def cmip5_datanode_fp():
    return '/CMIP5/output1/UKMO/HadCM3/decadal1990/mon/atmos/Amon/r3i2p1/v20100105/tas/tas_Amon_HadCM3_decadal1990_r3i2p1_199001-199012.nc'

@pytest.fixture(scope='module')
def cmip5_cmor_fname():
    return 'tas_Amon_HADCM3_decadal1990_r3i2p1.nc'

@pytest.fixture(scope='module')
def cmip5_meta_dict():
    return {
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