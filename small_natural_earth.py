from pyqgis_scripting_ext.core import *
old_folder = "/Users/amelonelie/Documents/Master EMMA/semester 2/advanced geomatics+EIA/advanced geomatics/06/natural_earth_vector.gpkg/packages/"
#use this old folder to access the full natural earth package to create a smaller one


geopackagePath = old_folder + "natural_earth_vector.gpkg"
folder = "/Users/amelonelie/Documents/Programme/GitHub/advanced_geomatics/data/"

citiesName = "ne_50m_populated_places"
countriesName = "ne_50m_admin_0_countries"
regionsName = "ne_10m_admin_1_states_provinces"
riversName = "ne_10m_rivers_lake_centerlines_scale_rank"

countriesLayer = HVectorLayer.open(geopackagePath, countriesName)
citiesLayer = HVectorLayer.open(geopackagePath, citiesName)
regionsLayer = HVectorLayer.open(geopackagePath, regionsName)
riversLayer = HVectorLayer.open(geopackagePath, riversName)


saving_path = folder + "small_natural_earth.gpkg"
print(saving_path)

countriesLayer.dump_to_gpkg(saving_path, overwrite=True)
citiesLayer.dump_to_gpkg(saving_path, overwrite=False)
regionsLayer.dump_to_gpkg(saving_path, overwrite=False)
riversLayer.dump_to_gpkg(saving_path, overwrite=False)