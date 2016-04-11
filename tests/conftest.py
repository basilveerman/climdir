import os
import pytest

from netCDF4 import Dataset

from util import get_base_netcdf, nc_add_variable

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
def cmip5_cmor_fname_temporal_suffix():
    return 'tas_Amon_HADCM3_decadal1990_r3i2p1_19710201-19710214-avg.nc.nc'

@pytest.fixture(scope='module')
def cmip5_cmor_fname_geographical_info():
    return 'tas_Amon_HADCM3_decadal1990_r3i2p1_g-lat20S20Nlon170W130W.nc'

@pytest.fixture(scope='module')
def cmip5_cmor_fname_temporal_geographical_suffix():
    return 'tas_Amon_HADCM3_decadal1990_r3i2p1_199001-199012-clim_g-global-ocn-areaavg.nc'

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

@pytest.fixture(scope='module')
def cmip3_fp():
    return '/data/sresa2/pr/csiro_mk3_0/run1/csiro_mk3_0-sresa2-pr-run1.nc'

@pytest.fixture(scope='module')
def cmip3_meta_dict():
    return {
        'model': 'csiro_mk3_0',
        'experiment': 'sresa2',
        'ensemble_member': 'run1',
        'variable_name': 'pr',
    }

@pytest.fixture(scope="session")
def metadata_complete_netcdf(request):
    shape = {'time': 4, 'lon': 4, 'lat': 4}
    nc = get_base_netcdf(shape)
    nc_add_variable(nc, 'var01', shape)
    nc.experiment_id = 'rcp26'
    nc.frequency = 'day'
    nc.institute_id = 'UKMO'
    nc.model_id = 'HadCM3'
    nc.modeling_realm = 'atmos'
    nc.realization = 1
    nc.initialization_method = 1
    nc.physics_version = 1

    def teardown():
        nc.close()
    request.addfinalizer(teardown)

    return nc