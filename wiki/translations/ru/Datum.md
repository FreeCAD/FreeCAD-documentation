# Datum/ru
## Введение

In FreeCAD the word \"[Datum](Datum.md)\" is normally used to refer to auxiliary geometry in the [PartDesign Workbench](PartDesign_Workbench.md). These geometrical elements will not form part of the final [Shape](Shape.md) of the [Body](Body.md), but can be used as references and supports for [sketches](Sketch.md) and other types of [features](Feature.md).

The following correspond to elements derived from the `Part::Datum` class, itself derived from [Part Feature](Part_Feature.md):

-   [PartDesign Point](PartDesign_Point.md)
-   [PartDesign Line](PartDesign_Line.md)
-   [PartDesign Plane](PartDesign_Plane.md)
-   [PartDesign CoordinateSystem](PartDesign_CoordinateSystem.md)

The following are derived directly from [Part Feature](Part_Feature.md):

-   [PartDesign ShapeBinder](PartDesign_ShapeBinder.md)
-   [PartDesign SubShapeBinder](PartDesign_SubShapeBinder.md)

## Применение

1.  Switch to the [PartDesign Workbench](PartDesign_Workbench.md).
2.  Press **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Body](PartDesign_Body.md)**.
3.  Select the Origin of the Body, and make it visible by pressing the **Space** bar in your keyboard.
4.  Press **[<img src=images/PartDesign_Plane.svg style="width:16px"> [PartDesign Plane](PartDesign_Plane.md)** to open the plane [task panel](task_panel.md).
5.  In the [3D view](3D_view.md), click on one of the standard planes, for example, the XY plane. Then press **OK** to close the task panel.
6.  Now in the [tree view](tree_view.md), select the newly created DatumPlane, and then press **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign NewSketch](PartDesign_NewSketch.md)**.
7.  Create a closed wire, and then use **[<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Pad](PartDesign_Pad.md)** to extrude the sketch, and create an initial solid.

Now you can move and rotate the DatumPlane as you wish, by changing its properties in the [property editor](property_editor.md), and the Sketch and Pad will follow its new [Placement](Placement.md).

You can add other types of datums to be used with other sketches and features.

## Примечания

Since they appeared in v0.17, datum objects were intended to be used inside [PartDesign Bodies](PartDesign_Body.md). However, since they are useful \"reference\" objects with different [attachment methods](Part_EditAttachment.md), it has been proposed that they should be available outside of the [PartDesign Workbench](PartDesign_Workbench.md). In this way, they will be usable in all workbenches as supporting geometry, particularly in the context of creating [assemblies](Assembly.md).

-   [Create and display local coordinate system](https://forum.freecadweb.org/viewtopic.php?f=10&t=2604)
-   [Datum objects in App::Part](https://forum.freecadweb.org/viewtopic.php?f=22&t=33654)
-   [Structure toolbar and datums](https://forum.freecadweb.org/viewtopic.php?t=42759)
-   [Local CS cannot be used in Part Wb?](https://forum.freecadweb.org/viewtopic.php?f=3&t=42960)


{{PartDesign Tools navi

}} {{Document objects navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [PartDesign](Category_PartDesign.md) > Datum/ru
