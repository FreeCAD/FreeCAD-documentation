# Arch SHP
## Description

FreeCAD is able to import [shapefiles](https://en.wikipedia.org/wiki/Shapefile)

The importer uses the shapefile.py library from <https://github.com/GeospatialPython/pyshp>, it is not found on your system on first run, the importer will propose to download and install it for you.

Shapefiles are composed of 3 files (a .shp, a .shx and a .dbf file), any of them can be used with this importer. They are composed of 2D objects of one geometry type, that can be polygons/faces, polylines or point cloud (all 3 types are supported by this importer), and custom fields, for which each face, polyline or point in the shapefile has a value. This is the real gem of GIS, to bind a database with geometry. The most common use is to have one field to represent the elevation coordinate of each shape in the file. On opening the file, the importer will ask you what field to get shape elevations from.

One shape will be created from each shapefile in FreeCAD.

Note that all the question of georeferenced units, with hundreds of projection systems used worldwide, is not treated at the moment. The coordinates from the file are used \"as is\".

## Related

-   FreeCAD Forum thread announcement [Shapefile Importer](https://forum.freecadweb.org/viewtopic.php?f=9&t=46150)
-   Forum thread on [OSArch](https://community.osarch.org/discussion/comment/578#Comment_578) discussion
-   [Import Export](Import_Export.md)
-   [FreeCAD Howto Import Export](FreeCAD_Howto_Import_Export.md)
-   [Import Export Preferences](Import_Export_Preferences.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [File Formats](Category_File Formats.md) > [Arch](Arch_Workbench.md) > Arch SHP
