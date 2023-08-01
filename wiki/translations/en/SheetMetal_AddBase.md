---
- GuiCommand:
   Name: SheetMetal AddBase
   MenuLocation: SheetMetal - Make Base Wall
   Workbenches: [SheetMetal](SheetMetal_Workbench.md)
   Shortcut: **C** **B**
---

# SheetMetal AddBase/en

## Description

The <img alt="" src=images/SheetMetal_AddBase.svg  style="width:24px;"> **SheetMetal AddBase** command creates a SheetMetal base object from a sketch.

From an open contour it creates a prismatic **profile**:

<img alt="" src=images/SheetMetal_AddBase-01.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddBase-02.png  style="width:200px;">

From a closed outline it creates a base **plate** (blank):

<img alt="" src=images/SheetMetal_AddBase-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddBase-04.png  style="width:200px;">

## Usage

### Profile

1.  Select an **open contour** <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [sketch](Sketcher_Workbench.md).
2.  Activate the <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [SheetMetal AddBase](SheetMetal_AddBase.md) command using one of the following:
    -   The **<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase.md)** button.
    -   The **SheetMetal → <img src="images/SheetMetal_AddBase.svg" width=16px> Make Base Wall** menu option.
    -   The keyboard shortcut: **C** then **B**.
3.  Adjust the profile\'s parameters by editing the corresponding values in the [Property editor](Property_editor.md):
    -   The property **length** for the profile length,
    -   The property **thickness** for the profile thickness,
    -   The property **radius** for the inner radius of the bends.

### Plate

1.  Select a **closed outline** <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [sketch](Sketcher_Workbench.md).
2.  Activate the <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [SheetMetal AddBase](SheetMetal_AddBase.md) command (see above).
3.  Adjust the plate\'s parameter by editing the corresponding value in the [Property editor](Property_editor.md):
    -   The property **thickness** for the thickness of the plate.

:   

    :   (The properties **length** and **radius** are not used for plates.)

## Properties

See also: [Property editor](Property_editor.md).

A SheetMetal BaseBend object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|Base}}

-    **Label|String**: Default value: The user editable name of this object, it may be any arbitrary UTF8 string.

-    **Base Feature|Link|hidden**: Base Feature. Link to the parent feature.

-    **_Body|LinkHidden|hidden**: Hidden link to the parent body.


{{Properties_Title|Parameters}}

-    **Bend Side|Enumeration**: \"Relief Type\". {{value|Outside}} (default), {{value|Inside}}, {{value| Middle}}.

-    **Bend Sketch|Link**: \"Wall Sketch object\". Link to the profile/outline sketch.

-    **Mid Plane|Bool**: \"Extrude Symmetric to Plane\".   `True`, the profile extends symmetrically to both sides of the sketch plane.

-    **Reverse|Bool**: \"Reverse Extrusion Direction\". Default: `False`.

-    **length|Length**: \"Length of wall\". Default: {{value|100,00 mm}}.

-    **radius|Length**: \"Bend Radius\". Default: {{value|1,00 mm}}.

-    **thickness|Length**: \"Thickness of sheetmetal\". Default: {{value|1,00 mm}}.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddBase/en
