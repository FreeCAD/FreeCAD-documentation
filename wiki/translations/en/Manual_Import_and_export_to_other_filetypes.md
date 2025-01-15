# Manual:Import and export to other filetypes/en
{{Manual:TOC}}

FreeCAD can import and export to many file types. Here is a list of the most important ones with a short description of the available features:

  Format   Import   Export   Notes
     
  STEP     Yes      Yes      This is the most faithful import/export format available since it supports solid geometry and NURBS. Use it whenever it is possible.
  IGES     Yes      Yes      An older solid format, also very well supported. Some older applications don\'t support STEP but have IGES.
  BREP     Yes      Yes      The native format of [OpenCasCade](https://en.wikipedia.org/wiki/Open_Cascade_Technology), FreeCAD\'s geometry kernel.
  DXF      Yes      Yes      An open format maintained by Autodesk. Since the 3D data inside a DXF file is encoded in a proprietary format, FreeCAD can only import/export 2D data to/from this format.
  DWG      Yes      Yes      The proprietary version of DXF. Requires the installation of the [Teigha File Converter](https://www.opendesign.com/guestfiles) utility. This format suffers from the same limitations as DXF.
  OBJ      Yes      Yes      A mesh-based format. Can only contain triangulated meshes. All solid and NURBS-based objects of FreeCAD will be converted to mesh on export. An alternative exporter is provided by the Arch workbench, more suited to the export of architectural models.
  DAE      Yes      Yes      The main import/export format of Sketchup. Can only contain triangulated meshes. All solid and NURBS-based objects of FreeCAD will be converted to mesh on export.
  STL      Yes      Yes      A mesh-based format, commonly used for 3D printing. Can only contain triangulated meshes. All solid and NURBS-based objects of FreeCAD will be converted to mesh on export.
  PLY      Yes      Yes      An older mesh-based format. Can only contain triangulated meshes. All solid and NURBS-based objects of FreeCAD will be converted to mesh on export.
  IFC      Yes      Yes      [Industry Foundation Classes](https://en.wikipedia.org/wiki/Industry_Foundation_Classes). Requires the installation of [IfcOpenShell-python](http://ifcopenshell.org/python). The IFC format and its compatibility with other applications is a complex affair, use with care.
  SVG      Yes      Yes      An excellent, widespread 2D graphics format
  VRML     Yes      Yes      A rather old mesh-based web format.
  GCODE    Yes      Yes      FreeCAD can already import and export to/from several flavors of GCode, but only a small number of machines are supported at the moment.
  CSG      Yes      No       OpenSCAD\'s [CSG](https://en.wikipedia.org/wiki/Constructive_solid_geometry) (Constructive Solid Geometry) format.

Some of these file formats have options. These can be configured from menu **Edit → Preferences → Import/export:**

![](images/FreeCAD_022_ImportExport.png )

**Read more**

-   [All file formats supported by FreeCAD](Import_Export.md)
-   [Working with DXF files in FreeCAD](Draft_DXF.md):
-   [Working with SVG files in FreeCAD](Draft_SVG.md)
-   [Importing and exporting to IFC](Arch_IFC.md)
-   [OpenCasCade](http://www.opencascade.com)
-   [Teigha File Converter](https://www.opendesign.com/guestfiles)
-   [IFC Specifications Database](https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/)
-   [IfcOpenShell](http://ifcopenshell.org/)



---
⏵ [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser%20Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Import and export to other filetypes/en
