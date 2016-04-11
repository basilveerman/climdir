import pytest

from cfmeta import CmipFile, Cmip5File, Cmip3File

def check_metadata_complete_netcdf(cf):

    assert cf.variable_name == 'var01'
    assert cf.experiment == 'rcp26'
    assert cf.frequency == 'day'
    assert cf.institute == 'UKMO'
    assert cf.model == 'HadCM3'
    assert cf.modeling_realm == 'atmos'
    assert cf.ensemble_member == 'r1i1p1'

## CmipFile instantiation
def test_can_inst_cmipfile_from_netcdf(metadata_complete_netcdf):
    cf = CmipFile(nc = metadata_complete_netcdf)
    check_metadata_complete_netcdf(cf)

def test_can_inst_cmipfile3_from_netcdf(metadata_complete_netcdf):
    cf = Cmip5File(nc = metadata_complete_netcdf)
    check_metadata_complete_netcdf(cf)


def test_can_inst_cmipfile5_from_netcdf(metadata_complete_netcdf):
    cf = Cmip3File(nc = metadata_complete_netcdf)
    check_metadata_complete_netcdf(cf)
