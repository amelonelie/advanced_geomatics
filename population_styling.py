from pyqgis_scripting_ext.core import *

folder = "/Users/amelonelie/Documents/Programme/GitHub/advanced_geomatics/data/"
output_folder = "/Users/amelonelie/Documents/Programme/GitHub/advanced_geomatics/outputs/"
geopackagePath = folder + "small_natural_earth.gpkg"


HMap.remove_layers_by_name(["Population"])

citiesName = "ne_50m_populated_places"
countriesName = "ne_50m_admin_0_countries"


countriesLayer = HVectorLayer.open(geopackagePath, countriesName)
countriesFeatures = countriesLayer.features()
popIndex = countriesLayer.field_index("POP_EST")
nameIndex = countriesLayer.field_index("NAME")


population_dict = {
 "name": "String",
 "population": "Integer"
 }
 
 
 # thematic styling
ranges = [
    [0, 1000000],
    [1000001, 80000000],
    [80000001, float('inf')],
]
styles = [
    HFill("green"),
    HFill("blue"),
    HFill("red"),
]


population_layer = HVectorLayer.new("Population", "Polygon", "EPSG:4326", population_dict)

for feature in countriesFeatures:
    name = feature.attributes[nameIndex]
    population = feature.attributes[popIndex]
    geometry = feature.geometry 
    geometry = feature.geometry
    population_layer.add_feature(geometry,[name, population])
  
population_layer.set_graduated_style('population', ranges, styles)  

HMap.add_layer(population_layer)    

    
output_path = output_folder + "population.gpkg"
error = population_layer.dump_to_gpkg(output_path, overwrite=True)
if(error):
    print(error)   