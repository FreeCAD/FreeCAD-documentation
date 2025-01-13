---
 GuiCommand:
   Name: SheetMetal AddCutout
   MenuLocation: SheetMetal , Extruded Cutout
   Workbenches: SheetMetal_Workbench
   Shortcut: **E** **C**
   Version: 0.5.04
---

# SheetMetal AddCutout/en

## Description

The <img alt="" src=images/SheetMetal_AddCutout.svg  style="width:16px;"> [SheetMetal AddCutout](SheetMetal_AddCutout.md) command creates an extruded cutout from a sketch extrusion.

The difference between a \'normal\' cutout and an extruded cutout is that in the latter case the edges are made perpendicular to the selected face of the sheet metal object. The effect of the command is only visible if the sketch is not plane-parallel to the face.

![](images/SheetMetal_AddCutout_Example.png )



*Extruded cutout based on a circular sketch*

## Usage

1.  Select a planar face and a sketch with a closed contour (in any order).
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/SheetMetal_AddCutout.svg" width=16px> [Extruded Cutout](SheetMetal_AddCutout.md)** button.
    -   Select the **SheetMetal → <img src="images/SheetMetal_AddCutout.svg" width=16px> Extruded Cutout** option from the menu.
    -   Right-click in the [Tree view](Tree_view.md) or the [3D view](3D_view.md) and select the **SheetMetal → <img src="images/SheetMetal_AddCutout.svg" width=16px> Extruded Cutout** option from the context menu.
    -   Use the keyboard shortcut: **E** then **C**.
3.  The **Extruded Cutout Parameters** [Task panel](Task_panel.md) opens.
4.  Optionally press the **Face** button to reselect the planar face.
5.  Optionally press the **Sketch** button to reselect a sketch.
6.  Optionally adjust the parameters in the Task panel.
7.  Press the **OK** button to finish the command and close the Task panel.
8.  An **ExtrudedCutout** object will be created consisting of one or more holes in a line through the object.
9.  Optionally adjust the parameters in the [Property editor](Property_editor.md).

## Properties

See also: [Property editor](Property_editor.md).

A SheetMetal ExtrudedCutout object is derived from a [Part Feature](Part_Feature.md) object or, if it is inside a [PartDesign Body](PartDesign_Body.md), from a [PartDesign Feature](PartDesign_Feature.md) object, and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|Extruded Cutout}}

-    **Cut Side|Enumeration**: Default is {{value|Inside}}. Side of the cut.

-    **Cut Type|Enumeration**: Default is {{value|Through everything both sides}}. Cut type.

-    **Extrusion Length1|Length|hidden**: Default is {{value|500.0 mm}}. Length of the extrusion direction 1.

-    **Extrusion Length2|Length|hidden**: Default is {{value|500.0 mm}}. Length of the extrusion direction 2.

-    **Selected Face|LinkSub**: The selected object and face.

-    **Sketch|Link**: The sketch for the cut.


{{Properties_Title|Extruded Cutout Improvements}}

-    **Improve Cut|Bool**: Default is {{value|False}}. Improve cut geometry if it enters the cutting zone. Only select {{value|True}} if the cut needs fix, because it can be slow.

-    **Improve Level|IntegerConstraint|hidden**: Default is {{value|4}}. Level of cut improvement quality. More than 10 can take a very long time.

-    **Refine|Bool**: Default is {{value|False}}. Refine the geometry.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddCutout/en
