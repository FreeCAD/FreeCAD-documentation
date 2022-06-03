---
- GuiCommand   *
   Name   *Std ViewIvStereoInterleavedColumns
   MenuLocation   *View → Stereo → Stereo interleaved Columns
   Workbenches   *All
   SeeAlso   *[Std ViewIvStereoRedGreen](Std_ViewIvStereoRedGreen.md), [Std ViewIvStereoQuadBuff](Std_ViewIvStereoQuadBuff.md), [Std ViewIvStereoInterleavedRows](Std_ViewIvStereoInterleavedRows.md), [Std ViewIvStereoOff](Std_ViewIvStereoOff.md)
---

# Std ViewIvStereoInterleavedColumns/pl

## Description

The **Std ViewIvStereoInterleavedColumns** command changes the active [3D view](3D_view.md) to interleaved columns stereo view mode. To use this stereo mode a special graphics card, a special display and [glasses with polarized lenses](https   *//en.wikipedia.org/wiki/Polarized_3D_system) are requires.

## Usage

1.  Select the **View → Stereo → <img src="images/Std_ViewIvStereoInterleavedColumns.svg" width=16px> Stereo interleaved Columns** option from the menu.

## Preferences

-   The eye to eye distance can be changed in the preferences   * **Edit → Preferences... → Display → 3D View → Eye to eye distance for stereo modes**. See [Preferences Editor](Preferences_Editor#3D_View.md).

## Scripting


**See also   ***

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To change the view to interleaved columns stereo use the `setStereoType` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('InterleavedColumns')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewIvStereoInterleavedColumns/pl
