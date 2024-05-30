from pyqgis_scripting_ext.core import *


HMap.remove_layers_by_name(["Population"])

citiesName = "ne_50m_populated_places"
countriesName = "ne_50m_admin_0_countries"

folder = "/Users/amelonelie/Documents/Master EMMA/semester 2/advanced geomatics+EIA/advanced geomatics/06/natural_earth_vector.gpkg/packages/"
geopackagePath = folder + "natural_earth_vector.gpkg"

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
    [80000001, 100000000000],
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

    
path = folder + "population.gpkg"
error = population_layer.dump_to_gpkg(path, overwrite=True)
if(error):
    print(error)   