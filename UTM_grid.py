# create UTM grid

# 60 zones a 6°

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