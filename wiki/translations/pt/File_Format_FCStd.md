# File Format FCStd/pt
{{TOCright}}

## Overview

The **FreeCAD Standard file format** (**.FCStd**) is FreeCAD\'s main file format. It is a compound format, supports compression and embedding of different kinds of data.

## Internals of .FCStd files 

FCStd is a [ standard zip file containing one or more files](#Contents.md) in a [specific structure](#structure.md). As such, it is possible to unpack a **.FCStd** file using a regular zip decompression tool, but care needs to be taken while packing the contents of a **.FCStd** file. FreeCAD contains a \"Project Utility\" to re-pack **.FCStd** files, it\'s use is described in [Change the source of the file .FCStd](#Change_the_source_of_the_file_.FCStd.md) below.

### Document.xml

This is the main **.xml** file describing all the objects inside a FreeCAD document, that is, only the geometric and parametric definition of the objects, not their visual representation. If FreeCAD is ran in console mode (without the GUI), only this **Document.xml** will be used.

#### Example Document.xml 


{{Code|lang=xml|code=
 <?xml version='1.0' encoding='utf-8'?>
 
 <Document SchemaVersion="4">
    <Properties Count="9">
       <Property name="Comment" type="App   *   *PropertyString">
          <String value=""/>
       </Property>
       <Property name="Company" type="App   *   *PropertyString">
          <String value=""/>
       </Property>
       <Property name="CreatedBy" type="App   *   *PropertyString">
          <String value=""/>
       </Property>
       <Property name="CreationDate" type="App   *   *PropertyString">
          <String value="Fri Jan 29 15   *14   *38 2010 "/>
       </Property>
       <Property name="FileName" type="App   *   *PropertyString">
          <String value="/tmp/test.FCStd"/>
       </Property>
       <Property name="Id" type="App   *   *PropertyString">
          <String value="201b746f-a1ed-4297-bf3d-65d5ec11abe0"/>
       </Property>
       <Property name="Label" type="App   *   *PropertyString">
          <String value="names"/>
       </Property>
       <Property name="LastModifiedBy" type="App   *   *PropertyString">
          <String value=""/>
       </Property>
       <Property name="LastModifiedDate" type="App   *   *PropertyString">
          <String value="Fri Jan 29 15   *15   *21 2010 "/>
       </Property>
    </Properties>
    <Objects Count="2">
       <Object type="Mesh   *   *Cube" name="Cube" />
       <Object type="Part   *   *Box" name="Box" />
    </Objects>
    <ObjectData Count="2">
       <Object name="Cube">
          <Properties Count="7">
             <Property name="Height" type="App   *   *PropertyFloatConstraint">
                <Float value="10"/>
             </Property>
             <Property name="Label" type="App   *   *PropertyString">
                <String value="Cube"/>
             </Property>
             <Property name="Length" type="App   *   *PropertyFloatConstraint">
                <Float value="10"/>
             </Property>
             <Property name="Mesh" type="Mesh   *   *PropertyMeshKernel">
                <Mesh file="MeshKernel.bms"/>
             </Property>
             <Property name="Placement" type="App   *   *PropertyPlacement">
                <PropertyPlacement Px="0" Py="0" Pz="0" Q0="0" Q1="0" Q2="0" Q3="1"/>
             </Property>
             <Property name="Pos" type="App   *   *PropertyPlacementLink">
                <Link value=""/>
             </Property>
             <Property name="Width" type="App   *   *PropertyFloatConstraint">
                <Float value="10"/>
             </Property>
          </Properties>
       </Object>
       <Object name="Box">
          <Properties Count="7">
             <Property name="Height" type="App   *   *PropertyLength">
                <Float value="10"/>
             </Property>
             <Property name="Label" type="App   *   *PropertyString">
                <String value="Box2"/>
             </Property>
             <Property name="Length" type="App   *   *PropertyLength">
                <Float value="10"/>
             </Property>
             <Property name="Placement" type="App   *   *PropertyPlacement">
                <PropertyPlacement Px="0" Py="0" Pz="0" Q0="0" Q1="0" Q2="0" Q3="1"/>
             </Property>
             <Property name="Pos" type="App   *   *PropertyPlacementLink">
                <Link value=""/>
             </Property>
             <Property name="Shape" type="Part   *   *PropertyPartShape">
                <Part file="PartShape.brp2"/>
             </Property>
             <Property name="Width" type="App   *   *PropertyLength">
                <Float value="10"/>
             </Property>
          </Properties>
       </Object>
    </ObjectData>
 </Document>
}}

### GuiDocument.xml

This is the GUI counterpart of the **Document.xml** file. For each object described in the **Document.xml**, there is one corresponding object in **GuiDocument.xml**, describing the visual representation of that object (color, linewidth, etc).

### Thumbnails/thumbnail.png

This is a 128x128 pixels thumbnail image of the document, which is a screenshot of the 3D view at save time. Thumbnails are generated only if the corresponding option is enabled in the FreeCAD preferences.

### \*.brep

These are the [B-rep](wikipedia_Boundary_representation.md) shapes of all objects that have a Part shape in the **Document.xml**. Each object, even if it is parametric, has its shape stored as an individual **.brep** file, so it can be accessed by components without the need to recalculate the shape.

### \*.svg

These are the template svg files used in [TechDraw](TechDraw_Workbench.md) pages.

### Typical structure 

Structure of a typical **.FCStd** file. The extension can be changed to **.zip** to explore it like a normal directory. The **Document.xml** and **GuiDocument.xml** are at the root of the archive, together with any number of **.brp** (BREP) files. One subdirectory may hold the thumbnail, and another the SVG templates used by [TechDraw](TechDraw_Workbench.md).

    File.FCStd (File.zip)
      |
      |--thumbnails/
      |  |
      |     *--Thumbnail.png
      |
         *--Document.xml
         *--GuiDocument.xml
         *--Shape1.brp
         *--Shape2.brp
         *--MyPage.svg
         *--etc.

## Embedding other files 

In order to embed other file types inside a FCStd file, you must first create a [scripted object](Scripted_objects.md) from the [Python console](Python_console.md), and give it an `App   *   *PropertyFileIncluded` property.

Then in the [property editor](Property_editor.md) you can go to the added property and choose a file in the computer. Once the FCStd file is saved, the file assigned to the **PropertyFileIncluded** property will be packed inside the `.FCStd`. When the document is restored, the same file will be restored with the **PropertyFileIncluded** property.


```python
custom_obj = App.ActiveDocument.addObject("App   *   *FeaturePython", "CustomObject")
custom_obj.addProperty("App   *   *PropertyFileIncluded", "AttachedFile")
```

See the forum thread, [PDF inside the project](https   *//forum.freecadweb.org/viewtopic.php?t=38201).

## Change the source of the file .FCStd 

-   See [Std ProjectUtil](Std_ProjectUtil.md).

## Other

-   A file Converter utility [ImageConv](ImageConv.md).


 

[Category   *Developer](Category_Developer.md) [Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *File\_Formats](Category_File_Formats.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer](Category_Developer.md) > [Developer Documentation](Category_Developer Documentation.md) > [File_Formats](Category_File_Formats.md) > File Format FCStd/pt
