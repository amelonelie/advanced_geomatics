from pyqgis_scripting_ext.core import *

folder = "/Users/amelonelie/Documents/Programme/GitHub/advanced_geomatics/data/"
path = f"{folder}dpc-covid19-ita-regioni.csv"

folder2 = "/Users/amelonelie/Documents/Master EMMA/semester 2/advanced geomatics+EIA/advanced geomatics/06/natural_earth_vector.gpkg/packages/"
geopackagePath = folder2 + "natural_earth_vector.gpkg"
countriesName = "ne_50m_admin_0_countries"
citiesName = "ne_50m_populated_places"
countriesLayer = HVectorLayer.open(geopackagePath, countriesName)


countriesFeatures = countriesLayer.features()
nameIndex = countriesLayer.field_index("NAME")
fieldNames = countriesLayer.field_names


for feature in countriesFeatures:
    if feature.attributes[nameIndex] == 'Italy':
        geom = feature.geometry 


with open(path, 'r') as file:
    covid_lines =file.readlines()
    



for line in covid_lines[:5]:
    line = line.strip()   
    line = line.split(",")
    x_coord = line[4]
    y_coord = line[5]
  
    