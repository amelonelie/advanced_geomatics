from pyqgis_scripting_ext.core import *


HMap.remove_layers_by_name(["Centroids"])

citiesName = "ne_50m_populated_places"
countriesName = "ne_50m_admin_0_countries"

folder = "/Users/amelonelie/Documents/Master EMMA/semester 2/advanced geomatics+EIA/advanced geomatics/06/natural_earth_vector.gpkg/packages/"
geopackagePath = folder + "natural_earth_vector.gpkg"

countriesLayer = HVectorLayer.open(geopackagePath, countriesName)
countriesFeatures = countriesLayer.features()
nameIndex = countriesLayer.field_index("NAME")


centroids_dict = {
    "name": "String"
}

centroid_layer = HVectorLayer.new("Centroids", "Point", "EPSG:4326", centroids_dict)
for feature in countriesFeatures:
    name = feature.attributes[nameIndex]
    geometry = feature.geometry
    my_centroid = geometry.centroid()
    centroid_layer.add_feature(my_centroid,[name])
    
HMap.add_layer(centroid_layer)    


    
path = folder + "centroids.gpkg"
error = centroid_layer.dump_to_gpkg(path, overwrite=True)
if(error):
    print(error)            