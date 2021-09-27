# Import Export/es
## Introducción

En esta página se enumeran los diversos formatos de archivo que FreeCAD puede importar y exportar. Para completar la lista se incluye el formato nativo de FreeCAD. Algunos formatos tienen una página wiki relacionada a la que se puede acceder haciendo clic en la extensión en la primera columna.

## Relacionados

Ver las siguientes páginas para obtener información adicional:

-   [Preferencias de importación y exportación](Import_Export_Preferences/es.md)
-   [FreeCAD Cómo importar y exportar](FreeCAD_Howto_Import_Export/es.md)

## Vista general de los formatos archivo 


<div class="mw-translate-fuzzy">

  Formato                                       Descripción                                                                                                                                         Importar   Exportar   Modulo                                                                                  Pagina de preferencias
  --------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------- ---------- ---------- --------------------------------------------------------------------------------------- ------------------------
  [FCStd](Fcstd_file_format/es.md)      Formato de archivo nativo de FreeCAD                                                                                                                si         si         Incorporado                                                                             no
  [FCMat](Material/es.md)               Tarjeta de material de FreeCAD                                                                                                                      si         si         Incorporado                                                                             no
  [FCMacro](Macros/es.md)               Macro de FreeCAD                                                                                                                                    si         si         Incorporado                                                                             no
  STEP                                          Uno de los mas ampliamente usado formato de intercambio para modelos de ingenieria                                                                  si         si         [Part](Part_Workbench/es.md)                                                    si
  IGES                                          Un poco viejo pero todavia sigue mucho en uso de formato basado-solido                                                                              si         si         [Part](Part_Workbench/es.md)                                                    si
  BREP                                          Formato nativo de OpenCasCade                                                                                                                       si         si         [Part](Part_Workbench/es.md)                                                    no
  [DXF](Draft_DXF/es.md)                Formato de intercambio Autodesk. Solo geometrica 2D es soportada                                                                                    si         si         [Draft](Draft_Workbench/es.md)                                                  si
  [DWG](FreeCAD_and_DWG_Import/es.md)   Formato principal de Autocad.Solo geometria 2D soportada. Requiere de la instalación de [software externo](FreeCAD_and_DWG_Import/es.md).   si         si         [Borrador](Draft_Workbench/es.md)                                               si
  [SVG](Draft_SVG/es.md)                Formato 2D ampliamente utilizado por gráficos vectoriales                                                                                           si         si         [Borrador](Draft_Workbench/es.md) / [Dibujo](Drawing_Workbench/es.md)   si
  [OCA](Draft_OCA/es.md)                Open CAD Format (obsolete, 2D-only format)                                                                                                          yes        yes        [Borrador](Draft_Workbench/es.md)                                               yes
  [IFC](Arch_IFC.md)                    Clases de origen industrial, utilizado para intercambiar modelos. Requiere la instalación de [software externo](Arch_IFC/es.md).            si         si         [Arquitectura](Arch_Workbench/es.md)                                            si
  [DAE](Arch_DAE/es.md)                 Formato collada, utilizado para intercambio de geometrías de malla                                                                                  si         si         [Arquitectura](Arch_Workbench/es.md)                                            si
  [OBJ](Arch_OBJ/es.md)                 Formato de intercambio de mallas                                                                                                                    si         si         [Arquitectura](Arch_Workbench/es.md) / [Malla](Mesh_Workbench/es.md)    no
  STL                                           Formato de intercambio de malla mayormente utilizado para impresoras 3D                                                                             si         si         [Malla](Mesh_Workbench/es.md)                                                   no
  BMS                                           Formato de intercambio de malla binaria                                                                                                             si         si         [Malla](Mesh_Workbench/es.md)                                                   no
  AST                                           Formato de intercambio de malla                                                                                                                     yes        yes        [Malla](Mesh_Workbench/es.md)                                                   no
  OFF                                           Formato de intercambio de malla                                                                                                                     si         si         [Malla](Mesh_Workbench/es.md)                                                   no
  PLY                                           Mesh exchange format / Points cloud                                                                                                                 yes        yes        [Mesh](Mesh_Workbench.md) / [Points](Points_Workbench.md)               no
  INP                                           Abaqus format                                                                                                                                       yes        yes        [FEM](FEM_Workbench.md)                                                         no
  POLY                                          Tetgen format                                                                                                                                       no         yes        [FEM](FEM_Workbench.md)                                                         no
  UNV                                           FEM exchange format                                                                                                                                 yes        yes        [FEM](FEM_Workbench.md)                                                         no
  MED                                           FEM exchange format                                                                                                                                 yes        yes        [FEM](FEM_Workbench.md)                                                         no
  DAT                                           FEM exchange format (FEM) or 2D airfoil profile (Draft)                                                                                             yes        yes        [FEM](FEM_Workbench.md) / [Draft](Draft_Workbench.md)                   no
  BDF                                           FEM exchange format                                                                                                                                 yes        no         [FEM](FEM_Workbench.md)                                                         no
  FRD                                           CalculiX result format                                                                                                                              yes        no         [FEM](FEM_Workbench.md)                                                         no
  NC                                            G-Code file format                                                                                                                                  yes        yes        [Path](Path_Workbench.md)                                                       no
  GC                                            G-Code file format                                                                                                                                  yes        yes        [Path](Path_Workbench.md)                                                       no
  NCC                                           G-Code file format                                                                                                                                  yes        yes        [Path](Path_Workbench.md)                                                       no
  NGC                                           G-Code file format                                                                                                                                  yes        yes        [Path](Path_Workbench.md)                                                       no
  CNC                                           G-Code file format                                                                                                                                  yes        yes        [Path](Path_Workbench.md)                                                       no
  TAP                                           G-Code file format                                                                                                                                  yes        yes        [Path](Path_Workbench.md)                                                       no
  GCODE                                         G-Code file format                                                                                                                                  yes        yes        [Path](Path_Workbench.md)                                                       no
  EMN                                           IDF file format                                                                                                                                     yes        no         Idf                                                                                     no
  IV                                            OpenInventor file format                                                                                                                            yes        yes        Built-in                                                                                no
  VRML                                          Web 3D format                                                                                                                                       yes        yes        Built-in                                                                                no
  WebGL (HTML)                                  Web 3D format                                                                                                                                       no         yes        [Arch](Arch_Workbench.md)                                                       no
  SCAD                                          OpenSCAD file format                                                                                                                                yes        yes        [OpenSCAD](OpenSCAD_Workbench.md)                                               no
  CSG                                           OpenSCAD Constructive Solid Geometry                                                                                                                yes        yes        [OpenSCAD](OpenSCAD_Workbench.md)                                               no
  ASC                                           Points cloud format                                                                                                                                 yes        no         [Points](Points_Workbench.md)                                                   no
  POV                                           Povray format                                                                                                                                       no         yes        [Raytracing](Raytracing_Workbench.md)                                           no
  CSV                                           Comma-separated values spreadsheet                                                                                                                  yes        yes        [Spreadsheet](Spreadsheet_Workbench.md)                                         no
  PDF                                           Adobe portable document format                                                                                                                      no         yes        Built-in                                                                                no


</div>







_

---
[documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > [Import](Import_Workbench.md) > Import Export/es
