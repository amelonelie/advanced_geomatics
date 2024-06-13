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
    
    if index < 50000:
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
            
            for regionname, regionGeometry in regionName2GeometryMap.items():
                if regionGeometry.intersects(dataPoint):
                    featuresList = day2featuresMap.get(day)
                    if featuresList:
                        featuresList.append((regionGeometry, [day, region, totalCases]))
                    else:
                        featuresList = [(regionGeometry, [day, region, totalCases])]
                        
                    day2featuresMap[day] = featuresList


imagePathsList = []

for day, featuresList in day2featuresMap.items():
  #  if day != "2020-04-01":
   #     continue
        
    #print("Generating day", day)   
    newLayerName = "covid_italy" 
    HMap.remove_layers_by_name([newLayerName])  
  
    schema = {
        "day":"string", 
        "region":"string",
        "totalCases": "Int"
    }
    
    covidLayer = HVectorLayer.new(newLayerName, "MultiPolygon", "EPSG:4326", schema)
           
    for geometry, attributes in featuresList:
        covidLayer.add_feature(geometry, attributes)
    
    # style = HFill('yellow') + HStroke('black', 0.5)
    # covidLayer.set_style(style)
    
    ranges = [
    [float('-inf'), 1000], 
    [1001, 3000], 
    [3001, 10000], 
    [10001, 40000], 
    [40001, 1000000], 
    [1000001, float('inf')]
    ]
    #set styles according to cases
    styles = [
    HFill('blue') + HStroke('white', 0.5),
    HFill('green') + HStroke('white', 0.5),
    HFill('yellow') + HStroke('white', 0.5),
    HFill('orange') + HStroke('white', 0.5),
    HFill('red') + HStroke('white', 0.5),
    HFill('black') + HStroke('white', 0.5),
    ]
    
    labelStyle = HLabel('totalCases', size = 8, color = 'black') + HHalo() + HFill()
    covidLayer.set_graduated_style("totalCases", ranges, styles, labelStyle)
    HMap.add_layer(covidLayer)
  
    printer = HPrinter(iface)
    mapProperties = {
    "x": 5, 
    "y":25, 
    "width":285, 
    "height":180,
    "frame":True, 
    "extent": provincesLayer.bbox()
    }
    printer.add_map(**mapProperties)
    
    imageName = f"{day}_covid.png"
    imagePath = f"{outputFolder}/{imageName}"
    printer.dump_to_image(imagePath)
    imagePathsList.append(imagePath)
  
  
from PIL import Image

imagesList = []
for path in imagePathsList:
    img = Image.open(path)
    imagesList.append(img)
animationPath = f"{outputFolder}/covid_animation.gif"


imagesList[0].save(animationPath, save_all = True, append_images=imagesList[1:], duration = 500)

for path in imagePathsList:
    os.remove(path)


