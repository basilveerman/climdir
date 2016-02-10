import os
import pytest

@pytest.fixture(scope='module')
def cmip5_cmor_fp():
    return '/CMIP5/output/CCCMA/CanESM2/rcp85/day/atmos/tasmin/tasmin_day_CanESM2_rcp85_r1i1p1_20060101-21001231.nc'

@pytest.fixture(scope='module')
def cmip5_datanode_fp():
    return '/CMIP5/output1/UKMO/HadCM3/decadal1990/mon/atmos/Amon/r3i2p1/v20100105/tas/tas_Amon_HADCM3_ decadal1990_r3i2p1_199001-199012.nc'

@pytest.fixture(scope='module')
def cmip5_cmor_fname():
    return 'tas_Amon_HADCM3_decadal1990_r3i2p1_199001-199012.nc'
