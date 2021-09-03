---
- GuiCommand:/it
   Name:Std ViewIvStereoOff
   Name/it:Stereo off
   MenuLocation:Visualizza → Stereo → Stereo off
   Workbenches:Tutti
   SeeAlso:[Stereo rosso/ciano](Std_ViewIvStereoRedGreen/it.md), [Stereo quad buffer](Std_ViewIvStereoQuadBuff/it.md),  [Stereo a righe interlacciate](Std_ViewIvStereoInterleavedRows/it.md), [Stereo a colonne interlacciate](Std_ViewIvStereoInterleavedColumns/it.md)
---

## Descrizione

The **Std ViewIvStereoOff** command switches off stereo mode in the active [3D view](3D_view.md).

## Utilizzo

1.  Select the **View → Stereo → <img src="images/Std_ViewIvStereoOff.svg" width=16px> Stereo Off** option from the menu.

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

To change the view to non-stereo use the `setStereoType` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('None')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}  
