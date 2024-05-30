from pyqgis_scripting_ext.core import *

citiesName = "ne_50m_populated_places"
countriesName = "ne_50m_admin_0_countries"

HMap.remove_layers_by_name(["OpenStreetMap", "Cities in France", "France"])
osm = HMap.get_osm_layer()
HMap.add_layer(osm)


folder = "/Users/amelonelie/Documents/Master EMMA/semester 2/advanced geomatics+EIA/advanced geomatics/06/natural_earth_vector.gpkg/packages/"
geopackagePath = folder + "natural_earth_vector.gpkg"

citiesLayer = HVectorLayer.open(geopackagePath, citiesName)
countriesLayer = HVectorLayer.open(geopackagePath, countriesName)

countriesFeatures = countriesLayer.features()
nameIndex = countriesLayer.field_index("ADMIN")

for feature in countriesFeatures:
    if feature.attributes[nameIndex] == 'France':
        francegeom = feature.geometry # get the geometry
        print("GEOM:", francegeom.asWkt()[:50] + "...")

cityFeatures = citiesLayer.features()
citynameIndex = citiesLayer.field_index("NAME")

cityCoords = []
for feature in cityFeatures:
    citygeom = feature.geometry
    if citygeom.intersects(francegeom):
        intersection = citygeom.intersection(francegeom)
        cityCoords.append(intersection)
print(cityCoords[:20])  

fields = {
"id": "Integer",
}


citiesfrance = HVectorLayer.new("Cities in France", "Point", "EPSG:4326", fields)
countryfrance = HVectorLayer.new("France", "Polygon", "EPSG:4326", fields)
countryfrance.add_feature(francegeom, [1])

id = 1

for item in cityCoords:
    citiesfrance.add_feature(item, [id])
    id +=1



HMap.add_layer(countryfrance) 
HMap.add_layer(citiesfrance)  
 