# GlTF/de
## Beschreibung

The [GL Transmission Format](https://www.khronos.org/gltf/) (glTF™) is a royalty-free specification for the efficient transmission and loading of 3D scenes and models by applications. It minimizes both the size of 3D assets, and the runtime processing needed to unpack and use those assets.

## Installation

According to this [forum thread](https://forum.freecadweb.org/viewtopic.php?f=8&t=31680&p=450917&#p450658), OCC must be compiled with RapidJSON support in order to utilize glTF features. Therefore set the option `USE_RAPIDJSON` in the CMake configuration step. This requires the package rapidjson-dev.



## Importieren

Currently not supported in FreeCAD.



## Exportieren

Since FreeCAD version 0.19.23074 the [Std Export](Std_Export.md) command can export to the gITF format.

### Alternative export solutions 

For earlier versions these workarounds can be used:

1\. Export as STEP → Import into CAD Assistant from Opencascade -\> Export to glTF

OR

2\. Use the `cqparts` Python library ([website](https://github.com/cqparts/cqparts)): {{code|
import cqparts
cqparts.Assembly.importer('step')('myfile.stp').exporter('gltf')('myfile.gltf')
}}

Source: [Forum thread](https://forum.freecadweb.org/viewtopic.php?f=8&t=31680&p=449977#p449977)

## Related

-   [Import Export](Import_Export.md)
-   [FreeCAD Howto Import Export](FreeCAD_Howto_Import_Export.md)



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > GlTF/de
