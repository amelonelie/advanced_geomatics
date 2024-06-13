from pyqgis_scripting_ext.core import *

folder = "/Users/amelonelie/Documents/Programme/GitHub/advanced_geomatics/data/"
path = f"{folder}dpc-covid19-ita-regioni.csv"
geopackagePath = folder + "small_natural_earth.gpkg"

provincesName = "ne_10m_admin_1_states_provinces"
regionsLayer = HVectorLayer.open(geopackagePath, regionsName)
outputFolder = "/Users/amelonelie/Documents/Programme/GitHub/advanced_geomatics/outputs/covid_images"

HMap.remove_layers_by_name([provincesName])



provincesLayer = HVectorLayer.open(geopackagePath, provincesName)
provincesLayer.subset_filter("iso_a2='IT'")

# create a dictionary containing the region name and its geometry
regionName2GeometryMap = {}

regionIndex = provincesLayer.field_index("region")

for provinceFeature in provincesLayer.features():
    geometry = provinceFeature.geometry
    regionName = provinceFeature.attributes[regionIndex]
    
    regionGeometry = regionName2GeometryMap.get(regionName)
    if regionGeometry:
        regionGeometry = regionGeometry.union(geometry)
    else:
        regionGeometry = geometry
    regionName2GeometryMap[regionName] = regionGeometry
   
for name, geom in regionName2GeometryMap.items():
    print(name)

with open(path, 'r') as file:
    lines = file.readlines()
    
    
day2featuresMap = {}

 
for index, line in enumerate(lines):
    line = line.strip()
    
    if index < 500:
        lineSplit = line.split(",")
        # 0 -> date
        # 3 -> region
        # 17 -> total cases
        dayAndTime = lineSplit[0]
        dayAndTime = dayAndTime.split("T")
        day = dayAndTime[0]
        
        if day.endswith("01"):
            region = lineSplit[3]
            totalCases = int(lineSplit[17])
            lat = float(lineSplit[4])
            lon = float(lineSplit[5])
            dataPoint = HPoint(lon, lat)
            print(day)
            
            for regionname, regionGeometry in regionName2GeometryMap.items():
                if regionGeometry.intersects(dataPoint):
                    featuresList = day2featuresMap.get(day)
                    if featuresList:
                        featuresList.append((regionGeometry, [day, region, totalCases]))
                    else:
                        featuresList = [(regionGeometry, [day, region, totalCases])]
                        
                    day2featuresMap[day] = featuresList
                    
                    
                    
HMap.add_layer(provincesLayer)


# regionsFeatures = regionsLayer.features()
# nameIndex = regionsLayer.field_index("NAME")
# fieldNames = regionsLayer.field_names


# with open(path, 'r') as file:
#     covid_lines =file.readlines()
    

# regions_dict = {
#     "id": "Integer"
# }

# points = []
# for line in covid_lines[1:5]:
#     line = line.strip()   
#     line = line.split(",")
#     x_coord = float(line[4])
#     y_coord = float(line[5])
#     point = HPoint(x_coord, y_coord)

# region_layer = HVectorLayer.new("Regions", "Polygon", "EPSG:4326", regions_dict)    
  
# for feature in regionsFeatures:
#     geom = feature.geometry 
#     if geom.contains(point):
#         result = geom
        
# region_layer.add_feature(result,[1])  
# HMap.add_layer(region_layer)


# # dict key name of the region in csv file, value compele region (geometry)
# #together
