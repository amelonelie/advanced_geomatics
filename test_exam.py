from pyqgis_scripting_ext.core import *

folder = "/Users/amelonelie/Documents/Master EMMA/semester 2/advanced geomatics+EIA/advanced geomatics/"
nasa1 = f"{folder}07/22yr_T10MN"
#part 1
with open(nasa1, 'r') as file:
    lines =file.readlines()

polygons = []
poly_dict = {}

for line in lines[14:]:
    line = line.strip()     
    line = line.split(" ")
    lat = float(line[0])
    lon = float(line[1])
    avg = float(line[-1])
    coords = [[lon, lat], [lon, lat+1], [lon+1, lat+1], [lon+1, lat], [lon, lat]]
    polygon = HPolygon.fromCoords(coords)
    polygons.append(polygon)
    poly_dict[polygon] = avg
   



# part 2
natural_earth = f"{folder}06/natural_earth_vector.gpkg/packages/natural_earth_vector.gpkg"

HMap.remove_layers_by_name(["OpenStreetMap", "min air temp"])
osm = HMap.get_osm_layer()
HMap.add_layer(osm)

countriesName = "ne_50m_admin_0_countries"
countriesLayer = HVectorLayer.open(natural_earth, countriesName)

selected_country = "Germany"


countriesFeatures = countriesLayer.features()

nameIndex = countriesLayer.field_index("NAME")

for feature in countriesFeatures:
    if feature.attributes[nameIndex] == selected_country:
        geometry = feature.geometry 




#part 3
selected_polygons_dict = {}

for key ,value in poly_dict.items():
    if not geometry.intersects(key):
        continue
    intersection = geometry.intersection(item)
    selected_polygons_dict[key] = value



fields = {
"id": "Integer",
}

min_air_temp = HVectorLayer.new("min air temp", "MultiPolygon", "EPSG:4326", fields)

id = 1

for key, value in selected_polygons_dict.items():
    min_air_temp.add_feature(key, [id])
    id +=1
    if value >= 0 and value <1:
        selected_polygons_dict[key] = [value, 1]
print(selected_polygons_dict)

  
HMap.add_layer(min_air_temp)       
 

# featuresList = []
# for ...
#     rect
#     value
#     feature = {
#     "geometry":rect, 
#     "temperature":value, 
#     }
#     featuresList.append(feature)
    
    
    
    