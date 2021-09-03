---
- GuiCommand:
   Name:Std ViewIvStereoRedGreen
   MenuLocation:View → Stereo → Stereo red/cyan
   Workbenches:All
   SeeAlso:[Std ViewIvStereoQuadBuff](Std_ViewIvStereoQuadBuff.md), [Std ViewIvStereoInterleavedRows](Std_ViewIvStereoInterleavedRows.md), [Std ViewIvStereoInterleavedColumns](Std_ViewIvStereoInterleavedColumns.md), [Std ViewIvStereoOff](Std_ViewIvStereoOff.md)
---

## Description

The **Std ViewIvStereoRedGreen** command changes the active [3D view](3D_view.md) to red/cyan, [anaglyph](https://en.wikipedia.org/wiki/Anaglyph_3D), stereo view mode. To use this stereo mode glasses with colored lenses are requires.

## Usage

1.  Select the **View → Stereo → <img src="images/Std_ViewIvStereoRedGreen.svg" width=16px> Stereo red/cyan** option from the menu.

## Preferences

-   The eye to eye distance can be changed in the preferences: **Edit → Preferences... → Display → 3D View → Eye to eye distance for stereo modes**. See [Preferences Editor](Preferences_Editor#3D_View.md).

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To change the view to red/cyan stereo use the `setStereoType` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('Anaglyph')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}  
