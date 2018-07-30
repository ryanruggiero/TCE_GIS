import urllib
import urllib2
import csv
import zipfile
import arcpy
import datetime
import os


arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True


##desc = arcpy.Describe("S:\\GIS\\one_ft_contour_SHP_files\\Elevation_CN1T2014_EVT1071\\Elevation_CN1T2014_EVT1071.shp")
##SR = desc.spatialReference
##balls = str(SR.Name)
##print balls[0]

    



zip_names = []

with open("Vermont_LiDAR_shape_file_zip_names_update_3.csv", 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        zip_names.append(', '.join(row))

for i in zip_names:
    url = 'http://maps.vcgi.vermont.gov/gisdata/vcgi/packaged_zips/ElevationContours_CN1T/' + i
    urllib.urlretrieve(url, i + ".zip")
    zip_ref = zipfile.ZipFile('S:\\GIS\\one_ft_contour_SHP_files' + '\\' + i + ".zip", 'r')
    zip_ref.extractall('S:\\GIS\\one_ft_contour_SHP_files' + "\\" + i[:-4])
    zip_ref.close()
##    folder_paths = []
##    
##    folder = 'S:\\GIS\\one_ft_contour_SHP_files' + "\\" + i[:-4]
##    for file_ in os.listdir(folder):
##        if file_.lower().endswith(".shp"):
##            shp_path_names = "S:\\GIS\\one_ft_contour_SHP_files" + "\\" + file_[:-4] + "\\" + file_
##          
##            # convert path name, which is a .shp file, to a feature class in my geodatabse
##            arcpy.FeatureClassToGeodatabase_conversion(shp_path_names,'S:\\GIS\\ryan_geodatabase.gdb')
##          
##            # arcpy process from .pyt workflow
##            meter_feature_class = "S:\\GIS\\ryan_geodatabase.gdb" + "\\" + file_[:-4]
##            feet_shape_file = "S:\\GIS\\ryan_geodatabase.gdb\\feet_shape_file"
##            feet_shape_layer = "S:\\GIS\\ryan_geodatabase.gdb\\feet_shape_layer"
##            feet_shape = "S:\\GIS\\ryan_geodatabase.gdb\\feet_shape"
          
            # Process: Project
##            desc = arcpy.Describe("S:\\GIS\\one_ft_contour_SHP_files" + "\\" + file_[:-4] + "\\" + file_)
##            SR = desc.spatialReference
##            projection_name = str(SR.name)
##            if projection_name == 'NAD_1983_StatePlane_Vermont_FIPS_4400':
            # here is hwere code changes from orginal python code, need to replace the projection to one that includes the input having "2011" in its source, stupid shit
##            arcpy.Project_management(meter_feature_class, feet_shape_file, "PROJCS['NAD_1983_StatePlane_Vermont_FIPS_4400_Feet',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',1640416.666666667],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-72.5],PARAMETER['Scale_Factor',0.9999642857142858],PARAMETER['Latitude_Of_Origin',42.5],UNIT['Foot_US',0.3048006096012192]]", "'WGS_1984_(ITRF08)_To_NAD_1983_2011 + WGS_1984_(ITRF00)_To_NAD_1983'", "PROJCS['NAD_1983_2011_StatePlane_Vermont_FIPS_4400',GEOGCS['GCS_NAD_1983_2011',DATUM['D_NAD_1983_2011',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['false_easting',500000.0],PARAMETER['false_northing',0.0],PARAMETER['central_meridian',-72.5],PARAMETER['scale_factor',0.999964285714286],PARAMETER['latitude_of_origin',42.5],UNIT['Meter',1.0]]")          
##            # Process: Add Field
##            arcpy.AddField_management(feet_shape_file, "Layer", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
##            feet_shape = arcpy.mapping.Layer(feet_shape_file)
##            # Process: Select Layer By Attribute
##            arcpy.SelectLayerByAttribute_management(feet_shape, "NEW_SELECTION", "MOD( \"Elevation\",5)=0")
##            # Process: Calculate Field
##            arcpy.CalculateField_management(feet_shape, "Layer", "\"TECON_LIDAR_MAJ\"", "VB", "")
##            # Process: Select Layer By Attribute (2)
##            arcpy.SelectLayerByAttribute_management(feet_shape, "NEW_SELECTION", "MOD( Elevation,5) <> 0")
##            # Process: Calculate Field (2)
##            arcpy.CalculateField_management(feet_shape, "Layer", "\"TECON_LIDAR_MIN\"", "VB", "")
##            feet_shape = "S:\\GIS\\ryan_geodatabase.gdb\\feet_shape"
##            # Process: Export to CAD
##            arcpy.ExportCAD_conversion(feet_shape_file, "DWG_R2010", "S:\\GIS\\one_ft_contour_CAD_files" + "\\" + file_[:-4] + ".dwg", "Ignore_Filenames_in_Tables", "OVERWRITE_EXISTING_FILES", "S:\GIS\seed_file.dwg")
##            # Process: Delete featureclass from Geodatabase
##            arcpy.Delete_management("S:\\GIS\\ryan_geodatabase.gdb" + "\\" + file_[:-4])
##            print "finished conversion of " + shp_path_names + " sucka, at time %s" %datetime.datetime.now()
##            else:
##            # Process: Project
##            arcpy.Project_management(meter_feature_class, feet_shape_file, "PROJCS['NAD_1983_2011_StatePlane_Vermont_FIPS_4400_Ft_US',GEOGCS['GCS_NAD_1983_2011',DATUM['D_NAD_1983_2011',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',1640416.666666667],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-72.5],PARAMETER['Scale_Factor',0.9999642857142858],PARAMETER['Latitude_Of_Origin',42.5],UNIT['Foot_US',0.3048006096012192]]", "'WGS_1984_(ITRF00)_To_NAD_1983 + WGS_1984_(ITRF08)_To_NAD_1983_2011'", "PROJCS['NAD_1983_StatePlane_Vermont_FIPS_4400',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-72.5],PARAMETER['Scale_Factor',0.9999642857142858],PARAMETER['Latitude_Of_Origin',42.5],UNIT['Meter',1.0]],VERTCS['NAVD_1988',VDATUM['North_American_Vertical_Datum_1988'],PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['Meter',1.0]]")
##            # Process: Add Field
##            arcpy.AddField_management(feet_shape_file, "Layer", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
##            feet_shape = arcpy.mapping.Layer(feet_shape_file)
##            # Process: Select Layer By Attribute
##            arcpy.SelectLayerByAttribute_management(feet_shape, "NEW_SELECTION", "MOD( \"Elevation\",5)=0")
##            # Process: Calculate Field
##            arcpy.CalculateField_management(feet_shape, "Layer", "\"TECON_LIDAR_MAJ\"", "VB", "")
##            # Process: Select Layer By Attribute (2)
##            arcpy.SelectLayerByAttribute_management(feet_shape, "NEW_SELECTION", "MOD( Elevation,5) <> 0")
##            # Process: Calculate Field (2)
##            arcpy.CalculateField_management(feet_shape, "Layer", "\"TECON_LIDAR_MIN\"", "VB", "")
##            feet_shape = "S:\\GIS\\ryan_geodatabase.gdb\\feet_shape"
##            # Process: Export to CAD
##            arcpy.ExportCAD_conversion(feet_shape_file, "DWG_R2010", "S:\\GIS\\one_ft_contour_CAD_files" + "\\" + file_[:-4] + ".dwg", "Ignore_Filenames_in_Tables", "OVERWRITE_EXISTING_FILES", "S:\GIS\seed_file.dwg")
##            # Process: Delete featureclass from Geodatabase
##            arcpy.Delete_management("S:\\GIS\\ryan_geodatabase.gdb" + "\\" + file_[:-4])
##            print "finished conversion of " + shp_path_names + " sucka, at time %s" %datetime.datetime.now()






##            




##
##### code from original tool
##
##import arcpy
##import datetime
##import os 
##arcpy.CheckOutExtension("Spatial")
##arcpy.env.overwriteOutput = True
##
##
##folder_paths = []
##
##
### root folder
##for root, dirs, files in os.walk("."):
##   for name in dirs:
##      folder_paths.append("S:\\GIS\\one_ft_contour_SHP_files" + "\\" + name)
##
##      
### extract .shp file from folders and source code loop
##for folder in folder_paths:
##   for file_ in os.listdir(folder):
##      if file_.lower().endswith(".shp"):
##          shp_path_names = "S:\\GIS\\one_ft_contour_SHP_files" + "\\" + file_[:-4] + "\\" + file_
##          
##          # convert path name, which is a .shp file, to a feature class in my geodatabse
##          arcpy.FeatureClassToGeodatabase_conversion(shp_path_names,'S:\\GIS\\ryan_geodatabase.gdb')
##          
##          # arcpy process from .pyt workflow
##          meter_feature_class = "S:\\GIS\\ryan_geodatabase.gdb" + "\\" + file_[:-4]
##          feet_shape_file = "S:\\GIS\\ryan_geodatabase.gdb\\feet_shape_file"
##          feet_shape_layer = "S:\\GIS\\ryan_geodatabase.gdb\\feet_shape_layer"
##          feet_shape = "S:\\GIS\\ryan_geodatabase.gdb\\feet_shape"
##          
##          # Process: Project
##          
##          # here is hwere code changes from orginal python code, need to replace the projection to one that includes the input having "2011" in its source, stupid shit
##          arcpy.Project_management(meter_feature_class, feet_shape_file, "PROJCS['NAD_1983_StatePlane_Vermont_FIPS_4400_Feet',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',1640416.666666667],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-72.5],PARAMETER['Scale_Factor',0.9999642857142858],PARAMETER['Latitude_Of_Origin',42.5],UNIT['Foot_US',0.3048006096012192]]", "'WGS_1984_(ITRF08)_To_NAD_1983_2011 + WGS_1984_(ITRF00)_To_NAD_1983'", "PROJCS['NAD_1983_2011_StatePlane_Vermont_FIPS_4400',GEOGCS['GCS_NAD_1983_2011',DATUM['D_NAD_1983_2011',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['false_easting',500000.0],PARAMETER['false_northing',0.0],PARAMETER['central_meridian',-72.5],PARAMETER['scale_factor',0.999964285714286],PARAMETER['latitude_of_origin',42.5],UNIT['Meter',1.0]]")          
##          # Process: Add Field
##          arcpy.AddField_management(feet_shape_file, "Layer", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
##          feet_shape = arcpy.mapping.Layer(feet_shape_file)
##          # Process: Select Layer By Attribute
##          arcpy.SelectLayerByAttribute_management(feet_shape, "NEW_SELECTION", "MOD( \"Elevation\",5)=0")
##          # Process: Calculate Field
##          arcpy.CalculateField_management(feet_shape, "Layer", "\"TECON_LIDAR_MAJ\"", "VB", "")
##          # Process: Select Layer By Attribute (2)
##          arcpy.SelectLayerByAttribute_management(feet_shape, "NEW_SELECTION", "MOD( Elevation,5) <> 0")
##          # Process: Calculate Field (2)
##          arcpy.CalculateField_management(feet_shape, "Layer", "\"TECON_LIDAR_MIN\"", "VB", "")
##          feet_shape = "S:\\GIS\\ryan_geodatabase.gdb\\feet_shape"
##          # Process: Export to CAD
##          arcpy.ExportCAD_conversion(feet_shape_file, "DWG_R2010", "S:\\GIS\\one_ft_contour_CAD_files" + "\\" + file_[:-4] + ".dwg", "Ignore_Filenames_in_Tables", "OVERWRITE_EXISTING_FILES", "S:\GIS\seed_file.dwg")
##          print "finished conversion of " + shp_path_names + " sucka, at time %s" %datetime.datetime.now()

