from pyqgis_scripting_ext.core import *


folder = "/Users/amelonelie/Documents/Programme/GitHub/advanced_geomatics/data/"
path = f"{folder}stations.txt"

with open(path, 'r') as file:
     station_lines =file.readlines()
     
stations = []     
station_dict = {}
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
    stations.append(point)
    
    station_name = stationSplit[1].strip()
    station_dict[station_name] = point  
      
crsHelper = HCrs()
crsHelper.from_srid(4326)
crsHelper.to_srid(32632)   

for station in stations:
    proj_station = crsHelper.transform(station)

location = HPoint(11.34999, 46.49809)

closest_distance = float('inf')
closest_station = None

for key,value in station_dict.items():
    distance = location.distance(value)
    if distance < closest_distance:
        closest_distance = distance
        closest_station = key
        closest_coordinates = value
print(closest_station, "->", closest_coordinates)


