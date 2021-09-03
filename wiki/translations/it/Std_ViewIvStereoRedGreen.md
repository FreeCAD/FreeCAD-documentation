---
- GuiCommand:/it
   Name:Std ViewIvStereoRedGreen
   Name/it:Stereo rosso/ciano
   MenuLocation:Visualizza → Stereo → Stereo rosso/ciano
   Workbenches:Tutti
   SeeAlso:[Stereo quad buffer](Std_ViewIvStereoQuadBuff/it.md), [Stereo a righe interlacciate](Std_ViewIvStereoInterleavedRows/it.md), [Stereo a colonne interlacciate](Std_ViewIvStereoInterleavedColumns/it.md), [Stereo Off](Std_ViewIvStereoOff/it.md)
---

## Descrizione

The **Std ViewIvStereoRedGreen** command changes the active [3D view](3D_view.md) to red/cyan, [anaglyph](https://en.wikipedia.org/wiki/Anaglyph_3D), stereo view mode. To use this stereo mode glasses with colored lenses are requires.

## Utilizzo

1.  Select the **View → Stereo → <img src="images/Std_ViewIvStereoRedGreen.svg" width=16px> Stereo red/cyan** option from the menu.

## Preferenze

-   The eye to eye distance can be changed in the preferences: **Edit → Preferences... → Display → 3D View → Eye to eye distance for stereo modes**. See [Preferences Editor](Preferences_Editor#3D_View.md).

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

To change the view to red/cyan stereo use the `setStereoType` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('Anaglyph')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}  
