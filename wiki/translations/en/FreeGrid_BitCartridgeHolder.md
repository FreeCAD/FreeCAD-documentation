---
 GuiCommand:
   Name: FreeGrid BitCartridgeHolder
   MenuLocation: FreeeGrid , Bit cartridge holder
   Workbenches: FreeGrid_Workbench
   Version: 
   SeeAlso: 
---

# FreeGrid BitCartridgeHolder/en

## Description

The [FreeGrid BitCartridgeHolder](FreeGrid_BitCartridgeHolder.md) tool creates a bit cartridge holder.

This tool is part of the [FreeGrid Workbench](FreeGrid_Workbench.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md).

## Usage

1.  There are several ways to invoke the tool:
    -   Press the **<img src="images/FreeGrid_BitCartridgeHolder.svg" width=16px> [Bit cartridge holder](FreeGrid_BitCartridgeHolder.md)** button.
    -   Select the **FreeGrid → <img src="images/FreeGrid_BitCartridgeHolder.svg" width=16px> Bit cartridge holder** option from the menu.
2.  A bit cartridge holder is created with properties based on the current preferences.
3.  Optionally select the object and change its properties in the [Property editor](Property_editor.md).

## Properties

A FreeGrid BitCartridgeHolder object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|Bit Cartridge Holder features}}

-    **Side Length|Length**: Default is {{value|15.0 mm}}. Length of the longest side of the holder.


{{Properties_Title|Box features}}

-    **Floor Support|Bool**: Default is `True`. Add integral floor support.


{{Properties_Title|Magnet mount}}

-    **Magnet Diameter|Length**: Default is {{Value|6 mm}}. Diameter of the magnets.

-    **Magnet Height|Length**: Default is {{Value|2 mm}}. Height of the magnets.

-    **Magnet Option|Enumeration**: Default is {{Value|allIntersections}}. Positions of the magnets. The other options are: {{Value|cornersOny}} and {{Value|noMagnets}}.


{{Properties_Title|Position on grid}}

-    **Position X|IntegerConstraint**: Default is {{Value|0}}. Object position on the grid along the X axis. Starts at zero.

-    **Position Y|IntegerConstraint**: Default is {{Value|0}}. Object position on the grid along the Y axis. Starts at zero.


{{Properties_Title|Size}}

-    **Depth|IntegerConstraint**: Default is {{Value|1}}. Number of 50 mm units in the Y direction of the object.

-    **Height|Length**: Default is {{Value|50 mm}}. Height of the object.

-    **Width|IntegerConstraint**: Default is {{Value|1}}. Number of 50 mm units in the X direction of the object.



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [FreeGrid](Category_FreeGrid.md) > FreeGrid BitCartridgeHolder/en
