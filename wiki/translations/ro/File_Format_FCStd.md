# File Format FCStd/ro
{{TOCright}}

## Overview


<div class="mw-translate-fuzzy">

**FreeCAD Standard file format** (.FCStd) este formatul principal de fișier al FreeCAD . Un proiect FreeCAD, este compus de fapt dintr-o serie de fișiere normale tip text care conțin întodeauna un fișier document .xml, GuiDocument.xml, Document.xml și eventual mai multe fișiere de date PartShape3.brp Points3 . . ., plus o vineta în format .PNG totul fiind arhivat într-un fișier .zip la care se înlocuiește extensia .FCStd.t .


</div>

## Interiorul fișierelor .FCStd 


<div class="mw-translate-fuzzy">

FCStd este un fișier standard tip fișier zip, conținând fișiere[one or more](#Contents.md) îmtr-o [Structure](#structure.md) specifică. Ca atare, este posibilă dezarhivarea unui fișier FCStd utilizând un instrument de decompresie zip obișnuit. FreeCAD conține un \"Project Utility\" pentru rearhivarea fișierelor FCStd, utilizara sa este descrisă mai jos în [#Change the source of the file .FCStd](#Change_the_source_of_the_file_.FCStd.md) .


</div>


<div class="mw-translate-fuzzy">

### Conținuturi

#### Document.xml

This is the main xml file describing all the objects inside a FreeCAD document, that is, only the geometric and parametric definition of the objects, not their visual representation. If FreeCAD is ran in console mode (without the GUI), only this xml document will be used.=


</div>

This is the main **.xml** file describing all the objects inside a FreeCAD document, that is, only the geometric and parametric definition of the objects, not their visual representation. If FreeCAD is ran in console mode (without the GUI), only this **Document.xml** will be used.


<div class="mw-translate-fuzzy">

##### Exemplu de Document.xml 


</div>


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


<div class="mw-translate-fuzzy">

#### GuiDocument.xml

This is the GUI counterpart of the Document.xml file. For each object described in the Document.xml, there is one corresponding object in GuiDocument.xml, describing the visual representation of that object (color, linewidth, etc).


</div>

This is the GUI counterpart of the **Document.xml** file. For each object described in the **Document.xml**, there is one corresponding object in **GuiDocument.xml**, describing the visual representation of that object (color, linewidth, etc).


<div class="mw-translate-fuzzy">

#### Thumbnails/thumbnail.png

This is a 128x128 pixels thumbnail image of the document, which is a screenshot of the 3D view at save time. Thumbnails are generated only if the corresponding option is enabled in the FreeCAD preferences.


</div>

This is a 128x128 pixels thumbnail image of the document, which is a screenshot of the 3D view at save time. Thumbnails are generated only if the corresponding option is enabled in the FreeCAD preferences.


<div class="mw-translate-fuzzy">

#### \*.brep

Acestea sunt forme .brep shapes a tuturor obeicteleor care au o Part shape în Document.xml. Fiecare obiect, chiar dacă este parametric, are forma sa stocată ca fișier individual .brep , astfel încât acesta poate fi accesat de către componente fără a fi nevoie să recalculați forma.


</div>

These are the [B-rep](wikipedia_Boundary_representation.md) shapes of all objects that have a Part shape in the **Document.xml**. Each object, even if it is parametric, has its shape stored as an individual **.brep** file, so it can be accessed by components without the need to recalculate the shape.


<div class="mw-translate-fuzzy">

#### Șabloane/\*.svg

In the Templates folder are stored the template svg files used in [Drawing](Drawing_Workbench.md) pages.


</div>

These are the template svg files used in [TechDraw](TechDraw_Workbench.md) pages.


<div class="mw-translate-fuzzy">

### Structură

Structure of a typical FCStd file   *


</div>

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


<div class="mw-translate-fuzzy">

## Schimbarea sursei fișierului .FCStd 


**'''ATTENTION ALWAYS WORK ON A COPY OF YOUR PROJECT !'''**


</div>


<div class="mw-translate-fuzzy">

Este posibilă schimbara sursei fișierului .FCStd Dar procedura nu este lipsită de riscuri din acest motiv trebuie să lucrăm pe o **copy**.


</div>

## Altele


<div class="mw-translate-fuzzy">

Here, a file Converter utility [ImageConv](ImageConv.md).


</div>


 

[Category   *Developer](Category_Developer.md) [Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *File_Formats](Category_File_Formats.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer](Category_Developer.md) > [Developer Documentation](Category_Developer Documentation.md) > [File_Formats](Category_File_Formats.md) > File Format FCStd/ro
