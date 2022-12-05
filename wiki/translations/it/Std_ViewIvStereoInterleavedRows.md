---
- GuiCommand:/it
   Name:Std ViewIvStereoInterleavedRows
   Name/it:Stereo a righe interlacciate
   MenuLocation:Visualizza → Stereo → Stereo a righe interlacciate
   Workbenches:Tutti
   SeeAlso:[Stereo rosso/ciano](Std_ViewIvStereoRedGreen/it.md), [Stereo quad buffer](Std_ViewIvStereoQuadBuff/it.md),  [Stereo a colonne interlacciate](Std_ViewIvStereoInterleavedColumns/it.md), [Stereo Off](Std_ViewIvStereoOff/it.md)
---

# Std ViewIvStereoInterleavedRows/it

## Descrizione

The **Std ViewIvStereoInterleavedRows** command changes the active [3D view](3D_view.md) to interleaved rows stereo view mode. To use this stereo mode a special graphics card, a special display and [glasses with polarized lenses](https://en.wikipedia.org/wiki/Polarized_3D_system) are requires.

## Utilizzo

1.  Select the **View → Stereo → <img src="images/Std_ViewIvStereoInterleavedRows.svg" width=16px> Stereo interleaved Rows** option from the menu.

## Preferenze

-   The eye to eye distance can be changed in the preferences: **Edit → Preferences... → Display → 3D View → Eye to eye distance for stereo modes**. See [Preferences Editor](Preferences_Editor#3D_View.md).

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

To change the view to interleaved rows stereo use the `setStereoType` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('InterleavedRows')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewIvStereoInterleavedRows/it
