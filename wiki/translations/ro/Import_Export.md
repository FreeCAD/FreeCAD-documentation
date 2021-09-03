\_\_NOTOC\_\_ 




## Introduction


<div class="mw-translate-fuzzy">

Această pagină adună diferite formate de fișiere care pot fi importate sau exportate din FreeCAD. Cele mai multe dintre aceste formate de fișiere sunt implementate de un anumit modul. Acest modul nu trebuie să fie încărcat pentru a importa sau a exporta în acest format, dar trebuie să fie încărcat pentru a afișa pagina preferințelor corespunzătoare.


</div>

## Related

See the following pages for additional information:

-   [Import Export Preferences](Import_Export_Preferences.md)
-   [FreeCAD Howto Import Export](FreeCAD_Howto_Import_Export.md)

## Overview of file formats 


<div class="mw-translate-fuzzy">

  Format                                     Description                                                                                                                                Import   Export   Module                                                                          Preferences page
  ------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------ -------- -------- ------------------------------------------------------------------------------- ------------------
  [FCStd](Fcstd_file_format.md)      FreeCAD\'s native file format                                                                                                              yes      yes      Built-in                                                                        no
  [FCMat](Material.md)               FreeCAD Material Card                                                                                                                      yes      yes      Built-in                                                                        no
  [FCMacro](Macros.md)               FreeCAD Macro                                                                                                                              yes      yes      Built-in                                                                        no
  STEP                                       One of the most widely used exchange format for engineering models                                                                         yes      yes      [Part](Part_Workbench.md)                                               yes
  STPZ                                       Compressed version of STEP exchange format for engineering models                                                                          yes      yes      [Part](Part_Workbench.md)                                               yes
  IGES                                       A bit older but still much in use solid-based format                                                                                       yes      yes      [Part](Part_Workbench.md)                                               yes
  BREP                                       OpenCasCade\'s native format                                                                                                               yes      yes      [Part](Part_Workbench.md)                                               no
  [DXF](Draft_DXF.md)                Autodesk Exchange Format. Only 2D geometry is supported                                                                                    yes      yes      [Draft](Draft_Workbench.md)                                             yes
  [DWG](FreeCAD_and_DWG_Import.md)   Autocad main format. Only 2D geometry is supported. Requires the installation of [external software](FreeCAD_and_DWG_Import.md).   yes      yes      [Draft](Draft_Workbench.md)                                             yes
  [SVG](Draft_SVG.md)                2D format widely used for vector graphics                                                                                                  yes      yes      [Draft](Draft_Workbench.md) / [Drawing](Drawing_Workbench.md)   yes
  [OCA](Draft_OCA.md)                Open CAD Format (obsolete, 2D-only format)                                                                                                 yes      yes      [Draft](Draft_Workbench.md)                                             yes
  [IFC](Arch_IFC.md)                 Industry Foundation Classes, used to exchange BIM models. Requires the installation of [external software](Arch_IFC.md).           yes      yes      [Arch](Arch_Workbench.md)                                               yes
  [DAE](Arch_DAE.md)                 Collada format, used for exchange of mesh geometry                                                                                         yes      yes      [Arch](Arch_Workbench.md)                                               yes
  [OBJ](Arch_OBJ.md)                 Mesh exchange format                                                                                                                       yes      yes      [Arch](Arch_Workbench.md) / [Mesh](Mesh_Workbench.md)           no
  STL                                        Mesh exchange format mostly used for 3D printing                                                                                           yes      yes      [Mesh](Mesh_Workbench.md)                                               no
  BMS                                        Binary mesh exchange format                                                                                                                yes      yes      [Mesh](Mesh_Workbench.md)                                               no
  AST                                        Mesh exchange format                                                                                                                       yes      yes      [Mesh](Mesh_Workbench.md)                                               no
  OFF                                        Mesh exchange format                                                                                                                       yes      yes      [Mesh](Mesh_Workbench.md)                                               no
  PLY                                        Mesh exchange format / Points cloud                                                                                                        yes      yes      [Mesh](Mesh_Workbench.md) / [Points](Points_Workbench.md)       no
  INP                                        Abaqus format                                                                                                                              yes      yes      [FEM](FEM_Workbench.md)                                                 no
  POLY                                       Tetgen format                                                                                                                              no       yes      [FEM](FEM_Workbench.md)                                                 no
  UNV                                        FEM exchange format                                                                                                                        yes      yes      [FEM](FEM_Workbench.md)                                                 no
  MED                                        FEM exchange format                                                                                                                        yes      yes      [FEM](FEM_Workbench.md)                                                 no
  DAT                                        FEM exchange format (FEM) or 2D airfoil profile (Draft)                                                                                    yes      yes      [FEM](FEM_Workbench.md) / [Draft](Draft_Workbench.md)           no
  BDF                                        FEM exchange format                                                                                                                        yes      no       [FEM](FEM_Workbench.md)                                                 no
  FRD                                        CalculiX result format                                                                                                                     yes      no       [FEM](FEM_Workbench.md)                                                 no
  NC                                         G-Code file format                                                                                                                         yes      yes      [Path](Path_Workbench.md)                                               no
  GC                                         G-Code file format                                                                                                                         yes      yes      [Path](Path_Workbench.md)                                               no
  NCC                                        G-Code file format                                                                                                                         yes      yes      [Path](Path_Workbench.md)                                               no
  NGC                                        G-Code file format                                                                                                                         yes      yes      [Path](Path_Workbench.md)                                               no
  CNC                                        G-Code file format                                                                                                                         yes      yes      [Path](Path_Workbench.md)                                               no
  TAP                                        G-Code file format                                                                                                                         yes      yes      [Path](Path_Workbench.md)                                               no
  GCODE                                      G-Code file format                                                                                                                         yes      yes      [Path](Path_Workbench.md)                                               no
  EMN                                        IDF file format                                                                                                                            yes      no       Idf                                                                             no
  IV                                         OpenInventor file format                                                                                                                   yes      yes      Built-in                                                                        no
  VRML                                       Web 3D format                                                                                                                              yes      yes      Built-in                                                                        no
  WebGL (HTML)                               Web 3D format                                                                                                                              no       yes      [Arch](Arch_Workbench.md)                                               no
  SCAD                                       OpenSCAD file format                                                                                                                       yes      yes      [OpenSCAD](OpenSCAD_Workbench.md)                                       no
  CSG                                        OpenSCAD Constructive Solid Geometry                                                                                                       yes      yes      [OpenSCAD](OpenSCAD_Workbench.md)                                       no
  ASC                                        Points cloud format                                                                                                                        yes      no       [Points](Points_Workbench.md)                                           no
  POV                                        Povray format                                                                                                                              no       yes      [Raytracing](Raytracing_Workbench.md)                                   no
  CSV                                        Comma-separated values spreadsheet                                                                                                         yes      yes      [Spreadsheet](Spreadsheet_Workbench.md)                                 no
  PDF                                        Adobe portable document format                                                                                                             no       yes      Built-in                                                                        no


</div>







[Category:File\_Formats{{\#translation:}}](Category:File_Formats.md)
