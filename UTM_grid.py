# create UTM grid

# 60 zones a 6°

# coordinates = []
# number = 0
# for i in range(60):
#     coord = [[number,0], [number,180], [number+6,180], [number+6,0], [number,0]]
#     coordinates.append(coord)
#     number +=6

# multipolygon = HMultiPolygon.fromCoords(coordinates)
# canvas = HMapCanvas.new()
# canvas.add_geometry(multipolygon, "red", 2)
# canvas.set_extent([-10, -10, 370, 10])
# canvas.show()


polygons = []
extent = 6
for lon in range(-180, 180, extent):
    minX = lon
    maxX = lon + extent
    minY = -84
    maxY = 84
    coords = [[minX, minY], [minX, maxY], [maxX, maxY],[maxX, minY] ,[minX, minY]]
    polygon = HPolygon.fromCoords(coords)
    polygons.append(polygon)
    
    
canvas = HMapCanvas.new()   
osm = HMap.get_osm_layer()
canvas.set_layers([osm])

for polygon in polygons: 
    canvas.add_geometry(polygon)


canvas.set_extent([-180, -84, 180, 84])
canvas.show()