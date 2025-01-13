---
 GuiCommand:
   Name: FreeGrid StorageGrid
   MenuLocation: FreeeGrid , Storage grid
   Workbenches: FreeGrid_Workbench
   Version: 
   SeeAlso: 
---

# FreeGrid StorageGrid

## Description

The [FreeGrid StorageGrid](FreeGrid_StorageGrid.md) tool creates a storage grid.

This tool is part of the [FreeGrid Workbench](FreeGrid_Workbench.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md).

## Usage

1.  There are several ways to invoke the tool:
    -   Press the **<img src="images/FreeGrid_StorageGrid.svg" width=16px> [Storage grid](FreeGrid_StorageGrid.md)** button.
    -   Select the **FreeGrid → <img src="images/FreeGrid_StorageGrid.svg" width=16px> Storage grid** option from the menu.
2.  A storage grid is created with properties based on the current preferences.
3.  Optionally select the object and change its properties in the [Property editor](Property_editor.md).

## Properties

A FreeGrid StorageBox object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|Grid features}}

-    **Corner Connectors|Bool**: Default is `True`. Add cavities for corner connectors.

-    **Extra Bottom Material|Length**: Default is {{Value|16 mm}}. Extra thickness under the grid.

-    **Is Subtractive|Bool**: Default is `False`. Create a grid suitable for subtractive manufacturing.


{{Properties_Title|Magnet mount}}

-    **Include Magnets|Bool**: Default is `True`. Include magnet receptacles.

-    **Magnet Diameter|Length**: Default is {{Value|6 mm}}. Diameter of the magnets.

-    **Magnet Height|Length**: Default is {{Value|2 mm}}. Height of the magnets.


{{Properties_Title|Size}}

-    **Depth|IntegerConstraint**: Default is {{Value|2}}. Number of 50 mm units in the Y direction of the object.

-    **Width|IntegerConstraint**: Default is {{Value|3}}. Number of 50 mm units in the X direction of the object.



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [FreeGrid](Category_FreeGrid.md) > FreeGrid StorageGrid
