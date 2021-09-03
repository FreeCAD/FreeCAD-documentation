 {{UnfinishedDocu}}





{{TOCright}}

## Description

Toolbits are the foundation of the [Path Tools](Path_Tools.md) system. They represent a specific tool that can be used in a Path Job to generate a toolpath. Each toolbit is stored as a JSON file. JSON is structured data that can be easily parsed by macros or python scripts but remains human readable. Describing toolbits with JSON allows for the possibility of automatically creating large collections of accurate toolbits automatically or with a script.

Storing a tool as a JSON file sounds great but eliminates the option of an accurate thumbnail or solid body representation. On the other hand, if each toolbit were created as a FreeCAD object, obtaining the solid body would be simple but would require enormous storage for large tool collections. Also automatically creating toolbits as FreeCAD objects would be difficult or impossible.

Instead, the toolbit is a hybrid. The JSON file contains the file path to the toolshape file and values for all parameters required to create the specific toolbit.

When a tool is instantiated in a job the a body is created from the template and the constraints are set according to the values from the JSON file. All additional parameters are created as properties on the object. This provides the the correct shape and dimensions which can be used to generate a point cloud or mesh for advanced algorithms (and potentially simulation).

## Usage

Within the FreeCAD GUI the Path toolbit library manager provides a mechanism to create a new toolbit. A single toolbit can exist in multiple toolbit libraries.

1.  Open the Path Toolbit manager.
2.  Select a library.
3.  Create a Toolbit.

## JSON Structure 


{{Code|
{
  "version": 2,
  "name": "T1",
  "shape": "endmill.fcstd",
  "attribute": {},
  "parameter": {
    "CuttingEdgeHeight": "30.000 mm",
    "Diameter": "1.000 mm",
    "Length": "50.000 mm",
    "ShankDiameter": "3.000 mm"
  }
}
}}

## Options

## Related

-   [Path Tools](Path_Tools.md)
-   [Path ToolBitLibraryOpen](Path_ToolBitLibraryOpen.md)





{{Path_Tools_navi

}} 
