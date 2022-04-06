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

A ShapeBinder will track the relative placement of the referenced geometry, which is useful in the context of creating [assemblies](Assembly.md), if its **Trace Support** property is set to {{True}}. See the [Example](#Example.md) below to understand how this works.

The referenced geometry can either be a single object (for example a [Part Box](Part_Box.md), a [PartDesign Body](PartDesign_Body.md), or a [sketch](PartDesign_NewSketch.md) or [Feature](PartDesign_Feature.md) inside a Body), or one or more subelements (faces, edges or vertices) belonging to the same parent object. Which geometry should be selected depends on the intended purpose of the ShapeBinder. For a Boolean operation you would need to select a solid. For a Pad operation a face or a sketch can be used. And for the external geometry in a sketch, or to attach a sketch, any combination of subelements may be appropriate. The referenced geometry can also belong to the Body the ShapeBinder is nested in.

<img alt="" src=images/Shapebinder_flow.png  style="width:600px;"> 
*From two selected faces a ShapeBinder is created in a still empty Body. Geometry from the Shapebinder can then be used as external geometry in a sketch in that Body.*

## Utilización

1.  [Activate the Body](PartDesign_Body#Active_status.md) the ShapeBinder should be nested in.
2.  Optionally select a single object, or one or more subelements belonging to the same parent object. Subelements can only be selected in the [3D view](3D_view.md).
3.  There are several ways to invoke the tool:
    -   Press the **<img src="images/PartDesign_ShapeBinder.svg" width=16px> [PartDesign ShapeBinder](PartDesign_ShapeBinder.md)** button.
    -   Select the **Part Design → <img src="images/PartDesign_ShapeBinder.svg" width=16px> Create a shape binder** option from the menu.
4.  The **Datum shape parameters** task panel opens.
5.  Optionally select an object, this is not required if you want the select subelements:
    1.  Press the **Object** button.
    2.  Select an object in the [Tree view](Tree_view.md) or the [3D view](3D_view.md).
    3.  Any previously selected subelements will be removed.
    4.  If a Body is selected here, selecting subelements will be impossible as these belong to a different object, namely the [Tip Feature](PartDesign_Body#Tip.md) of the Body.
6.  Optionally select subelements:
    1.  Press the **Add geometry** button.
    2.  Select a subelement in the [3D view](3D_view.md).
    3.  The **Add geometry** button has to be pressed for every subelement you want to add.
    4.  Only subelements belonging to the same parent object can be selected. If required use the **Object** button to select a different parent object.
7.  Optionally remove subelements:
    1.  Press the **Remove geometry** button.
    2.  Select a subelement in the [3D view](3D_view.md).
    3.  The **Remove geometry** button has to be pressed for every subelement you want to remove.
8.  Press the **OK** button.

## Opciones

To edit a ShapeBinder double-click it in the [Tree view](Tree_view.md), or right-click it and select **Edit shape binder** from the [Tree view](Tree_view.md) context menu.

## Notes

-   A ShapeBinder can be dragged out of the Body it is nested in, and dropped onto the <img alt="" src=images/Document.svg  style="width:16px;"> document node in the [Tree view](Tree_view.md). Such an unnested ShapeBinder can be used as the [Base Feature](PartDesign_Body#Base_Feature.md) for a new Body.
-   A ShapeBinder created from a sketch can have an opposite \"tool direction\". For example a [Pad](PartDesign_Pad.md) created from the sketch may extend in the +Y direction, while a [Pad](PartDesign_Pad.md), with the same properties, created from the ShapeBinder extends in the -Y direction. Toggling the **Reversed** property (or checkbox) will solve this.

## PartDesign SubShapeBinder vs. PartDesign ShapeBinder 

See [PartDesign SubShapeBinder](PartDesign_SubShapeBinder#PartDesign_SubShapeBinder_vs._PartDesign_ShapeBinder.md).

## Propiedades

-    **Support|LinkSubListGlobal**: support for the geometry.

-    **Trace Support|Bool**: Default is {{False}}. When {{True}}, the shape binder does observe relative placements of the parts and bodies (by manipulating values of its hidden **Placement** property).

## Example

The example uses the ShapeBinder Feature to make a hole (with or without threads) through more than one body. Normally the Hole function of the Part Design workbench is limited to a single body. The example uses two cubes facing each other but misaligned in an arbitrary way. The holes are created with sketches containing a circle for every hole (the diameter is ignored by the hole function). When you copy the sketch to the other cube it will be at the same position in the local cube coordinate system. In the image this is shown by the white circle on the back cube. This is not what we want, because the hole at that position would not be aligned to the hole in the front cube.

![](images/ShapeBinderThroughHole.png ) 
*Example setup for showing how to make holes through different bodies. The white circle shows that copying sketches is not enough*

Here is how you use the ShapeBinder Feature to achieve it:

1.  Prepare a scene as per the above image. If you use the cubes from the [Part workbench](Part_Workbench.md), remember that you must put them into a Body container. Each one in a single body container. Otherwise the [PartDesign](PartDesign_Workbench.md) functions would not work. If you build them from sketches the system should create body containers by default.
2.  In the [Property editor](Property_editor.md) change the placement of the second cube so that it touches the first cube with a side displacement.
3.  Select the PartDesign workbench
4.  Create a sketch on the front face of the first cube and place a circle anywhere and close the sketch
5.  Select the sketch in the tree and press the **<img src="images/PartDesign_Hole.svg" width=16px> [PartDesign Hole](PartDesign_Hole.md)** button. Before make sure the first body is the [active body](PartDesign_Body#Active_status.md) (double-click).
6.  Select a hole of appropriate size. The image above had also counterbore selected. Close the [Hole](PartDesign_Hole.md) function.

    :   Now the image should look as above. When you hide the first cube (select and press space) you can see that the hole does not reach the second cube. It will not, even when you select **Through All**, or when you enter a really large distance in the [Hole](PartDesign_Hole.md) task panel. The hole is always limited to a single body.
    :   Here is where our ShapeBinder comes in.
7.  First select the back cube. This is the target where the ShapeBinder will be added. It must be [actived](PartDesign_Body#Active_status.md) before, so be sure it has been double-clicked.
8.  In the tree select the sketch we used for the hole. It\'s important to not activate the first body.
9.  Select the shapeBinder function.

    :   A task panel should open. In the line **Object** the name of our sketch should be visible. If you had selected the function without selecting the sketch, you could press **Object** and then select the sketch from the list. It\'s recommended to select it first in order to get the right one, especially if you have many sketches with automatically generated names Sketch001,.. **Add Geometry** is not useful for us, because we want to select the whole sketch. **Add Geometry** is used if only parts should be selected.
10. Press **OK** to close the task panel and check that a new item has been added to the tree of the second cube.

    :   When you toggle the visibility of the ShapeBinder it is shown yellow in the [3D view](3D_view.md). However it\'s on the wrong position, just as the white circle in the image above. That is because of the default setting for the Trace parameter.
11. In the PropertyView of the ShapeBinder in the Data tab set the **Trace Support** parameter to true. The default was false.

    :   With **Trace Support** true, the ShapeBinder in not affected by local transformations of the target body, e.g. our translations. The shape remains exactly where the original front object shape has been. Try moving the front object around and you can see that the ShapeBinder always follows to the new position.
12. Select the ShapeBinder in the tree and press press the **<img src="images/PartDesign_Hole.svg" width=16px> [PartDesign Hole](PartDesign_Hole.md)** button. If you enter the same values as for the initial hole you will notice that no hole is created in the second cube. This is because a ShapeBinder in some cases has an opposite \"tool direction\" compared to the referenced sketch. To solve this check the Reverse checkbox. Press **OK** to finish.
13. You now have linked holes in two different bodies. If you change the position of the circle in the sketch, both holes will adapt. You can even add new circles in the sketch to create additional linked holes.


<div class="mw-translate-fuzzy">





</div>


{{PartDesign_Tools_ navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign ShapeBinder/es
