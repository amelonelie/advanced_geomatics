from pyqgis_scripting_ext.core import *

folder = "/Users/amelonelie/Documents/Master EMMA/semester 2/advanced geomatics+EIA/advanced geomatics/03/"
path = f"{folder}stations.txt"
HMap.remove_layers_by_name(["Stations"])

with open(path, 'r') as file:
    station_lines =file.readlines()
 
headers = []
fields_dict = {}

for line in station_lines[:5]:
    line = line.strip()      
    if line.startswith("#"):
        fields = line[1:].split(",")
    for item in fields:
        item = item.strip()
        if item == "CN" or item == "STANAME" :
            fields_dict[item] = "String"
        elif item == "STAID" or item == "HGHT":
            fields_dict[item] = "Integer"
        elif item =="LAT" or item == "LON":
            fields_dict[item] = "double"
        headers.append(item)

station_layer = HVectorLayer.new("Stations", "Point", "EPSG:4326", fields_dict)

print(fields_dict) 
 

for line in station_lines:
    if line.startswith("#") or len(line) == 0:
        continue
    stationSplit = line.split(",") 
    statid = stationSplit[0].strip()
    statname = stationSplit[1].strip()
    statcn = stationSplit[2].strip()
    statheight = stationSplit[5].strip()

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
    station_layer.add_feature(point,[statid, statname, statcn, latitude, longitude, statheight])


path = folder + "stations.gpkg"
error = station_layer.dump_to_gpkg(path, overwrite=True)
if(error):
    print(error)
    
HMap.add_layer(station_layer)         



