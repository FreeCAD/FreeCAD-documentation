---
 GuiCommand:
   Name: SheetMetal AddBase
   MenuLocation: SheetMetal , Make Base Wall
   Workbenches: SheetMetal_Workbench
   Shortcut: **C** **B**
---

# SheetMetal AddBase/it

## Description

The <img alt="" src=images/SheetMetal_AddBase.svg  style="width:24px;"> **SheetMetal AddBase** command creates a SheetMetal base object from a sketch.

From an open contour it creates a prismatic **profile**:

<img alt="" src=images/SheetMetal_AddBase-01.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddBase-02.png  style="width:200px;">

From a closed outline it creates a base **plate** (blank):

<img alt="" src=images/SheetMetal_AddBase-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddBase-04.png  style="width:200px;">

## Usage

### Profile

1.  Select an **open contour** <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [sketch](Sketcher_Workbench.md).
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase.md)** button.
    -   Select the **Sheet Metal → <img src="images/SheetMetal_AddBase.svg" width=16px> Make Base Wall** option from the menu.
    -   Right-click in the [Tree view](Tree_view.md) or the [3D view](3D_view.md) and select the **Sheet Metal → <img src="images/SheetMetal_AddBase.svg" width=16px> Make Base Wall** option from the context menu.
    -   Use the keyboard shortcut: **C** then **B**.
3.  A **BaseBend** object will be created, corners along the contour are automatically converted into cylindrical bends.
4.  Adjust the profile parameters in the [Property editor](Property_editor.md):
    -   
        **length**
        
        for the extrusion length of the profile,

    -   
        **thickness**
        
        for the wall thickness of the profile,

    -   
        **radius**
        
        for the inner radius of automatically added bends.

### Plate

1.  Select a **closed outline** <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [sketch](Sketcher_Workbench.md).
2.  Invoke the command as described above.
3.  Adjust the plate parameters in the [Property editor](Property_editor.md):
    -   
        **thickness**
        
        for the thickness of the plate.

:   

    :   (**length** and **radius** are not used for plates.)

## Properties

See also: [Property editor](Property_editor.md).

A SheetMetal BaseBend object is derived from a [Part Feature](Part_Feature.md) object or, if it is inside a [PartDesign Body](PartDesign_Body.md), from a [PartDesign Feature](PartDesign_Feature.md) object, and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|Parameters}}

-    **Bend Side|Enumeration**: \"Relief Type\", defines on which side of a profile curve the thickness applies. {{value|Outside}} (default), {{value|Inside}}, {{value| Middle}}. (not used for plates)

-    **Bend Sketch|Link**: \"Wall Sketch object\". Link to the profile/outline sketch.

-    **Mid Plane|Bool**: \"Extrude Symmetric to Plane\". The length of a profile or the thickness of a plate extends to one side of the sketch plane if `False` (default) or symmetrically to both sides if `True`.

-    **Reverse|Bool**: Reverses the direction of a profile extrusion or a plate thickness. Default: `False`.

-    **length|Length**: Extrusion length of a profile. Default: {{value|100,00 mm}}. (not used for plates)

-    **radius|Length**: Inner radius of automatically added bends. Default: {{value|1,00 mm}}. (not used for plates)

-    **thickness|Length**: Wall thickness of a sheetmetal profile or plate. Default: {{value|1,00 mm}}.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddBase/it
