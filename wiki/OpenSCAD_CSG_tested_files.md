# OpenSCAD CSG tested files
 

## This is a list of OpenSCAD files that can not be opened in FreeCAD 

  ------------------- ------------------------------------------ -------------------------------------------------------- ----------------------------------------------------------- ------------------------------------------
  **Description**     **Source**                                 **Reason**                                               **Interactive repair known**                                **Fixed version available**
  Driver Bit Handle   <http://www.thingiverse.com/thing:34852>   execute function does not return, Coincident geometry?   no                                                          no
  Ashtray             <http://www.thingiverse.com/thing:33191>   booleans of coincident geometry fail                     multi-fusing cylinders 001-004 at once solves the problem   no
  Batman Symbol       <http://www.thingiverse.com/thing:12381>   booleans of coincident geometry fail                     do booleans in 2D space, before applying linear extrusion   <http://www.thingiverse.com/thing:18780>
  venturi pump        <http://www.thingiverse.com/thing:29100>   uses screw lib <http://www.thingiverse.com/thing:8793>   no                                                          no
  Screw Library       <http://www.thingiverse.com/thing:8793>    returns meshes with duplicate vertices                   no                                                          no
  ------------------- ------------------------------------------ -------------------------------------------------------- ----------------------------------------------------------- ------------------------------------------

## This is a list of OpenSCAD files that can be opened in FreeCAD without any problem 

  ------------- ------------------------------------------
  Description   Source
  Tetrapode     <http://www.thingiverse.com/thing:33104>
  ------------- ------------------------------------------

## Related

-   [OpenSCAD Workbench](OpenSCAD_Workbench.md)
-   [OpenSCAD\_CSG](OpenSCAD_CSG.md)
-   [Import Export](Import_Export.md)

 {{OpenSCAD Tools navi}}

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:File\_Formats](Category:File_Formats.md)
