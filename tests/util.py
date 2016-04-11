from tempfile import NamedTemporaryFile

import netCDF4
import numpy as np

def get_base_netcdf(dims, calendar='standard', start_time = 0):
    f = NamedTemporaryFile(suffix='.nc')
    nc = netCDF4.Dataset(f.name, 'w')

    lat = nc.createDimension('lat', dims['lat'])
    var_lat = nc.createVariable('lat', 'f4', 'lat')
    var_lat[:] = range(dims['lat'])

    var_lat.axis = 'Y'
    var_lat.units = 'degrees_north'
    var_lat.long_name = 'latitude'

    lon = nc.createDimension('lon', dims['lon'])
    var_lon = nc.createVariable('lon', 'f4', 'lon')
    var_lon[:] = range(dims['lon'])

    var_lon.axis = 'X'
    var_lon.units = 'degrees_east'
    var_lon.long_name = 'longitude'

    time = nc.createDimension('time', dims['time'])
    var_time = nc.createVariable('time', 'i4', 'time')
    var_time[:] = range(start_time, start_time + dims['time'])

    var_time.axis = 'T'
    var_time.units = 'days since 2000-01-01'
    var_time.calendar = calendar
    var_time.long_name = 'time'

    return nc

def nc_add_variable(nc, variable_name, shape, fill_value = 1e20, fill_func = np.random.randn):
    var = nc.createVariable(variable_name, 'f4', ('time', 'lat', 'lon'), fill_value=fill_value)
    var.standard_name = variable_name + '_standard_name'
    var.long_name = variable_name + '_long_name'
    var.units = variable_name + '_units'
    var.missing_value = fill_value
    for t in range(shape['time']):
        var[t,:,:] = fill_func(shape['lat'], shape['lon'])

def get_bare_netcdf():
    f = NamedTemporaryFile()
    dims = {'time': 32, 'lon': 128, 'lat': 64}
    nc = netCDF4.Dataset(f.name, 'w')
    lat = nc.createDimension('lat', dims['lat'])
    lon = nc.createDimension('lon', dims['lon'])
    time = nc.createDimension('time', dims['time'])

    return nc