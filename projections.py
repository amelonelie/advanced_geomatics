from pyqgis_scripting_ext.core import *

crsHelper = HCrs()
crsHelper.from_srid(4326) # special reference system id
crsHelper.to_srid(32632) # utm zone 32N
point4326 = HPoint(11, 46)
point32632 = crsHelper.transform(point4326)
print(f"{point4326.asWkt()} -> {point32632.asWkt()}")
backTo4326 = crsHelper.transform(point32632, inverse = True)
print(backTo4326.asWkt())

