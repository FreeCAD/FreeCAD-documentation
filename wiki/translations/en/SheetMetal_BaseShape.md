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

## Usage

1.  Activate the <img alt="" src=images/SheetMetal_BaseShape.svg  style="width:16px;"> **SheetMetal BaseShape** command using one of the following:
    -   The **<img src="images/SheetMetal_BaseShape.svg" width=16px> [Add base shape](SheetMetal_BaseShape.md)** button.
    -   The **SheetMetal → <img src="images/SheetMetal_BaseShape.svg" width=16px> Add base shape** menu option.
    -   The keyboard shortcut: **H**.
2.  The **Unfold sheet metal object** Task panel opens.
3.  Select the desired shape from the **Base shape type** options.
4.  Adjust the parameters.
5.  Press **OK** to finish the command.

## Properties

See also: [Property editor](Property_editor.md).

A SheetMetal BaseShape object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|Base}}

-    **Label|String**: Default value: The user editable name of this object, it may be any arbitrary UTF8 string.


{{Properties_Title|Parameters}}

-    **fill Gaps|Bool**: Extends side and flanges to close all gaps. Default: `True`.

-    **flangeWidth|Length**: Width of top flange. Default: {{Value|5,00 mm}}.

-    **height|Length**: Shape height. Default: {{Value|10,00 mm}}.

-    **length|Length**: Shape length. Default: {{Value|30,00 mm}}.

-    **radius|Length**: Bend Radius. Default: {{Value|1,00 mm}}.

-    **shape Type|Enumeration**: Base shape type. {{Value|L-Shape}} (default), {{Value|U-Shape}}, {{Value|Tub}}, {{Value|Hat}}, {{Value|Box}}.

-    **thickness|Length**: Thickness of sheetmetal. Default: {{Value|1,00 mm}}.

-    **width|Length**: Shape width. Default: {{Value|20,00 mm}}.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal BaseShape/en
