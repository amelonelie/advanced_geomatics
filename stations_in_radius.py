from pyqgis_scripting_ext.core import *

folder = "/Users/amelonelie/Documents/Programme/GitHub/advanced_geomatics/data/"
path = f"{folder}stations.txt"

with open(path, 'r') as file:
     station_lines =file.readlines()
     
radius = 20000
stations = []     
station_dict = {}
crsHelper = HCrs()
crsHelper.from_srid(4326)
crsHelper.to_srid(32632) 


for line in station_lines:
    if line.startswith("#") or len(line) == 0:
        continue
    stationSplit = line.split(",") 
    
    long = stationSplit[4]
    longSplit = long.split(":")
    long_deg = int(longSplit[0].replace("+", ""))
    long_min = int(longSplit[1])/60
    long_sec = int(longSplit[2])/3600
    longitude = long_deg+long_min+long_sec
    
    lat = stationSplit[3]
    latSplit = lat.split(":")
    lat_deg = int(latSplit[0].replace("+", ""))
    lat_min = int(latSplit[1])/60
    lat_sec = int(latSplit[2])/3600
    latitude = lat_deg+lat_min+lat_sec
    
    point = HPoint(longitude, latitude)
    proj_point = crsHelper.transform(point)
    stations.append(proj_point)
    
    station_name = stationSplit[1].strip()
    station_dict[station_name] = proj_point  
      
  
location = HPoint(11.34999, 46.49809)
proj_location = crsHelper.transform(location)
buffer_polygon = proj_location.buffer(radius)
stations_in_radius = {}

for key,value in station_dict.items():
    if buffer_polygon.contains(value):
        proj_value = crsHelper.transform(value, inverse = True)
        stations_in_radius[key] = [proj_value, value]
      
for key, value in stations_in_radius.items():
    distance = (proj_location.distance(value[1]))/1000
    print(f"{key} {distance:.2f}km -> {value[0]}")
