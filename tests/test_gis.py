# -*- coding: utf-8 -*-
##
##  test_gis.py
##  RAPIDpy
##
##  Created by Alan D. Snow.
##  Copyright © 2016 Alan D Snow. All rights reserved.
##

from glob import glob
from nose.tools import ok_
import os
from osgeo import ogr

#local import
from RAPIDpy.gis.weight import CreateWeightTableECMWF, CreateWeightTableLDAS
from RAPIDpy.gis.workflow import CreateAllStaticECMWFRAPIDFiles
from RAPIDpy.gis.network import CreateNetworkConnectivityNHDPlus
from RAPIDpy.gis.taudem import TauDEM
from RAPIDpy.helper_functions import (compare_csv_decimal_files,
                                      remove_files)
#GLOBAL VARIABLES
MAIN_TESTS_FOLDER = os.path.dirname(os.path.abspath(__file__))
COMPARE_DATA_PATH = os.path.join(MAIN_TESTS_FOLDER, 'compare', 'gis')
GIS_INPUT_DATA_PATH = os.path.join(MAIN_TESTS_FOLDER, 'data', 'gis')
RAPID_INPUT_DATA_PATH = os.path.join(MAIN_TESTS_FOLDER, 'input')
OUTPUT_DATA_PATH = os.path.join(MAIN_TESTS_FOLDER, 'output')
LSM_INPUT_DATA_PATH = os.path.join(MAIN_TESTS_FOLDER, 'data','lsm_grids')

#------------------------------------------------------------------------------
# MAIN TEST SCRIPTS
#------------------------------------------------------------------------------
def test_gen_static_rapid_input():
    """
    Checks generating static RAPID input
    """
    print("TEST 1: TEST GENERATE STATIC RAPID INPUT DATA")
    CreateAllStaticECMWFRAPIDFiles(in_drainage_line=os.path.join(GIS_INPUT_DATA_PATH, 'flowline.shp'),
                                   river_id="COMID",
                                   length_id="LENGTHKM",
                                   slope_id="Slope",
                                   next_down_id="NextDownID",
                                   in_catchment=os.path.join(GIS_INPUT_DATA_PATH, 'catchment.shp'),
                                   catchment_river_id="FEATUREID",
                                   rapid_output_folder=OUTPUT_DATA_PATH,
                                   kfac_length_units="km",
                                   )
    
    #CHECK OUTPUT   
    #comid_lat_lon_z
    generated_comid_lat_lon_z_file = os.path.join(OUTPUT_DATA_PATH, 
                                                  "comid_lat_lon_z.csv")
    generated_comid_lat_lon_z_file_solution = os.path.join(COMPARE_DATA_PATH, "x-x",
                                                           "comid_lat_lon_z.csv")
    ok_(compare_csv_decimal_files(generated_comid_lat_lon_z_file, 
                                  generated_comid_lat_lon_z_file_solution))

    #rapid_connect
    generated_rapid_connect_file = os.path.join(OUTPUT_DATA_PATH, 
                                                "rapid_connect.csv")
    generated_rapid_connect_file_solution = os.path.join(COMPARE_DATA_PATH, "x-x",
                                                         "rapid_connect.csv")
    ok_(compare_csv_decimal_files(generated_rapid_connect_file, 
                                  generated_rapid_connect_file_solution))

    #riv_bas_id
    generated_riv_bas_id_file = os.path.join(OUTPUT_DATA_PATH, 
                                             "riv_bas_id.csv")
    generated_riv_bas_id_file_solution = os.path.join(COMPARE_DATA_PATH, "x-x",
                                                      "riv_bas_id.csv")
    ok_(compare_csv_decimal_files(generated_riv_bas_id_file, 
                                  generated_riv_bas_id_file_solution))

    #kfac
    generated_kfac_file = os.path.join(OUTPUT_DATA_PATH, 
                                       "kfac.csv")
    generated_kfac_file_solution = os.path.join(COMPARE_DATA_PATH, "x-x",
                                                "kfac.csv")
    ok_(compare_csv_decimal_files(generated_kfac_file, 
                                  generated_kfac_file_solution))
    
    #k
    generated_k_file = os.path.join(OUTPUT_DATA_PATH, 
                                    "k.csv")
    generated_k_file_solution = os.path.join(COMPARE_DATA_PATH, "x-x",
                                             "k.csv")
    ok_(compare_csv_decimal_files(generated_k_file, 
                                  generated_k_file_solution))

    #x
    generated_x_file = os.path.join(OUTPUT_DATA_PATH, 
                                    "x.csv")
    generated_x_file_solution = os.path.join(COMPARE_DATA_PATH, "x-x",
                                             "x.csv")
    ok_(compare_csv_decimal_files(generated_x_file, 
                                  generated_x_file_solution))

    #weight_ecmwf_t1279
    generated_weight_ecmwf_t1279_file = os.path.join(OUTPUT_DATA_PATH, 
                                                     "weight_ecmwf_t1279.csv")
    generated_weight_ecmwf_t1279_file_solution = os.path.join(COMPARE_DATA_PATH, "x-x",
                                                              "weight_ecmwf_t1279.csv")
    ok_(compare_csv_decimal_files(generated_weight_ecmwf_t1279_file, 
                                  generated_weight_ecmwf_t1279_file_solution))

    #weight_ecmwf_tco369
    generated_weight_ecmwf_tco639_file = os.path.join(OUTPUT_DATA_PATH, 
                                                      "weight_ecmwf_tco639.csv")
    generated_weight_ecmwf_tco639_file_solution = os.path.join(COMPARE_DATA_PATH, "x-x",
                                                               "weight_ecmwf_tco639.csv")
    ok_(compare_csv_decimal_files(generated_weight_ecmwf_tco639_file, 
                                  generated_weight_ecmwf_tco639_file_solution))

    #weight_era_t511
    generated_weight_era_t511_file = os.path.join(OUTPUT_DATA_PATH, 
                                                  "weight_era_t511.csv")
    generated_weight_era_t511_file_solution = os.path.join(COMPARE_DATA_PATH, "x-x",
                                                           "weight_era_t511.csv")
    ok_(compare_csv_decimal_files(generated_weight_era_t511_file, 
                                  generated_weight_era_t511_file_solution))

    remove_files(generated_comid_lat_lon_z_file,
                 generated_rapid_connect_file,
                 generated_riv_bas_id_file,
                 generated_kfac_file,
                 generated_k_file,
                 generated_x_file,
                 generated_weight_ecmwf_t1279_file,
                 generated_weight_ecmwf_tco639_file,
                 generated_weight_era_t511_file)

def test_gen_static_nhd_connect_rapid_input():
    """
    Checks generating static NHDPlus connect RAPID input
    """
    print("TEST 2: TEST GENERATE STATIC NHDPlus CONNECT RAPID INPUT DATA")
    generated_rapid_connect_file = os.path.join(OUTPUT_DATA_PATH, 
                                                "rapid_connect_nhd.csv")
    CreateNetworkConnectivityNHDPlus(in_drainage_line=os.path.join(GIS_INPUT_DATA_PATH, 'flowline.shp'),
                                     out_connectivity_file=generated_rapid_connect_file)
    #rapid_connect
    generated_rapid_connect_file_solution = os.path.join(COMPARE_DATA_PATH, "x-x",
                                                         "rapid_connect.csv")
                                                         
    ok_(compare_csv_decimal_files(generated_rapid_connect_file, 
                                  generated_rapid_connect_file_solution))

    remove_files(generated_rapid_connect_file)

def test_gen_weight_table_era20cm():
    """
    Checks generating weight table for ERA 20CM grid
    """
    print("TEST 3: TEST GENERATE WEIGTH TABLE FOR ERA 20CM GRIDS")
    generated_weight_table_file = os.path.join(OUTPUT_DATA_PATH, 
                                               "weight_era_t159.csv")
    #rapid_connect
    rapid_connect_file = os.path.join(COMPARE_DATA_PATH, "x-x",
                                      "rapid_connect.csv")

    lsm_grid = os.path.join(LSM_INPUT_DATA_PATH, "era20cm", "era_20cm_runoff_20000129_0.nc")
    CreateWeightTableECMWF(in_ecmwf_nc=lsm_grid, 
                           in_catchment_shapefile=os.path.join(GIS_INPUT_DATA_PATH, 'catchment.shp'), 
                           river_id="FEATUREID", 
                           in_connectivity_file=rapid_connect_file, 
                           out_weight_table=generated_weight_table_file)
                                                         
    generated_weight_table_file_solution = os.path.join(COMPARE_DATA_PATH, "x-x",
                                                        "weight_era_t159.csv")
    ok_(compare_csv_decimal_files(generated_weight_table_file, 
                                  generated_weight_table_file_solution))

    remove_files(generated_weight_table_file)

def test_gen_weight_table_era_t255():
    """
    Checks generating weight table for ERA T255 grid
    """
    print("TEST 4: TEST GENERATE WEIGTH TABLE FOR ERA T255 GRIDS")
    generated_weight_table_file = os.path.join(OUTPUT_DATA_PATH, 
                                               "weight_era_t255.csv")
    #rapid_connect
    rapid_connect_file = os.path.join(COMPARE_DATA_PATH, "x-x",
                                      "rapid_connect.csv")

    lsm_grid = os.path.join(LSM_INPUT_DATA_PATH, "erai3t255", "era_interim_runoff_20140820.nc")
    CreateWeightTableECMWF(in_ecmwf_nc=lsm_grid, 
                           in_catchment_shapefile=os.path.join(GIS_INPUT_DATA_PATH, 'catchment.shp'), 
                           river_id="FEATUREID", 
                           in_connectivity_file=rapid_connect_file, 
                           out_weight_table=generated_weight_table_file)
                                                         
    generated_weight_table_file_solution = os.path.join(COMPARE_DATA_PATH, "x-x",
                                                        "weight_era_t255.csv")
    ok_(compare_csv_decimal_files(generated_weight_table_file, 
                                  generated_weight_table_file_solution))

    remove_files(generated_weight_table_file)

def test_gen_weight_table_era_t511_24hr():
    """
    Checks generating weight table for ERA T511 24hr grid
    """
    print("TEST 5: TEST GENERATE WEIGTH TABLE FOR ERA T511 24hr GRIDS")
    generated_weight_table_file = os.path.join(OUTPUT_DATA_PATH, 
                                               "weight_era_t511.csv")
    #rapid_connect
    rapid_connect_file = os.path.join(COMPARE_DATA_PATH,"x-x",
                                      "rapid_connect.csv")

    lsm_grid = os.path.join(LSM_INPUT_DATA_PATH, "erai24", "19990109_erai_runoff.grib.nc")
    CreateWeightTableECMWF(in_ecmwf_nc=lsm_grid, 
                           in_catchment_shapefile=os.path.join(GIS_INPUT_DATA_PATH, 'catchment.shp'), 
                           river_id="FEATUREID", 
                           in_connectivity_file=rapid_connect_file, 
                           out_weight_table=generated_weight_table_file)
                                                         
    generated_weight_table_file_solution = os.path.join(COMPARE_DATA_PATH, "x-x",
                                                        "weight_era_t511.csv")
    ok_(compare_csv_decimal_files(generated_weight_table_file, 
                                  generated_weight_table_file_solution))

    remove_files(generated_weight_table_file)

def test_gen_weight_table_gldas2():
    """
    Checks generating weight table for GLDAS V2 grid
    """
    print("TEST 6: TEST GENERATE WEIGTH TABLE FOR GLDAS V2 GRIDS")
    generated_weight_table_file = os.path.join(OUTPUT_DATA_PATH, 
                                               "weight_gldas2.csv")
    #rapid_connect
    rapid_connect_file = os.path.join(COMPARE_DATA_PATH, "x-x",
                                      "rapid_connect.csv")

    lsm_grid = os.path.join(LSM_INPUT_DATA_PATH, "gldas2", "GLDAS_NOAH025_3H.A20101231.0000.020.nc4")
    CreateWeightTableLDAS(in_ldas_nc=lsm_grid,
                          in_nc_lon_var="lon",
                          in_nc_lat_var="lat", 
                          in_catchment_shapefile=os.path.join(GIS_INPUT_DATA_PATH, 'catchment.shp'), 
                          river_id="FEATUREID", 
                          in_connectivity_file=rapid_connect_file, 
                          out_weight_table=generated_weight_table_file)
                                                         
    generated_weight_table_file_solution = os.path.join(COMPARE_DATA_PATH, "x-x",
                                                        "weight_gldas2.csv")
    ok_(compare_csv_decimal_files(generated_weight_table_file, 
                                  generated_weight_table_file_solution))

    remove_files(generated_weight_table_file)

def test_gen_weight_table_lis():
    """
    Checks generating weight table for LIS grid
    """
    print("TEST 7: TEST GENERATE WEIGTH TABLE FOR LIS GRIDS")
    generated_weight_table_file = os.path.join(OUTPUT_DATA_PATH, 
                                               "weight_lis.csv")
    #rapid_connect
    rapid_connect_file = os.path.join(COMPARE_DATA_PATH, "u-k",
                                      "rapid_connect.csv")

    lsm_grid = os.path.join(LSM_INPUT_DATA_PATH, "lis", "LIS_HIST_201101210000.d01.nc")
    CreateWeightTableLDAS(in_ldas_nc=lsm_grid,
                          in_nc_lon_var="lon",
                          in_nc_lat_var="lat", 
                          in_catchment_shapefile=os.path.join(GIS_INPUT_DATA_PATH, 'u-k', 'CatchmentSubset.shp'), 
                          river_id="DrainLnID", 
                          in_connectivity_file=rapid_connect_file, 
                          out_weight_table=generated_weight_table_file)
                                                         
    generated_weight_table_file_solution = os.path.join(COMPARE_DATA_PATH, "u-k",
                                                        "weight_lis.csv")
    ok_(compare_csv_decimal_files(generated_weight_table_file, 
                                  generated_weight_table_file_solution))

    remove_files(generated_weight_table_file)

def test_gen_weight_table_joules():
    """
    Checks generating weight table for Joules grid
    """
    print("TEST 8: TEST GENERATE WEIGTH TABLE FOR Joules GRIDS")
    generated_weight_table_file = os.path.join(OUTPUT_DATA_PATH, 
                                               "weight_joules.csv")
    #rapid_connect
    rapid_connect_file = os.path.join(COMPARE_DATA_PATH, "u-k",
                                      "rapid_connect.csv")

    lsm_grid = os.path.join(LSM_INPUT_DATA_PATH, "joules", "ukv_test.runoff.20080803_00.nc")
    CreateWeightTableLDAS(in_ldas_nc=lsm_grid,
                          in_nc_lon_var="east_west",
                          in_nc_lat_var="north_south", 
                          in_catchment_shapefile=os.path.join(GIS_INPUT_DATA_PATH, 'u-k', 'CatchmentSubset.shp'), 
                          river_id="DrainLnID", 
                          in_connectivity_file=rapid_connect_file, 
                          out_weight_table=generated_weight_table_file)
                                                         
    generated_weight_table_file_solution = os.path.join(COMPARE_DATA_PATH, "u-k",
                                                        "weight_joules.csv")
    ok_(compare_csv_decimal_files(generated_weight_table_file, 
                                  generated_weight_table_file_solution))

    remove_files(generated_weight_table_file)

def test_extract_sub_network_taudem():
    """
    Checks extracting sub network from larger network
    """
    print("TEST 9: TEST EXTRACTING SUB NETWORK FROM LARGER NETWORK")
    td = TauDEM()
    
    subset_network_file = os.path.join(OUTPUT_DATA_PATH, "DrainageLineSubset2.shp")
    #to extract a specific network
    td.extractSubNetwork(network_file=os.path.join(GIS_INPUT_DATA_PATH, 'u-k', "DrainageLineSubset.shp"),
                         out_subset_network_file=subset_network_file,
                         outlet_ids=[42911], #list of outlet ids
                         river_id_field="HydroID",
                         next_down_id_field="NextDownID",
                         river_magnitude_field="HydroID",
                         safe_mode=False,
                         )
    
    #to extract the subset watersheds using subset river network
    subset_watershed_file = os.path.join(OUTPUT_DATA_PATH,"CatchmentSubset2.shp")
    td.extractSubsetFromWatershed(subset_network_file=subset_network_file,
                                  subset_network_river_id_field="HydroID",
                                  watershed_file=os.path.join(GIS_INPUT_DATA_PATH, 'u-k', 'CatchmentSubset.shp'),
                                  watershed_network_river_id_field="DrainLnID",
                                  out_watershed_subset_file=subset_watershed_file)
                                                         
    #Test results
    subset_network_shapefile = ogr.Open(subset_network_file)
    subset_network_layer = subset_network_shapefile.GetLayer()

    ogr_watershed_shapefile = ogr.Open(subset_watershed_file)
    ogr_watershed_shapefile_lyr = ogr_watershed_shapefile.GetLayer()

    number_of_network_features = subset_network_layer.GetFeatureCount()
    number_of_watershed_features = ogr_watershed_shapefile_lyr.GetFeatureCount()
    
    #count number of features
    ok_(number_of_network_features==7)
    ok_(number_of_watershed_features==7)
    
    #make sure IDs correct
    network_id_list = [42911,42891,42747,42748,42892,42841,42846]    
    for feature_idx, network_feature in enumerate(subset_network_layer):
        ok_(network_feature.GetField("HydroID") in network_id_list)
    for feature_idx, watershed_feature in enumerate(ogr_watershed_shapefile_lyr):
        ok_(watershed_feature.GetField("DrainLnID") in network_id_list)
     
    #make sure all fields are there
     
     #TEST WATERSHED
    subset_watershed_layer_defn = ogr_watershed_shapefile_lyr.GetLayerDefn()
    num_watershed_fields = subset_watershed_layer_defn.GetFieldCount()

    watershed_field_names = ['Shape_Leng','Shape_Area','HydroID','GridID','DrainLnID']
    ok_(num_watershed_fields==len(watershed_field_names))    
    for i in range(num_watershed_fields):
        ok_(subset_watershed_layer_defn.GetFieldDefn(i).GetNameRef() in watershed_field_names)
          
    #TEST NETWORK                                         
    subset_network_layer_defn = subset_network_layer.GetLayerDefn()
    num_network_fields = subset_network_layer_defn.GetFieldCount()

    network_field_names = ['arcid','from_node','to_node','HydroID','GridID','NextDownID',
                           'SLength','Avg_Slope','LENGTHKM','Shape_Leng','Musk_x','watershed','subbasin']
    ok_(num_network_fields==len(network_field_names))    
    for i in range(num_network_fields):
        ok_(subset_network_layer_defn.GetFieldDefn(i).GetNameRef() in network_field_names)
    
    #cleanup
    remove_files(*glob(os.path.join(OUTPUT_DATA_PATH,"DrainageLineSubset2.*")))
    remove_files(*glob(os.path.join(OUTPUT_DATA_PATH,"CatchmentSubset2.*")))

if __name__ == '__main__':
    #import nose
    #nose.main()
    test_extract_sub_network_taudem()