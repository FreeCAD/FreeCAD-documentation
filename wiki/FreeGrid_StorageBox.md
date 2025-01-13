---
 GuiCommand:
   Name: FreeGrid StorageBox
   MenuLocation: FreeeGrid , Storage box
   Workbenches: FreeGrid_Workbench
   Version: 
   SeeAlso: 
---

# FreeGrid StorageBox

## Description

The [FreeGrid StorageBox](FreeGrid_StorageBox.md) tool creates a storage box.

This tool is part of the [FreeGrid Workbench](FreeGrid_Workbench.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md).

## Usage

1.  There are several ways to invoke the tool:
    -   Press the **<img src="images/FreeGrid_StorageBox.svg" width=16px> [Storage box](FreeGrid_StorageBox.md)** button.
    -   Select the **FreeGrid → <img src="images/FreeGrid_StorageBox.svg" width=16px> Storage box** option from the menu.
2.  A storage box is created with properties based on the current preferences.
3.  Optionally select the object and change its properties in the [Property editor](Property_editor.md).

## Properties

A FreeGrid StorageBox object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|Box features}}

-    **Box Grip|Bool**: Default is `True`. Add grip/label area at the rear of the box.

-    **Box Grip Depth|Length**: Default is {{Value|15 mm}}. Depth of the grip.

-    **Box Open Front|Bool**: Default is `False`. Leave the front of the box open.

-    **Box Ramp|Bool**: Default is `True`. Add a scoop inside the front of the box.

-    **Floor Support|Bool**: Default is `True`. Add integral floor support.


{{Properties_Title|Internal divisions}}

-    **Division Height|Percent**: Default is {{Value|100}}. Height of internal divisions relative to the height of the box.

-    **Divisions X|IntegerConstraint**: Default is {{Value|1}}. Number of divisions along the X axis.

-    **Divisions Y|IntegerConstraint**: Default is {{Value|1}}. Number of divisions along the Y axis.


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
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [FreeGrid](Category_FreeGrid.md) > FreeGrid StorageBox
