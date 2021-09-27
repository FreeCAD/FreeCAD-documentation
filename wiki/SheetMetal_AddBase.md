---
- GuiCommand:
   Name:SheetMetal AddBase
   MenuLocation:SheetMetal → Make Base Wall
   Workbenches:[SheetMetal](SheetMetal_Workbench.md)
   Shortcut:**C** **B**
---

# SheetMetal AddBase

## Description

The <img alt="" src=images/SheetMetal_AddBase.svg  style="width:24px;"> **SheetMetal AddBase** command creates a sheetmetal wall from a sketch.

## Usage

The tool creates a sheet based on a sketch:

-   An open sketch contour gets extruded by {{Parameter|length}}, creating a sheet of {{Parameter|thickness}} with corners rounded to {{Parameter|radius}}. The parameter {{Parameter|bend side}} determines the orientation of the sheet relative to the line.
-   A closed sketch contour gets extruded to a sheet of {{Parameter|thickness}}. In this case {{Parameter|length}} and {{Parameter|radius}} are not used.

 <img alt="" src=images/Sheetmetal.png  style="width:400px;"> 

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






_ _ _

---
[documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > SheetMetal AddBase
