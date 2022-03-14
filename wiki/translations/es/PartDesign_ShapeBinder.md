---
- GuiCommand:/es
   Name:PartDesign ShapeBinder
   Name/es:DiseñoPiezas FormaAglomerante
   MenuLocation:DiseñoPiezas → Crear una forma aglomerante
   Workbenches:[DiseñoPiezas](PartDesign_Workbench/es.md)
   Version:0.17
   SeeAlso:[DiseñoPiezas SubFormaAglomerante](PartDesign_SubShapeBinder/es.md), [DiseñoPiezas Clon](PartDesign_Clone/es.md)
---

# PartDesign ShapeBinder/es

## Descripción


<div class="mw-translate-fuzzy">

Crea un dato *aglomerante forma* a partir de un Cuerpo seleccionado dentro del Cuerpo activo. Un aglomerante forma es un objeto de referencia que se une a los bordes o caras de otro Cuerpo. También puede ser usado para unir un boceto de un cuerpo a otro cuerpo. El objeto aglomerante forma se muestra en amarillo translúcido en la [Vista 3D](3D_view/es.md).


</div>

Examples of use would be to build a box with fitting cover in two different bodies or to make holes that are aligned between different bodies.

<img alt="" src=images/Shapebinder_tree.png ) ![](images/Shapebinder_flow.png  style="width:600px;"> 
*Two shapes from Body.Pad004 are selected and their datum objects are now available in Body001.Sketch005 as external geometry through Body001.ShapeBinder.*

## Utilización

1.  [Activate the body](PartDesign_Body#Active_status.md), which is to receive the shape binder object.
2.  Press the **<img src="images/PartDesign_ShapeBinder.svg" width=16px> [Create a shape binder](PartDesign_ShapeBinder.md)** button.
3.  Press either the **Object** button or the **Add geometry** button.
4.  In the [3D view](3D_view.md), select the object or geometry to copy. *Object* picks the whole shape; *Add geometry* picks the highlighted geometry element (e.g., vertex, edge, or face).
5.  To remove geometry, press the **Remove geometry** button and then select the geometry in the [3D view](3D_view.md).
6.  Alternatively, geometry elements can be selected in the [3D view](3D_view.md) before launching the tool.
7.  Press **OK**.

To cancel an action that has been started with a button, press the same button again.

**Example**

:   The example uses the ShapeBinder feature to make a hole (with or without threads) through more than one body. Normally the Hole function of the Part Design workbench is limited to a single body. The example uses two cubes facing each other but misaligned in an arbitrary way. The holes are created with sketches containing a circle for every hole (the diameter is ignored by the hole function). When you copy the sketch to the other cube it will be at the same position in the local cube coordinate system. In the image this is shown by the white circle on the back cube. This is not what we want, because the hole at that position would not be aligned to the hole in the front cube.





:   

    :   ![](images/ShapeBinderThroughHole.png )
    :   *Example setup for showing HowTo make holes through different bodies. The white circle shows that copying sketches is not enough*

Here is how you use the ShapeBinder Feature to achieve it:

1.  Prepare a scene as per the above image. If you use the cubes from the [Part workbench](Part_Workbench.md), remember that you must put them into a \"body\" container. Each one in a single body container. Otherwise the [PartDesign](PartDesign_Workbench.md) functions would not work. If you build them from sketches the system should create body containers by default.
2.  Select the Properties Dialog Tab then Data to move the second cube to touch the first cube with a side displacement.
3.  Select the PartDesign workbench
4.  Create a sketch on the front face of the first cube and place a circle anywhere and close the sketch
5.  Select the sketch in the tree and press [Hole](PartDesign_Hole.md) function button. Before make sure the first body is the [active body](PartDesign_Body#Active_status.md) (double-click).
6.  Select a hole of appropriate size. The image above had also counterbore selected. Close the [Hole](PartDesign_Hole.md) function.

    :   Now the image should look as above. When you hide the first cube (select and press space) you can see that the hole does not reach the second cube. It will not, even when you select \"Through All\", or when you enter a really large distance in the [Hole](PartDesign_Hole.md) dialog. The hole dialog is always limited to a single body.
    :   Here is where our ShapeBinder comes in.
7.  First select the back cube. This is the target where the ShapeBinder will be added. It must be [actived](PartDesign_Body#Active_status.md) before, so be sure it has been double-clicked.
8.  In the tree select the sketch we used for the hole. It\'s important to not activate the first body.
9.  Select the shapeBinder function.

    :   A dialog should open. In the line \"Object\" the name of our sketch should be visible. If you had selected the function without selecting the sketch, you could press \"Object\" and then select the sketch from the list. It\'s recommended to select it first in order to get the right one, especially if you have many sketches with automatically generated names Sketch001,.. The \"Add Geometry\" is not useful for us, because we want to select the whole sketch. \"AddGeometry\" is used if only parts should be selected.
10. Press **OK** to close the dialog and check that a new item has been added to the tree of the second cube.

    :   When you toggle the visibility of the ShapeBinder it is shown yellow in the [3D view](3D_view.md). However it\'s on the wrong position, just as the white circle in the image above. That is because of the default setting for the Trace parameter.
11. In the PropertyView of the ShapeBinder in the Data tab set the **Trace Support** parameter to true. The default was false.

    :   With **Trace Support** true, the ShapeBinder in not affected by local transformations of the target body, e.g. our translations. The shape remains exactly where the original front object shape has been. Try moving the front object around and you can see that the ShapeBinder always follows to the new position.
    :   Unfortunately we can not select the ShapeBinder for a [Hole](PartDesign_Hole.md). Therefore we create a local sketch and use that for our hole in the second cube.
12. Select the front face of the back cube and create a new sketch (click **OK** for the suggestion in the dialog)
13. Make all geometry invisible and the ShapeBinder visible. Now you can use the external geometry function and select the circle in the shape binder. We need the center point of that circle.
14. Create a new circle and put it at the center point of the ShapeBinders circle. The radius is not important. The [Hole](PartDesign_Hole.md) function only uses the center points of the circles (note: single points are ignored by the Hole function, we must use circles)
15. Close the sketch and click [Hole](PartDesign_Hole.md). Set the dialog to the same values as the initial hole and press OK.

**Done.**

:   Now you have two linked holes in two different bodies. If you change the geometry or the positions of the holes, both holes will adapt. Only when you add a new hole, you need to update the sketch in the second cube for the second hole.





:   Notes:
:   that there is another way to create a ShapeBinder: with the back cube activated click the front face of the front cube and create a new sketch. A dialog will pop up where you select \"Dependent sketch\". This will actually create a shape binder. You can see the **Trace Support** parameter in the property window. It\'s a few clicks less than our procedure.
:   Also note that working with ShapeBinder with Sketches is only a subset of its capabilities. It\'s also possible to use parts of 3D geometry as seen in the example above.

## Opciones

Double-click the ShapeBinder label in the [tree view](Tree_view.md) or right-click and select **Edit shape binder** in the contextual menu to edit its parameters.

## Propiedades

-    **Label**: name given to the object, this name can be changed at convenience.

-    **Trace Support**: Default is false. When true, the shape binder does observe relative placements of the parts and bodies (by manipulating values of its hidden **Placement** property). See the example above for how this is used and works.

## Limitaciones

-   Multiple selection is not supported. The Add geometry and Remove geometry buttons need to be pressed for each single selection.
    -   There is a workaround for multiple selection: If you select all the elements you want to have *before* creating the shape binder, they appear in the initial list.
-   A shape binder cannot serve as base feature.
-   Selected geometry on a body must be contiguous.
-   If the body to be copied is selected first before launching the command, or if the **Object** button is used, it is no longer possible to only select specific geometry elements.
-   The relative placement of the target body and the referenced body is not taken into account. The shape binder will adopt the same internal coordinates as the referenced body.
    -   Use the **Trace Support** property to change this behavior.


<div class="mw-translate-fuzzy">





</div>


{{PartDesign_Tools_ navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign ShapeBinder/es
