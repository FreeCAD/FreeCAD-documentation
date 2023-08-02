---
- GuiCommand:
   Name: Std ViewIvStereoQuadBuff
   MenuLocation: View -> Stereo -> Stereo quad buffer
   Workbenches: All
   SeeAlso: Std_ViewIvStereoRedGreen, Std_ViewIvStereoInterleavedRows, Std_ViewIvStereoInterleavedColumns, Std_ViewIvStereoOff
---

# Std ViewIvStereoQuadBuff

## Description

The **Std ViewIvStereoQuadBuff** command changes the active [3D view](3D_view.md) to quad buffer stereo view mode. To use this stereo mode a special graphics card, a special display and [shutter glasses](https://en.wikipedia.org/wiki/Active_shutter_3D_system) are requires.

## Usage

1.  Select the **View → Stereo → <img src="images/Std_ViewIvStereoQuadBuff.svg" width=16px> Stereo quad buffer** option from the menu.

## Preferences

-   The eye to eye distance can be changed in the preferences: **Edit → Preferences... → Display → 3D View → Eye to eye distance for stereo modes**. See [Preferences Editor](Preferences_Editor#3D_View.md).

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To change the view to quad buffer stereo use the `setStereoType` method of the ActiveView object. This method is not available if FreeCAD is in console mode.

 
```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('QuadBuffer')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```




 {{Std Base navi}}



---
⏵ [documentation index](../README.md) > Std ViewIvStereoQuadBuff
