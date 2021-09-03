---
- GuiCommand:
   Name:Std ViewIvStereoInterleavedRows
   MenuLocation:View → Stereo → Stereo interleaved Rows
   Workbenches:All
   SeeAlso:[Std ViewIvStereoRedGreen](Std_ViewIvStereoRedGreen.md), [Std ViewIvStereoQuadBuff](Std_ViewIvStereoQuadBuff.md), [Std ViewIvStereoInterleavedColumns](Std_ViewIvStereoInterleavedColumns.md), [Std ViewIvStereoOff](Std_ViewIvStereoOff.md)
---

## Beschreibung

The **Std ViewIvStereoInterleavedRows** command changes the active [3D view](3D_view.md) to interleaved rows stereo view mode. To use this stereo mode a special graphics card, a special display and [glasses with polarized lenses](https://en.wikipedia.org/wiki/Polarized_3D_system) are requires.

## Anwendung

1.  Select the {{MenuCommand|View → Stereo → <img src="images/Std_ViewIvStereoInterleavedRows.svg" width=16px> Stereo interleaved Rows}} option from the menu.

## Preferences

-   The eye to eye distance can be changed in the preferences: {{MenuCommand|Edit → Preferences... → Display → 3D View → Eye to eye distance for stereo modes}}. See [Preferences Editor](Preferences_Editor#3D_View.md).

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To change the view to interleaved rows stereo use the `setStereoType` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('InterleavedRows')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}  
