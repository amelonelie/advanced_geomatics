from pyqgis_scripting_ext.core import *


g1 = HPolygon.fromCoords([[0, 0], [0, 5], [5, 5], [5, 0], [0, 0]])
g2 = HPolygon.fromCoords([[5, 0], [5, 2], [7, 2], [7, 0], [5, 0]])
g3 = HPoint(4, 1)
g4 = HPoint(5, 4)
g5 = HLineString.fromCoords([[1, 0], [1, 6]])
g6 = HPolygon.fromCoords([[3, 3], [3, 6], [6, 6], [6, 3], [3, 3]])


canvas = HMapCanvas.new()

canvas.add_geometry(g1, 'black', 3)
canvas.add_geometry(g2, 'magenta', 3)
canvas.add_geometry(g6, 'orange', 3)
canvas.add_geometry(g5, 'green', 3)
canvas.add_geometry(g3, 'blue', 10)
canvas.add_geometry(g4, 'red', 10)
canvas.set_extent([-1, -1, 8, 8])
canvas.show()