from pyqgis_scripting_ext.core import *

folder = "/Users/amelonelie/Documents/Programme/GitHub/advanced_geomatics/data/"
path = f"{folder}dpc-covid19-ita-regioni.csv"

folder2 = "/Users/amelonelie/Documents/Master EMMA/semester 2/advanced geomatics+EIA/advanced geomatics/06/natural_earth_vector.gpkg/packages/"
geopackagePath = folder2 + "natural_earth_vector.gpkg"

regionsName = "ne_10m_admin_1_states_provinces"
regionsLayer = HVectorLayer.open(geopackagePath, regionsName)


regionsFeatures = regionsLayer.features()
nameIndex = regionsLayer.field_index("NAME")
fieldNames = regionsLayer.field_names


with open(path, 'r') as file:
    covid_lines =file.readlines()
    

regions_dict = {
    "id": "Integer"
}

points = []
for line in covid_lines[1:5]:
    line = line.strip()   
    line = line.split(",")
    x_coord = float(line[4])
    y_coord = float(line[5])
    point = HPoint(x_coord, y_coord)

region_layer = HVectorLayer.new("Regions", "Polygon", "EPSG:4326", regions_dict)    
  
for feature in regionsFeatures:
    geom = feature.geometry 
    if geom.contains(point):
        result = geom
        
region_layer.add_feature(result,[1])  
HMap.add_layer(region_layer)


# dict key name of the region in csv file, value compele region (geometry)
#together
