---
 GuiCommand:
   Name: FreeGrid StorageGrid
   MenuLocation: FreeeGrid , Storage grid
   Workbenches: FreeGrid_Workbench
   Version: 
   SeeAlso: 
---

# FreeGrid StorageGrid/pl


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Description


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The [FreeGrid StorageGrid](FreeGrid_StorageGrid.md) tool creates a storage grid.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

This tool is part of the [FreeGrid Workbench](FreeGrid_Workbench.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Usage


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  There are several ways to invoke the tool:
    -   Press the **<img src="images/FreeGrid_StorageGrid.svg" width=16px> [Storage grid](FreeGrid_StorageGrid.md)** button.
    -   Select the **FreeGrid → <img src="images/FreeGrid_StorageGrid.svg" width=16px> Storage grid** option from the menu.
2.  A storage grid is created with properties based on the current preferences.
3.  Optionally select the object and change its properties in the [Property editor](Property_editor.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Properties


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

A FreeGrid StorageBox object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Data


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">


{{Properties_Title|Grid features}}


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-    **Corner Connectors|Bool**: Default is `True`. Add cavities for corner connectors.

-    **Extra Bottom Material|Length**: Default is {{Value|16 mm}}. Extra thickness under the grid.

-    **Is Subtractive|Bool**: Default is `False`. Create a grid suitable for subtractive manufacturing.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">


{{Properties_Title|Magnet mount}}


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-    **Include Magnets|Bool**: Default is `True`. Include magnet receptacles.

-    **Magnet Diameter|Length**: Default is {{Value|6 mm}}. Diameter of the magnets.

-    **Magnet Height|Length**: Default is {{Value|2 mm}}. Height of the magnets.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">


{{Properties_Title|Size}}


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-    **Depth|IntegerConstraint**: Default is {{Value|2}}. Number of 50 mm units in the Y direction of the object.

-    **Width|IntegerConstraint**: Default is {{Value|3}}. Number of 50 mm units in the X direction of the object.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">





</div>



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [FreeGrid](Category_FreeGrid.md) > FreeGrid StorageGrid/pl
