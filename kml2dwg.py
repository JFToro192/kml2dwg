import osgeo.ogr as ogr

"'N0233 Flums - Murg' Section #1, 50kV, 'AAAC_300', from Str. #Tragwerk 69 Set 21 'Kette A1-L-1.1' to Str. #Tragwerk 70 Set 41 'Kette A1-L-1.2', Section at 40°C 'Initial FE', Notes_ '50 kV Flums - Murg;L_;Axpo;'"

# specify input and output file paths
input_kml_path = './input/input.kml'
output_shapefile_path = './output/output.shp'

# open the KML file
kml_driver = ogr.GetDriverByName('KML')
kml_ds = kml_driver.Open(input_kml_path, 0)  # 0 means read-only

# create the shapefile
shapefile_driver = ogr.GetDriverByName('ESRI Shapefile')
shapefile_ds = shapefile_driver.CreateDataSource(output_shapefile_path)

# loop through the layers in the KML file
for kml_layer in kml_ds:
    # create a new layer in the shapefile
    shapefile_layer = shapefile_ds.CreateLayer(kml_layer.GetName(), geom_type=ogr.wkbUnknown)

    # add the fields from the KML layer to the shapefile layer
    for field in kml_layer.schema:
        shapefile_layer.CreateField(field)

    # loop through the features in the KML layer and add them to the shapefile layer
    for kml_feature in kml_layer:
        # create a new feature in the shapefile layer
        shapefile_feature = ogr.Feature(shapefile_layer.GetLayerDefn())

        # set the geometry of the shapefile feature to be the same as the KML feature
        shapefile_feature.SetGeometry(kml_feature.GetGeometryRef())

        # copy the attributes from the KML feature to the shapefile feature
        for i in range(kml_feature.GetFieldCount()):
            value = kml_feature.GetField(i)
            shapefile_feature.SetField(i, value)

        # add the feature to the shapefile layer
        shapefile_layer.CreateFeature(shapefile_feature)

# close the data sources
kml_ds = None
shapefile_ds = None
