---
- GuiCommand:
   Name:SheetMetal AddJunction
   MenuLocation:SheetMetal - Make Junction
   Workbenches:[SheetMetal](SheetMetal_Workbench.md)
   Shortcut:**S** **J**
   SeeAlso:[SheetMetal AddRelief](SheetMetal_AddRelief.md), [SheetMetal AddBend](SheetMetal_AddBend.md)
---

# SheetMetal AddJunction

## Description

The <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:24px;"> [SheetMetal AddJunction](SheetMetal_AddJunction.md) command creates open junctions between two sections (walls/flanges) of a sheet metal object. Without these junctions sheet metal sections connected to the same base will not be unfoldable.

This command is the second of three steps to convert a shell object made with the [Part Workbench](Part_Workbench.md) or [PartDesign Workbench](PartDesign_Workbench.md) into an unfoldable sheet metal object:

1.  [SheetMetal AddRelief](SheetMetal_AddRelief.md)
2.  [SheetMetal AddJunction](SheetMetal_AddJunction.md)
3.  [SheetMetal AddBend](SheetMetal_AddBend.md)

 <img alt="" src=images/SheetMetal_ConvertShellObject-01.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-02.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-04.png  style="width:100px;">  
*Make Junction - cut edges open*

## Usage

1.  Select one or more edge(s).
2.  Activate the <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:16px;"> **SheetMetal AddJunction** command using one of the following:
    -   The **<img src="images/SheetMetal_AddJunction.svg" width=16px> [SheetMetal AddJunction](SheetMetal_AddJunction.md)** button.
    -   The **SheetMetal → <img src="images/SheetMetal_AddJunction.svg" width=16px> Make Junction** menu option.
    -   The keyboard shortcut: **S** then **J**.

 <img alt="" src=images/SheetMetal_ConvertShellObject-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-07.png  style="width:200px;"> 

## Notes

The commands <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> **[SheetMetal AddRelief](SheetMetal_AddRelief.md)**, <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:16px;"> **[SheetMetal AddJunction](SheetMetal_AddJunction.md)**, and <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> **[SheetMetal AddBend](SheetMetal_AddBend.md)** work best with hollow cuboids i.e. shell objects with a constant thickness and only 90° angles between faces.

See [SheetMetal AddRelief](SheetMetal_AddRelief#Notes.md) for hints about creating shell objects of cuboids.

## Properties

See also: [Property editor](Property_editor.md).

A SheetMetal Junction object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties and its label has a default value:

### Data


{{Properties_Title|Base}}

-    **Label|String**: Default value: The user editable name of this object, it may be any arbitrary UTF8 string.

-    **Base Feature|Link|hidden**: Base Feature. Link to the parent feature.

-    **_Body|LinkHidden|hidden**: Hidden link to the parent body.


{{Properties_Title|Parameters}}

-    **base Object|LinkSub**: \"Base Object\". Links to the edges defining gap/junction positions.

-    **gap|Length**: \"Junction Gap\". Default: {{value|2,00 mm}}.Size of gap/junction to be added.



---
![](images/Button_right.svg) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddJunction
