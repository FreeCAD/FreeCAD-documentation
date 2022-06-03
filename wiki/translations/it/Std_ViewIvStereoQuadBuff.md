---
- GuiCommand   */it
   Name   *Std ViewIvStereoQuadBuff
   Name/it   *Stereo quad buffer
   MenuLocation   *Visualizza → Stereo → Stereo quad buffer
   Workbenches   *Tutti
   SeeAlso   *[Stereo rosso/ciano](Std_ViewIvStereoRedGreen/it.md), [Stereo a righe interlacciate](Std_ViewIvStereoInterleavedRows/it.md), [Stereo a colonne interlacciate](Std_ViewIvStereoInterleavedColumns/it.md), [Stereo Off](Std_ViewIvStereoOff/it.md)
---

# Std ViewIvStereoQuadBuff/it

## Descrizione

The **Std ViewIvStereoQuadBuff** command changes the active [3D view](3D_view.md) to quad buffer stereo view mode. To use this stereo mode a special graphics card, a special display and [shutter glasses](https   *//en.wikipedia.org/wiki/Active_shutter_3D_system) are requires.

## Utilizzo

1.  Select the **View → Stereo → <img src="images/Std_ViewIvStereoQuadBuff.svg" width=16px> Stereo quad buffer** option from the menu.

## Preferenze

-   The eye to eye distance can be changed in the preferences   * **Edit → Preferences... → Display → 3D View → Eye to eye distance for stereo modes**. See [Preferences Editor](Preferences_Editor#3D_View.md).

## Script


**Vedere anche   ***

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

To change the view to quad buffer stereo use the `setStereoType` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('QuadBuffer')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewIvStereoQuadBuff/it
