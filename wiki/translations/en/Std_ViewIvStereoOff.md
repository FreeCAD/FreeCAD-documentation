---
 GuiCommand:
   Name: Std ViewIvStereoOff
   MenuLocation: View , Stereo , Stereo Off
   Workbenches: All
   SeeAlso: Std_ViewIvStereoRedGreen, Std_ViewIvStereoQuadBuff, Std_ViewIvStereoInterleavedRows, Std_ViewIvStereoInterleavedColumns
---

# Std ViewIvStereoOff/en

## Description

The **Std ViewIvStereoOff** command switches off stereo mode in the active [3D view](3D_view.md).

## Usage

1.  Select the **View → Stereo → <img src="images/Std_ViewIvStereoOff.svg" width=16px> Stereo Off** option from the menu.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To change the view to non-stereo use the `setStereoType` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('None')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewIvStereoOff/en
