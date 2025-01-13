---
 GuiCommand:
   Name: SheetMetal BaseShape
   MenuLocation: SheetMetal , Add base shape
   Workbenches: SheetMetal_Workbench
   Version: 0.3.10
   Shortcut: **H**
---

# SheetMetal BaseShape/en

## Description

The <img alt="" src=images/SheetMetal_BaseShape.svg  style="width:24px;"> **SheetMetal BaseShape** command creates a SheetMetal BaseShape object from parameters.

<img alt="" src=images/SheetMetal_BaseShape-01.png  style="width:400px;">



*The five available BaseShapes: L-shape, U-shape, Tub, Hat, and Box*

A rectangular sixth shape, called Flat, was introduced in v 0.4.10.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/SheetMetal_BaseShape.svg" width=16px> [Add base shape](SheetMetal_BaseShape.md)** button.
    -   Select the **SheetMetal → <img src="images/SheetMetal_BaseShape.svg" width=16px> Add base shape** option from the menu.
    -   Right-click in the [Tree view](Tree_view.md) or the [3D view](3D_view.md) and select the **SheetMetal → <img src="images/SheetMetal_BaseShape.svg" width=16px> Add base shape** option from the context menu.
    -   Use the keyboard shortcut: **H**.
2.  The **Generate Sheet Metal base shape** [Task panel](Task_panel.md) opens.
3.  Select the desired shape from the **Base shape type** options.
4.  Select the position of the origin in the **Location of part origin** widget.
5.  Optionally adjust the parameters in the Task panel.
6.  Press the **OK** button to finish the command and close the Task panel.
7.  A **BaseShape** object will be created.
8.  Optionally adjust the parameters in the [Property editor](Property_editor.md).

## Properties

See also: [Property editor](Property_editor.md).

A SheetMetal BaseShape object is derived from a [Part Feature](Part_Feature.md) object or, if it is inside a [PartDesign Body](PartDesign_Body.md), from a [PartDesign Feature](PartDesign_Feature.md) object, and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|Parameters}}

-    **fill Gaps|Bool**: Extends side and flanges to close all gaps. Default: `True`.

-    **flangeWidth|Length**: Width of top flange. Default: {{Value|5,00 mm}}.

-    **height|Length**: Shape height. Default: {{Value|10,00 mm}}.

-    **length|Length**: Shape length. Default: {{Value|30,00 mm}}.

-    **origin Loc|Enumeration**: Origin location.

    :   
        {{Value|-X,-Y}}
        
        , {{Value|-X,0}}, {{Value|-X,+Y}}, {{Value|0,-Y}}, {{Value|0,0}} (default), {{Value|0,+Y}}, {{Value|+X,-Y}}, {{Value|+X,0}}, and {{Value|+X,+Y}}

-    **radius|Length**: Bend Radius. Default: {{Value|1,00 mm}}.

-    **shape Type|Enumeration**: Base shape type.

    :   
        {{Value|Flat}}
        
        (introduced in v 0.4.10), {{Value|L-Shape}} (default), {{Value|U-Shape}}, {{Value|Tub}}, {{Value|Hat}}, and {{Value|Box}}.

-    **thickness|Length**: Thickness of sheetmetal. Default: {{Value|1,00 mm}}.

-    **width|Length**: Shape width. Default: {{Value|20,00 mm}}.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal BaseShape/en
