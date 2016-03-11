.. climdir documentation master file, created by
   sphinx-quickstart on Tue Feb  9 18:51:01 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

cfmeta - Climate and Forecase Metadata Processor
================================================

.. automodule:: cfmeta

Basic Usage::

    from cfmeta import Cmip5File
    cf5 = Cmip5File(cmor_fname = 'tas_Amon_HADCM3_decadal1990_r3i2p1.nc')
    cf5
    # Cmip5File(ensemble_member = 'r3i2p1', model = 'HADCM3', experiment = 'decadal1990', mip_table = 'Amon', variable_name = 'tas')

    cf5.update(variable_name = 'pr')

    cf5.cmor_fname
    # 'pr_Amon_HADCM3_decadal1990_r3i2p1.nc'

Convert to Cmip3 spec::

    from cfmeta import Cmip3File

    cf3 = Cmip3File(**cf5.atts)
    cf3.fname
    # 'HADCM3-decadal1990-pr-r3i2p1.nc'

.. Contents:

.. .. toctree::
..    :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

