# File Format FCStd/es
{{TOCright}}

## Resumen

El **FreeCAD Standard formato de archivo** (**.FCStd**) es el principal formato de archivo de FreeCAD. Es un formato compuesto, soporta la compresión y la incrustación de diferentes tipos de datos.

## Internos de los archivos .FCStd 


<div class="mw-translate-fuzzy">

FCStd es un [ archivo zip estándar que contiene uno o más archivos](#Contenido.md) en una [específica](#estructura.md). Como tal, es posible desempaquetar un archivo **.FCStd** utilizando una herramienta de descompresión zip normal, pero hay que tener cuidado al empaquetar el contenido de un archivo **.FCStd**. FreeCAD contiene una \"Utilidad de Proyecto\" para re-empaquetar archivos **.FCStd**, su uso se describe en [Cambiar la fuente del archivo .FCStd](#Cambiar_la_fuente_del_archivo_.FCStd.md) más abajo.


</div>

### Document.xml

Este es el archivo principal **.xml** que describe todos los objetos dentro de un documento de FreeCAD, es decir, sólo la definición geométrica y paramétrica de los objetos, no su representación visual. Si FreeCAD se ejecuta en modo consola (sin la GUI), sólo se utilizará este **Document.xml**.

#### Ejemplo Document.xml 


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

Es la contrapartida de la interfaz gráfica de usuario del archivo **Document.xml**. Para cada objeto descrito en **Document.xml**, hay un objeto correspondiente en **GuiDocument.xml**, que describe la representación visual de ese objeto (color, ancho de línea, etc).

### Miniaturas/thumbnail.png

Esta es una imagen en miniatura de 128x128 píxeles del documento, que es una captura de pantalla de la vista 3D en el momento de guardar. Las miniaturas se generan sólo si la opción correspondiente está activada en las preferencias de FreeCAD.

### \*.brep

Estas son las formas [B-rep](wikipedia_Boundary_representation.md) de todos los objetos que tienen una forma de Parte en el **Document.xml**. Cada objeto, incluso si es paramétrico, tiene su forma almacenada como un archivo individual **.brep**, por lo que puede ser accedido por los componentes sin necesidad de recalcular la forma.

### \*.svg

Estos son los archivos svg de plantilla utilizados en las páginas de [TechDraw](TechDraw_Workbench/es.md).

### Estructura típica 

Estructura de un archivo típico **.FCStd**. La extensión puede cambiarse a **.zip** para explorarlo como un directorio normal. Los archivos **Document.xml** y **GuiDocument.xml** están en la raíz del archivo, junto con cualquier número de archivos **.brp** (BREP). Un subdirectorio puede contener la miniatura, y otro las plantillas SVG utilizadas por [TechDraw](TechDraw_Workbench/es.md).

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

## Incrustar otros archivos 

Para incrustar otros tipos de archivos dentro de un archivo FCStd, primero hay que crear un [objeto scriptado](Scripted_objects/es.md) desde la [consola de Python](Python_console/es.md), y darle una propiedad `App   *   *PropertyFileIncluded`.

A continuación, en el [Editor de propiedades](Property_editor/es.md) puede ir a la propiedad añadida y elegir un archivo en el ordenador. Una vez guardado el archivo FCStd, el archivo asignado a la propiedad **PropertyFileIncluded** se empaquetará dentro del `.FCStd`. Al restaurar el documento, se restaurará el mismo archivo con la propiedad **PropertyFileIncluded**.


```python
custom_obj = App.ActiveDocument.addObject("App   *   *FeaturePython", "CustomObject")
custom_obj.addProperty("App   *   *PropertyFileIncluded", "AttachedFile")
```

Ver el hilo del foro, [PDF dentro del proyecto](https   *//forum.freecadweb.org/viewtopic.php?t=38201).

## Cambiar la fuente del archivo .FCStd 

-   Ver [Std ProjectUtil](Std_ProjectUtil/es.md).

## Otros

-   Una utilidad de conversión de archivos [ImageConv](ImageConv/es.md).


 

[Category   *Developer](Category_Developer.md) [Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *File_Formats](Category_File_Formats.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer](Category_Developer.md) > [Developer Documentation](Category_Developer Documentation.md) > [File_Formats](Category_File_Formats.md) > File Format FCStd/es
