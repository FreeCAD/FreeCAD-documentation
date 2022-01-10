# Installing additional components/en
{{TOCright}}

# Introduction

After installing FreeCAD for your operating system ([Windows](Installing_on_Windows.md), [Linux](Installing_on_Linux.md) or [Mac](Installing_on_Mac.md)), you may want to consider installing one or more of the following additional components.

# Help files 

The offline documentation is not shipped with all installers, but it is available as a separate package. See the [Installing Helpfile](Installing_Helpfile.md) page for more information.

# External workbenches 

Apart from the default [workbenches](workbenches.md) bundled with FreeCAD, there is a large collection of useful [external workbenches](External_workbenches.md) made by community members.

# Third party software 

FreeCAD supports several third party software packages out of the box. In many cases all you need to do is install the software, and when FreeCAD is restarted it will automatically find and be able to use it. This section aims to provide a list of such software packages, together with some information about where they are used in FreeCAD and where they can be downloaded.

## Support

### GitPython

_ can use this library. GitPython is included in the FreeCAD installers for Windows and Mac.

### GraphViz

_ tool.

### OpenCAMLib

_. See the [OpenCamLib](OpenCamLib.md) page for installation instructions.

### OpenSCAD

_ depends on this software and the [Mesh Workbench](Mesh_Workbench.md) uses it for its Boolean tools. It is also required for the import of SCAD files with the [Std Import](Std_Import.md) tool.

## File formats 

All software in this section will be used by the [Std Import](Std_Import.md) or [Std Export](Std_Export.md) tools.

### CADExchanger

[CADExchanger](https://cadexchanger.com) is a commercial application for exchanging various CAD file formats. There is an [external workbench](https://github.com/yorikvanhavre/CADExchanger) to use this application in FreeCAD.

### DXF Importer 

FreeCAD has a native importer and exporter for DXF files, programmed in C++. Currently they do not implement all features of the DXF format. For those features the legacy Python importer and exporter are still available. These require the _ page for more information.

### DWG converters 

FreeCAD cannot directly read and write DWG files. To convert DXF files to DWG files, and vice-versa, FreeCAD relies on external converters. There is built-in support for the following DWG converters:

-   [LibreDWG](https://www.gnu.org/software/libredwg) (open-source, lacks support for some DWG entities).
-   [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter) (free, but not open-source).
-   [QCAD pro](https://qcad.org/en/qcad-command-line-tools#dwg2dwg) (commercial). <small>(v0.20)</small> 

See [Import Export Preferences](Import_Export_Preferences#DWG.md) and [FreeCAD and DWG Import](FreeCAD_and_DWG_Import.md) for more information.

### IfcOpenShell

_ ({{VersionMinus|0.18}}) and [BIM IfcExplorer](BIM_IfcExplorer.md) tools. IfcOpenShell is included in the FreeCAD installers for Windows and Mac.

### IfcJson

[IfcJson](https://github.com/buildingSMART/ifcJSON) is a library required for exporting to the IFCJSON file format. IFCJSON is a new IFC format that is not yet supported by many applications.

### Pycollada

[Pycollada](https://github.com/pycollada/pycollada/releases), also known as python-collada, is a Python library to read and write Collada (DAE) files. Pycollada is included in the FreeCAD installers for Windows and Mac.

## Rendering

### LuxCoreRender

_ project. Officially it is not supported by the _ page for more information and installation instructions.

### LuxRender

_. In 2013 the project has been rebooted becoming _ may work with the Raytracing Workbench, it might be worth to give it a try. See the [LuxRender](LuxRender.md) page for more information and installation instructions, and the [LuxCoreRender](LuxCoreRender.md) if you want to try a more modern software.

### POV-Ray 

_. See the [POV-Ray](POV-Ray.md) page for more information and installation instructions.

## Finite element 

### CalculiX

_ tool.

### Gmsh

_ and [Mesh FromPartShape](Mesh_FromPartShape.md) tools.

### Elmer

_ tool.

### FEniCS

_

### Z88

_ tool. FreeCAD requires the open source Z88OS package.

### OpenFOAM

_ and _.

# Related pages 

-   [Import Export](Import_Export.md)
-   [Import Export Preferences](Import_Export_Preferences.md)
-   [Third Party Libraries](Third_Party_Libraries.md)




_

---
[documentation index](../README.md) > Installing additional components/en
