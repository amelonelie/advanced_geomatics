from pyqgis_scripting_ext.core import *

csv_path = "/Users/amelonelie/Documents/Master EMMA/semester 2/advanced geomatics+EIA/advanced geomatics/03/03_exe0_geometries.csv"
with open(csv_path, 'r') as file:
    lines =file.readlines()

mypoints = []
point_sizes = []

mylines = []
line_sizes = []

mypolygons = []
poly_sizes = []

for line in lines:
    line = line.strip()   
    line = line.split(";")
    gtype = line[0]
    coords = line[1]
    
    if gtype == "point":
        cSplit = coords.split(",")
        my_point_lon = float(cSplit[0])
        my_point_lat = float(cSplit[1])
        my_point = HPoint(my_point_lon, my_point_lat)
        mypoints.append(my_point)
        point_size = int(line[2])
        point_sizes.append(point_size)
    elif gtype == "line":
        coordinates = line[1].split(" ")
        line_coords = []
        for item in coordinates:
            lat_lon = item.split(",")
            line_lon = float(lat_lon[0])
            line_lat= float(lat_lon[1])
            line_coords.append([line_lon, line_lat])
        line_obj = HLineString.fromCoords(line_coords)
        mylines.append(line_obj)
        line_size = int(line[2])
        line_sizes.append(line_size)
    elif gtype == "polygon":
        coordinates = line[1].split(" ")
        poly_coords = []
        for char in coordinates:
            lat_lon = char.split(",")
            poly_lon = float(lat_lon[0])
            poly_lat = float(lat_lon[1])
            poly_coords.append([poly_lon, poly_lat])
        poly_obj = HPolygon.fromCoords(poly_coords)
        mypolygons.append(poly_obj)
        poly_size = int(line[2])
        poly_sizes.append(poly_size)

canvas = HMapCanvas.new()

for i in range(len(mypoints)):
    canvas.add_geometry(mypoints[i], "red", point_sizes[i])

for i in range(len(mylines)):
    canvas.add_geometry(mylines[i], "blue", line_sizes[i])

for i in range(len(mypolygons)):
    canvas.add_geometry(mypolygons[i], "yellow", poly_sizes[i])

canvas.set_extent([0, 0, 50, 50])
canvas.show()
