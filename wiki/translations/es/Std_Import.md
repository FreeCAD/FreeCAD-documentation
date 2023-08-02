# Std Import/es
---
- GuiCommand:   Name: Std_Import   Name/es: Std_Import   Workbenches: Todos   MenuLocation: Archivo -> Importar   Shortcut: CTRL+I   SeeAlso: Std_Open/es, Std_Save/es...---


</div>

## Description


<div class="mw-translate-fuzzy">

Añade en el documento actual el contenido de un fichero creado con otra aplicación. Estan soportados varios formatos de archivo: **[.IGES](http://en.wikipedia.org/wiki/IGES), [.STEP](http://es.wikipedia.org/wiki/ISO_10303), [.BREP](http://en.wikipedia.org/wiki/Boundary_representation), [.STL](http://en.wikipedia.org/wiki/STL_%28file_format%29), [.OBJ](http://en.wikipedia.org/wiki/Wavefront_.obj_file), [.PLY](http://en.wikipedia.org/wiki/PLY_%28file_format%29)**, etc.


</div>


<small>(v0.21)</small> 

: If an image format is selected the command will create an [Image Plane](#Image_Plane.md).

## Usage


<div class="mw-translate-fuzzy">

Cuando se carga, el fichero es **incorporado** al proyecto actual (que debe estar abierto). Si lo que deseas es cargar un nuevo archivo en una nueva ventana, usa el comando **[Std_Open](Std_Open/es.md)**.


</div>

## Options

-   Press **Esc** or the **Cancel** button to abort the command.

## Notes

-   To convert an imported [mesh object](Mesh_Workbench.md) into a solid see the [Import from STL or OBJ](Import_from_STL_or_OBJ.md) tutorial.
-   To import into a new document you can use the [Std Open](Std_Open.md) command.
-   Some workbenches have additional import commands. See: [Import Export](Import_Export.md).

## Preferences

-   See: [Import Export Preferences](Import_Export_Preferences.md).
-   The last used file location is stored: **Tools → Edit parameters... → BaseApp → Preferences → General → FileOpenSavePath**.
-   The last used import filter is stored: **Tools → Edit parameters... → BaseApp → Preferences → General → FileImportFilter**.

## Image Plane 

An Image Plane is a planar representation of an image in the [3D view](3D_view.md). It can for example be used when creating a model based on photographs of an existing object.

By default an Image Plane is placed on the global XY plane. The initial size of an Image Plane is calculated using a 96px/inch resolution.

### Edit

1.  To edit an Image Plane do one of the following:
    -   Double-click the Image Plane in the [Tree view](Tree_view.md).
    -   Right-click the Image Plane in the Tree view and select **<img src="images/Image-scaling.svg" width=16px> Change image...** from the context menu.

2.  If the Image Plane is not plane-parallel to the XY, XZ or YZ plane of the global coordinate system, it is realigned to be plane-parallel to the XY plane.

3.  The **Image plane settings** task panel opens.

4.  Optionally select the **XY-Plane**, **XZ-Plane** or **YZ-Plane** of the global coordinate system.

5.  Check **Reverse direction** to rotate the Image Plane 180°. The rotation axis depends on the selected plane. For the XY plane it is the global X axis. For the XZ and YZ plane it is the global Z axis.

6.  The **Offset**, **X distance** and **Y distance** are relative to the coordinate system of the Image Plane. A small negative offset can be useful when tracing the image with a [sketch](Sketcher_Workbench.md) or [Draft](Draft_Workbench.md) geometry.

7.  Optionally change the **Transparency**.

8.  
    **Image size**options:

    -   Scale by numerical input:
        1.  Optionally uncheck **Keep aspect ratio** for unequal scaling.
        2.  Enter a **Width** and/or **Height**.
    -   Scale by picking points:
        1.  Press the **Calibrate** button.
        2.  Pick two points inside the image.
        3.  A dimension line is displayed.
        4.  Enter the desired dimension.
        5.  Press **Enter** or the **Apply** button.

9.  Press the **OK** button to confirm the changes and close the task panel.

### Properties

See also: [Property editor](Property_editor.md).

An Image Plane object is derived from an [App GeoFeature](App_GeoFeature.md) object and inherits all its properties. It also has the following additional properties:

#### Data


{{TitleProperty|Image Plane}}

-    **Image File|FileIncluded**: The image file used for the Image Plane. This file is stored in the **.FCStd** file.

-    **XSize|Length**: The width of the Image Plane.

-    **YSize|Length**: The height of the Image Plane.

#### View


{{TitleProperty|Object Style}}

-    **Lighting|Enumeration**: How the Image Plane is illuminated in the [3D view](3D_view.md). Can be {{value|Two side}} or {{value|One side}}.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Std Import/es
