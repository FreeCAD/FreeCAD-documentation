---
- GuiCommand   *
   Name   *Std SelBoundingBox
   MenuLocation   *View → Bounding box
   Workbenches   *All
   Version   *0.19
   SeeAlso   *[Std DrawStyle](Std_DrawStyle.md)
---

# Std SelBoundingBox/pl

## Description

The **Std SelBoundingBox** command toggles the global bounding box highlighting mode. If this mode is switched on, selected objects are marked in a [3D view](3D_view.md) with a highlighted bounding box even if their **Selection Style** is set to \'Shape\'.

## Usage

1.  There are several ways to invoke the command   *
    -   Press the **<img src="images/Std_SelBoundingBox.svg" width=16px> [Std SelBoundingBox](Std_SelBoundingBox.md)** button.
    -   Select the **View → <img src="images/Std_SelBoundingBox.svg" width=16px> Bounding box** option from the menu.

## Preferences

The related setting is stored   * **Tools → Edit parameters... → BaseApp → Preferences → View → ShowSelectionBoundingBox**. It is a boolean value, the default is `False`.

## Scripting


**See also   ***

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To change the ShowSelectionBoundingBox setting use the `SetBool` method of the appropriate ParameterGrp. The code sample does not work if FreeCAD is in console mode.


```python
import FreeCAD, FreeCADGui

grp = FreeCAD.ParamGet('User parameter   *BaseApp/Preferences/View')
if grp.GetBool('ShowSelectionBoundingBox')   *
  grp.SetBool('ShowSelectionBoundingBox',False)
else   *
  grp.SetBool('ShowSelectionBoundingBox',True)

FreeCADGui.updateCommands()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std SelBoundingBox/pl
