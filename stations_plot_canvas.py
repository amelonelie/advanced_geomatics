from pyqgis_scripting_ext.core import *
folder = "/Users/amelonelie/Documents/Master EMMA/semester 2/advanced geomatics+EIA/advanced geomatics/03/"
path = f"{folder}stations.txt"

with open(path, 'r') as file:
     station_lines =file.readlines()
     
stations = []     
countries = {}
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
    country = stationSplit[2]
    count = countries.get(country, 0)
    count += 1 
    countries[country] = count

for key, value in countries.items():
    print(key, ":", value)
    
#projection
canvas = HMapCanvas.new()
crsHelper = HCrs()
crsHelper.from_srid(4326)
crsHelper.to_srid(3857)   

for station in stations:
    proj_station = crsHelper.transform(station)
    canvas.add_geometry(proj_station, "red", 2)

osm = HMap.get_osm_layer()
canvas.set_layers([osm])

    
canvas.set_extent([-1500000, 4000000, 6000000, 10000000])
canvas.show()